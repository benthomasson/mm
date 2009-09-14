
from pymud.scriptable import Updatable
from pymud.item import Item
from pymud.persist import P
from pymud.scheduler import Scheduler


class Apple(Updatable,Item):

    ticksPerTurn = 5000
    description = "a delicious red apple"
    attributes = {'name':'apple'}

    def update(self,tick):
        self.__class__ = RottenApple
        Scheduler.scheduler.schedule(self)

class RottenApple(Updatable,Item):

    ticksPerTurn = 1000
    description = "a wormy rotten apple"
    attributes = {'name':'apple'}

    def update(self,tick):
        P.persist.delete(self)
        

