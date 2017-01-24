class Human(object):
    def __init__(self,input_gender):
        self.gender = input_gender
    def printGender(self):
        print self.gender
        
nick = Human('male')
nick.printGender()