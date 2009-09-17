
from pymud.room import Room
from pymud.scriptable import Updatable, Mutable
from pymud.exceptions import *

class Flammable(object):
    pass

class Thorns(Updatable,Flammable,Room):

    description = "tall impassible thorns"
    detail = "sharp spines upon tangled vines"
    mapCharacter = "x"
    mapColor = "{GREEN}"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkEnter(self,o):
        raise GameException("Thorns are impassible")

class Grass(Mutable,Updatable,Flammable,Room):

    ticksPerTurn = 1000
    description = "tall green grass"
    detail = "green blades waving in the wind"
    mapCharacter = "."
    mapColor = "{LIGHTGREEN}"
    lifetime = 10
    nextClass = Thorns

    def __init__(self,id=None):
        Room.__init__(self,id)


class Ash(Mutable,Updatable,Room):

    ticksPerTurn = 1000
    description = "smouldering ash"
    detail = "embers and ashes of what once was"
    mapCharacter = "."
    mapColor = "{WHITE}"
    lifetime = 20
    nextClass = Grass

    def __init__(self,id=None):
        Room.__init__(self,id)

class Fire(Updatable,Mutable,Room):

    ticksPerTurn = 1000
    description = "tongues of flame"
    detail = "everything is a blaze"
    mapCharacter = "!"
    mapColor = "{RED}"
    lifetime = 3
    nextClass = Ash

    def __init__(self,id=None):
        Room.__init__(self,id)

    def update(self,tick):
        for exit in self.exits.values():
            if exit and isinstance(exit(),Flammable):
                exit().__class__ = Fire
                exit().mutate()
        Mutable.update(self,tick)

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

