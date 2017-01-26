# coding=utf-8
from PIL import Image
import hashlib
import math
import os


# 向量空间比较
class VectorCompare:
    def __init__(self):
        pass

    # 计算矢量大小
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的cos值
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


# 将图片转换为矢量
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 加载训练集
imageset = []
for letter in iconset:
    for img in os.listdir('python_captcha/iconset/%s' % letter):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open("python_captcha/iconset/%s/%s" % (letter, img))))
        imageset.append({letter: temp})

im = Image.open("python_captcha/captcha.gif")
# 将图片转换为8位像素模式
im.convert("P")
im2 = Image.new("P", im.size, 255)

# 提取圆图片的验证码，重新构建黑白图片
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        # 220,227是红色与灰色的颜色代码
        if pix == 220 or pix == 227:
            im2.putpixel((y, x), 0)

# im2.show()

# 得到单个字符的像素集合
inletter = False
foundletter = False
start = 0
end = 0

# 存储每个字符的起始列数和结束结束
letters = []

# 将图片纵向分割
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter = False

# print letters

count = 0
# 对图片切割，得到每个字符所在的那部分图片
for letter in letters:
    m = hashlib.md5()
    # 分割图片
    im3 = im2.crop([letter[0], 0, letter[1], im2.size[1]])
    # m.update("%s%s"%(time.time(),count))
    # im3.save("./%s.gif"%(m.hexdigest()))

    guess = []

    # 将切割得到的验证码与每个训练集进行比较
    for image in imageset:
        for x, y in image.iteritems():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(im3)), x))

    guess.sort(reverse=True)
    print "", guess[0]
    count += 1
