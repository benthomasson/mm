

from pymud.room import Room as BaseRoom
from pymud.scriptable import Updatable
from pymud.exceptions import *
from mm.rules import roomRules, Burn

class Flammable(object):
    pass

class Room(BaseRoom):

    rules = roomRules

class Forest(Flammable,Room):

    description = "dark haunting woods"
    detail = "trees mostly"
    mapCharacter = "+"
    mapColor = "{GREEN}"

class Thorns(Updatable,Flammable,Room):

    ticksPerTurn = 1000
    description = "tall impassible thorns"
    detail = "sharp spines upon tangled vines"
    mapCharacter = "x"
    mapColor = "{GREEN}"
    lifetime = 50
    nextClass = Forest

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

class Grass(Updatable,Room):

    ticksPerTurn = 1000
    description = "green grass"
    detail = "soft green carpet of grass"
    mapCharacter = "."
    mapColor = "{LIGHTGREEN}"
    lifetime = 10
    nextClass = TallGrass

class Ash(Updatable,Room):

    ticksPerTurn = 1000
    description = "smouldering ash"
    detail = "embers and ashes of what once was"
    mapCharacter = "."
    mapColor = "{WHITE}"
    lifetime = 20
    nextClass = Grass

class Fire(Updatable,Room):

    ticksPerTurn = 1000
    description = "tongues of flame"
    detail = "everything is a blaze"
    mapCharacter = "!"
    mapColor = "{RED}"
    lifetime = 3
    nextClass = Ash
    rules = roomRules + [ Burn ]

class Mountains(Room):

    description = "tall impassible mountains"
    detail = "sheer craggy cliffs"
    mapCharacter = "^"
    mapColor = "{WHITE}"

    def checkEnter(self,o):
        raise GameException("Mountains are impassible")

