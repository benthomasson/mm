#!/usr/bin/env python

from pymud.server import Server
import pymud

from mm.game import Game
import mm.items
import mm.rooms

if __name__ == '__main__':


    server = Server()
    game = Game()

    server.start()
    game.buildWorld()
    server.run()
    server.close()

