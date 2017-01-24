#coding=utf-8   
class bird(object):
    feather = True
    
class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def getAdult(self):
        if self.age > 1.0: 
            return True
        else: 
            return False
    adult = property(getAdult)
    
summer = chicken(2)
print(summer.adult)

summer.age = 0.5
print(summer.adult)


class num(object):
    def __init__(self, value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self, value):
        self.value = -value
    def delNeg(self):
        print("value also deleted")
        del self.value
    #property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。
    neg = property(getNeg, setNeg, delNeg, "I'm negative")
    
x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg