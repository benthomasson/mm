#!/usr/bin/env python

import unittest
from pymud.server import Server, TestServer

from mm.game import Game


class Test(unittest.TestCase):

    def test(self):
        server = TestServer()
        game = Game()
        server.start()
        game.buildWorld()
        server.theCli.onecmd('goto 1')
        server.theCli.onecmd('map')
        self.assert_(game.zone)
        server.run(10)
        server.close()

if __name__ == '__main__':
    unittest.main()
