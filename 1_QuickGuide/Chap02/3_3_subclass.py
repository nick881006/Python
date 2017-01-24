class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self,x,y):
        position=[0,0]
        position[0] = position[0]+x
        position[1] = position[1]+x 
        return position

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_kfc = True
    
class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_kfc = False
    
summer = Chicken()
print summer.have_feather
print summer.move(5,8)