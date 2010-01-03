
from pymud.exceptions import *
from pymud.util import *
import mm.mobs

def hi(self):
    self.sendMessage("notice",notice="Hi")

def checkSelf(self,target,message):
    if target == self: raise GameException(message)

def checkInstance(self,target,klass,message):
    if not isinstance(target,klass):
        raise GameException(message)

def smack(self,targetName):
    checkVoid(self,"You cannot find anything like " + targetName)
    target = getFirstTarget(self,targetName,'Who?')
    checkSelf(self,target,"What are you doing?")
    checkInstance(self,target,mm.mobs.Mob,"Cannot smack %s" % target.name)
    target.life += -1
    self.sendMessage("notice",notice="You smacked " + target.name)
    target.sendMessage("notice",notice="%s smacked you" % self.name)

commands = {
    'hi':hi,
    'smack':smack,
}

