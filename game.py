#!/usr/bin/env python

from pymud.server import Server
from pymud.persist import P
from pymud.room import Room
from pymud.mob import Mob
from pymud.item import Item

class Game():

    def buildWorld(self):
        self.world = P.persist.getOrCreate("world",Room)
        self.home = P.persist.getOrCreate("home",Room)
        self.world.exits['home'] = P(self.home)
        self.home.exits['world'] = P(self.world)
        self.mob = P.persist.getOrCreate("mob",Mob)
        self.world.add(self.mob)
        self.thing = P.persist.getOrCreate("thing",Item)
        self.world.add(self.thing)
