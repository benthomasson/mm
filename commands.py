
from pymud.exceptions import *
from pymud.util import *
import mm.mobs

def hi(self):
    self.sendMessage("notice",notice="Hi")

def smack(self,target):
    checkVoid(self,"You cannot find anything like " + target)
    target = getFirstTarget(self,target,'Who?')
    if target == self: raise GameException("What are you doing?")
    if not isinstance(target,mm.mobs.Mob): 
        raise GameException("Cannot smack %s" % target.name)
    target.life += -1
    self.sendMessage("notice",notice="You smacked " + target.name)
    target.sendMessage("notice",notice="%s smacked you" % self.name)

commands = {
    'hi':hi,
    'smack':smack,
}

