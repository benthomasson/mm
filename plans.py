

from pymud.plan import Plan
from pymud.rule import Pass, SteppableRule
from mm.items import Apple
from mm.rules import createInstanceInLocation, sendMessage
from pymud.util import *

def buildInLocation(klass,turns):
    def _a(rule,o):
        for x in xrange(turns,0,-1):
            o.user.waiting = 'Building %s' % x
            yield
        o.user.waiting = None
        i = createInstance(klass)
        o.location().add(i)
        o.user.sendMessage('notice',notice="You've made an %s" % i.name)
    return _a

class MakeApple(Plan):

    rule = SteppableRule(Pass,buildInLocation(Apple,50))


