
from pymud.room import Room
from pymud.scriptable import Updatable
from pymud.exceptions import *


class Grass(Updatable,Room):

    ticksPerTurn = 1000
    description = "tall green grass"
    detail = "green blades waving in the wind"

    def __init__(self,id=None):
        Room.__init__(self,id)
        self.lifetime = 10

    def update(self,tick):
        self.lifetime += -1
        if self.lifetime <= 0:
            self.__class__ = Thorns
            self.mutate()


class Thorns(Updatable,Room):

    description = "tall impassible thorns"
    detail = "sharp spines upon tangled vines"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkHold(self,o):
        raise GameException("Thorns are impassible")

