
from pymud.scriptable import Updatable
from pymud.item import Item

class Apple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a delicious red apple"
    attributes = ['red','delicious']
    name = 'apple'

    def update(self,tick):
        self.__class__ = RottenApple
        self.mutate()
        self.sendLocationMessage("notice",
            notice="The apple looks rotten at %d" % tick)

class RottenApple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a wormy rotten apple"
    attributes = ['wormy','rotten']
    name = 'apple'

    def update(self,tick):
        self.delete()
        self.sendLocationMessage("notice",
            notice="The worms have completely eaten the apple at %d" % tick)
        

        

