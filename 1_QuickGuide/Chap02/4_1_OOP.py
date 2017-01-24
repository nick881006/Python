class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_5th(self):
        for i in range(5):
            self.show_laugh()

nick = Human()          
nick.laugh_5th()