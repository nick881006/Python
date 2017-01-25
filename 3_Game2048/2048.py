# coding=utf-8
import curses
from random import randrange, choice
from collections import defaultdict

# 用户行为
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# 有效键值
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# 输入与行为关联
actions_dict = dict(zip(letter_codes, actions * 2))


# 用户输入处理
# 循环+阻塞，直到获得用户有效输入才返回对应行为
# 根据键盘输入返回对应action：'Up','Left','Down','Right','Restart','Exit'
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


# 矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]


# 矩阵逆转
def invert(field):
    return [row[::-1] for row in field]


# 创建棋盘，可以指定棋盘的高和宽以及游戏胜利条件，默认是最经典得到4*4～2048
class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height  # 高
        self.width = width  # 宽
        self.win_value = win  # 过关分数
        self.score = 0  # 当前分数
        self.highscore = 0  # 最高分
        self.reset()  # 棋盘重置

    # 随机生成一个2或者4
    def spawn(self):
        if randrange(100) > 89:
            new_element = 4
        else:
            new_element = 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    # 重置棋盘
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    # 棋盘走一步,通过矩阵转置与逆转，可以直接从左移得到其余三个方向的移动操作
    def move(self, direction):
        # 左移
        def move_row_left(row):
            # 把零散的非零单元挤到一块
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            # 对邻近元素进行合并
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            # 先挤到一块再合并再挤到一块
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                # 可以移动
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                # 可以合并
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    # 绘制棋盘
    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '(R)Restart (Q)Exit'
        gameover_string = 'Game Over'
        win_string = 'Win'

        def cast(string):
            screen.addstr(string + '\n')

        # 绘制水平分割线
        def draw_hor_seperator():
            line = '+' + ('+------' * self.width + '+')[1:]
            seperator = defaultdict(lambda: line)
            if not hasattr(draw_hor_seperator, "counter"):
                draw_hor_seperator.counter = 0
            cast(seperator[draw_hor_seperator.counter])
            draw_hor_seperator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHEST SCORE: ' + str(self.highscore))

        for row in self.field:
            draw_hor_seperator()
            draw_row(row)

        draw_hor_seperator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)


# 主逻辑代码
def main(stdscr):
    def init():
        # 重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        # 画出Game Over或者Win的界面
        game_field.draw(stdscr)
        # 读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)
        # 对应不同行为转换到不同的状态
        responses['Restart'] = 'Init'
        responses['Exit'] = 'Exit'
        return responses[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入得到action
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        # if成功移动了一步
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }

    curses.use_default_colors()
    game_field = GameField(win=2048)

    state = 'Init'

    # 状态及开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)