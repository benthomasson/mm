
from pymud.scriptable import Updatable
from pymud.item import Item
from pymud.admin import mutate

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
        

class Hat(Item):

    description = "a felt hat"
    detail = "a black felt hat"
    name = "hat"
    fitsInSlots = ['head']

def burn(self):
    """\
    Light a fire.

    burn
    """

    mutate(self,'here','Fire')
    self.sendMessage("notice",notice="You torch the place")
        
class Torch(Item):

    description = "a lit torch"
    detail = "the fiery light dispells darkness"
    name = "torch"
    fitsInSlots = ['hand']
    commands = { 'burn': burn }

        
        
