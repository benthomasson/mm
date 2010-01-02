
from pymud.util import *

def hi(self):
    self.sendMessage("notice",notice="Hi")

def smack(self,target):
    checkVoid(self,"You cannot find anything like " + target)
    target = getFirstTarget(self,target,'Who?')
    target.life += -1
    self.sendMessage("notice",notice="You smacked " + target.name)
    target.sendMessage("notice",notice="%s smacked you" % self.name)

commands = {
    'hi':hi,
    'smack':smack,
}

