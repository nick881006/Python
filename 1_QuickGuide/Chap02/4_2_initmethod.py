class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

class happyBird(Bird):
    def __init__(self, words):
        print 'We are happy birds', words

summer = happyBird('12345')