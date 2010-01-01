#!/usr/bin/env python

from pymud.server import Server
from pymud.persist import P
from pymud.room import Room
from pymud.mob import Mob
from pymud.item import Item
from pymud import builder

from mm.rooms import *
from mm.mobs import *
from mm.items import *
from mm.characters import *

roomMap = builder.buildRoomMapFile('maps/room')

class Game():

    def buildWorld(self):
        self.zone = builder.addZoneFromMapFile('zone','maps/map1',roomMap)


