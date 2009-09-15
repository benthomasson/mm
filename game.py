#!/usr/bin/env python

from pymud.server import Server
from pymud.persist import P
from pymud.room import Room
from pymud.mob import Mob
from pymud.item import Item
from pymud import builder

from mm.rooms import *
from mm.items import *

class Game():

    def buildWorld(self):
        self.world = builder.getOrCreate(Room,"world")
        self.home = builder.getOrCreate(Grass,"home")
        builder.addExit(self.world,'home',self.home)
        builder.addExit(self.home,'world',self.world)
        self.mob = builder.getOrCreate(Mob,"mob",self.world)
        self.thing = builder.getOrCreate(Item,"thing",self.world)
        self.apple = builder.getOrCreate(Apple,"apple",self.world)


