
from pymud.room import Room
from pymud.scriptable import Updatable, Mutable
from pymud.exceptions import *


class Grass(Mutable,Updatable,Room):

    ticksPerTurn = 1000
    description = "tall green grass"
    detail = "green blades waving in the wind"
    mapCharacter = "."
    mapColor = "{LIGHTGREEN}"
    lifetime = 1000

    def __init__(self,id=None):
        Room.__init__(self,id)

class Thorns(Updatable,Room):

    description = "tall impassible thorns"
    detail = "sharp spines upon tangled vines"
    mapCharacter = "x"
    mapColor = "{GREEN}"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkEnter(self,o):
        raise GameException("Thorns are impassible")

Grass.nextClass = Thorns

class Mountains(Updatable,Room):

    description = "tall impassible mountains"
    detail = "sheer craggy cliffs"
    mapCharacter = "^"
    mapColor = "{WHITE}"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkEnter(self,o):
        raise GameException("Mountains are impassible")

roomMap = {
    '.':Grass,
    'x':Thorns,
    '^':Mountains,
}

