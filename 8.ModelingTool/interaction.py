# coding=utf-8
from collections import defaultdict
from OpenGL.GLUT import glutGet, glutKeyboardFunc, glutMotionFunc, glutMouseFunc, glutPassiveMotionFunc, \
    glutPostRedisplay, glutSpecialFunc
from OpenGL.GLUT import GLUT_LEFT_BUTTON, GLUT_RIGHT_BUTTON, GLUT_MIDDLE_BUTTON, GLUT_WINDOW_HEIGHT, \
    GLUT_WINDOW_WIDTH, GLUT_DOWN, GLUT_KEY_UP, GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT
import trackball


class Interaction(object):
    def __init__(self):
        # 被按下的健
        self.pressed = None
        # 轨迹球
        self.trackball = trackball.Trackball(theta=-25, distance=15)
        # 当前鼠标位置
        self.mouse_loc = None
        # 回调函数词典
        self.callbacks = defaultdict(list)

        self.register()

    # 注册glut的事件回调函数
    def register(self):
        glutMouseFunc(self.handle_mouse_button)
        glutMotionFunc(self.handle_mouse_move)
        glutKeyboardFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_keystroke)

    # 当鼠标按键被点击或者释放的时候调用
    def handle_mouse_button(self, button, mode, x, y):
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - y  # OpenGL原点在窗口左下角，窗口原点在左上角，所以需要这种转换。
        self.mouse_loc = (x, y)

        # 鼠标按键按下的时候
        if mode == GLUT_DOWN:
            self.pressed = button
            if button == GLUT_RIGHT_BUTTON:
                pass
            elif button == GLUT_LEFT_BUTTON:
                self.trigger('pick', x, y)
        # 鼠标按键被释放的时候
        else:
            self.pressed = None
            # 标记当前窗口需要重新绘制
            glutPostRedisplay()

    # 鼠标移动时调用
    def handle_mouse_move(self, x, screen_y):
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - screen_y  # OpenGL原点在窗口左下角，窗口原点在左上角，所以需要这种转换
        if self.pressed is not None:
            dx = x - self.mouse_loc[0]
            dy = y - self.mouse_loc[1]
            if self.pressed == GLUT_RIGHT_BUTTON and self.trackball is not None:
                # 变化场景的角度
                self.trackball.drag_to(self.mouse_loc[0], self.mouse_loc[1], dx, dy)
            elif self.pressed == GLUT_LEFT_BUTTON:
                self.trigger('move', x, y)
            elif self.pressed == GLUT_MIDDLE_BUTTON:
                self.translate(dx / 60.0, dy / 60.0, 0)
            else:
                pass
            glutPostRedisplay()
        self.mouse_loc = (x, y)

    # 键盘输入时调用
    def handle_keystroke(self, key, x, screen_y):
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - screen_y
        if key == 's':
            self.trigger('place', 'sphere', x, y)
        elif key == 'c':
            self.trigger('place', 'cube', x, y)
        elif key == GLUT_KEY_UP:
            self.trigger('scale', up=True)
        elif key == GLUT_KEY_DOWN:
            self.trigger('scale', up=False)
        elif key == GLUT_KEY_LEFT:
            self.trigger('rotate_color', forward=True)
        elif key == GLUT_KEY_RIGHT:
            self.trigger('rotate_color', forward=False)
        glutPostRedisplay()

    # 第一个参数指明行为期望的效果，后续参数为该效果的参数
    def trigger(self, name, *args, **kwargs):
        # 取得callbacks词典下该效果对应的所有方法逐一调用
        for func in self.callbacks[name]:
            func(*args, **kwargs)

    # 注册回调函数
    def register_callback(self, name, func):
        self.callbacks[name].append(func)