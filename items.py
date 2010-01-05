
from pymud.scriptable import Updatable
from pymud.item import Item, FixedItem
from pymud.admin import mutate
from mm.rooms import Flammable
from mm.rules import Pass, Rule, createInstanceInLocation

class Apple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a delicious red apple"
    attributes = ['red','delicious']
    name = 'apple'

    def update(self,tick):
        self.__class__ = RottenApple
        self.reschedule()
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

    if isinstance(self.location(),Flammable):
        mutate(self,'here','Fire')
        self.sendMessage("notice",notice="You torch the place")
    else:
        self.sendMessage("notice",notice="Your torch is ineffective")

        
class Torch(Item):

    description = "a lit torch"
    detail = "the fiery light dispells darkness"
    name = "torch"
    fitsInSlots = ['hand']
    commands = { 'burn': burn }

    def __call__(self,user):
        burn(user)

class AppleTree(Updatable,FixedItem):

    ticksPerTurn = 1000
    description = "a grand tree"
    detail = "tree filled with red apples"
    name = "tree"
    rules = [ Rule(Pass,createInstanceInLocation(Apple)) ]

