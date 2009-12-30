#!/usr/bin/env python

import unittest
from pymud.server import Server

from mm.game import Game


class Test(unittest.TestCase):

    def test(self):
        server = Server()
        game = Game()
        server.start()
        game.buildWorld()
        self.assertEquals(game.mob.location(),game.world)
        self.assertEquals(game.thing.location(),game.world)
        server.close()

if __name__ == '__main__':
    unittest.main()
