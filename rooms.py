

from pymud.room import Room as BaseRoom
from pymud.scriptable import Updatable
from pymud.exceptions import *
from pymud.choices import weighted_choices
from pymud.rule import Rule
from mm.rules import roomRules, Burn, mutateKlass, attributeLessThan
from mm.items import FireWood

class Flammable(object):
    pass

class Room(BaseRoom):

    rules = roomRules

class LoggedForest(Updatable,Room):

    ticksPerTurn = 1000
    description = "stumps"
    detail = "stumps and broom straw"
    mapCharacter = "_"
    mapColor = "{LIGHTBLACK}"
    lifetime = 50
    nextClass = None

class Forest(Flammable,Room):

    description = "dark haunting woods"
    detail = "trees mostly"
    mapCharacter = "+"
    mapColor = "{GREEN}"
    harvestChoices = weighted_choices({FireWood:1})
    harvestAmount = 10
    checks = [ Rule(attributeLessThan('harvestAmount',1),
                    mutateKlass(LoggedForest)) ]

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

LoggedForest.nextClass = Grass

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

