
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

class smack(object):

    def __init__(s,self,targetName):
        #check self
        checkVoid(self,"You cannot find anything like " + targetName)
        #get target(s)
        target = getFirstTarget(self,targetName,'Who?')
        #check target(s)
        checkSelf(self,target,"What are you doing?")
        checkInstance(self,target,mm.mobs.Mob,"Cannot smack %s" % target.name)
        #calculate effects
        #apply effects
        target.life += -1
        #send messages
        self.sendMessage("notice",notice="You smacked " + target.name)
        target.sendMessage("notice",notice="%s smacked you" % self.name)

def harvest(self):
    l = self.location()
    if hasattr(l,'harvestChoices') and hasattr(l,'harvestAmount'):
        if l.harvestAmount <= 0:
            raise GameException('There is nothing left to harvest')
        klass = l.harvestChoices.next()
        i = createInstance(klass)
        self.add(i)
        l.harvestAmount += -1
        if l.harvestAmount <= 0:
            l.runChecks()
        self.sendMessage("notice",notice="You harvested a %s" % i.name)
    else:
        raise GameException('Cannot harvest from %s' % l.name)


commands = {
    'hi':hi,
    'smack':smack,
    'harvest':harvest,
}

