class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self,x,y):
        position=[0,0]
        position[0] = position[0]+x
        position[1] = position[1]+x 
        return position
    
summer = Bird()
print 'after move', summer.move(5, 6)