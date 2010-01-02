

from pymud.mob import Mob as BaseMob
from pymud.chainedmap import ChainedMap
import mm.commands
from mm.rules import rules

class Mob(BaseMob):

    life = 2
    rules = ChainedMap(map=rules)

class Peon(Mob):

    commands = ChainedMap(map=mm.commands.commands,parent=Mob.commands)

    def __init__(self,id=None):
        Mob.__init__(self,id)

