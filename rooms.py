

from pymud.room import Room as BaseRoom
from pymud.scriptable import Updatable
from pymud.exceptions import *
from mm.rules import roomRules

class Flammable(object):
    pass

class Room(BaseRoom):

    rules = roomRules

class Thorns(Updatable,Flammable,Room):

    description = "tall impassible thorns"
    detail = "sharp spines upon tangled vines"
    mapCharacter = "x"
    mapColor = "{GREEN}"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkEnter(self,o):
        raise GameException("Thorns are impassible")

class TallGrass(Updatable,Flammable,Room):

    ticksPerTurn = 1000
    description = "tall green grass"
    detail = "green blades waving in the wind"
    mapCharacter = "/"
    mapColor = "{LIGHTGREEN}"
    lifetime = 50
    nextClass = Thorns

    def __init__(self,id=None):
        Room.__init__(self,id)

class Grass(Updatable,Room):

    ticksPerTurn = 1000
    description = "green grass"
    detail = "soft green carpet of grass"
    mapCharacter = "."
    mapColor = "{LIGHTGREEN}"
    lifetime = 10
    nextClass = TallGrass

    def __init__(self,id=None):
        Room.__init__(self,id)


class Ash(Updatable,Room):

    ticksPerTurn = 1000
    description = "smouldering ash"
    detail = "embers and ashes of what once was"
    mapCharacter = "."
    mapColor = "{WHITE}"
    lifetime = 20
    nextClass = Grass

    def __init__(self,id=None):
        Room.__init__(self,id)

class Fire(Updatable,Room):

    ticksPerTurn = 1000
    description = "tongues of flame"
    detail = "everything is a blaze"
    mapCharacter = "!"
    mapColor = "{RED}"
    lifetime = 3
    nextClass = Ash

    def __init__(self,id=None):
        Room.__init__(self,id)

class Mountains(Room):

    description = "tall impassible mountains"
    detail = "sheer craggy cliffs"
    mapCharacter = "^"
    mapColor = "{WHITE}"

    def __init__(self,id=None):
        Room.__init__(self,id)

    def checkEnter(self,o):
        raise GameException("Mountains are impassible")

