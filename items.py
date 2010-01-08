
from pymud.scriptable import Updatable
from pymud.item import Item, FixedItem
from pymud.admin import mutate
from mm.rules import Pass, Rule, createInstanceInLocation, progn,\
    sendLocationMessage, MutateAction, Decay

Disappear = Rule(Pass,progn(sendLocationMessage("notice",
            notice="The worms have completely eaten the apple."), Decay))

class RottenApple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a wormy rotten apple"
    attributes = ['wormy','rotten']
    name = 'apple'
    rules = [ Disappear ]

Rot = Rule(Pass,progn(MutateAction,sendLocationMessage("notice",notice="The apple looks rotten")))

class Apple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a delicious red apple"
    attributes = ['red','delicious']
    nextClass = RottenApple
    name = 'apple'
    rules = [ Rot ]

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

    from mm.rooms import Flammable
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

DropApple = Rule(Pass, progn(createInstanceInLocation(Apple),
              sendLocationMessage("notice",notice="An apple dropped from the tree.")))

class AppleTree(Updatable,FixedItem):

    ticksPerTurn = 1000
    description = "a grand tree"
    detail = "tree filled with red apples"
    name = "tree"
    rules = [ DropApple ]


class FireWood(Item):

    description = "fire wood"
    name = "wood"
    detail = "dense punky wood"


