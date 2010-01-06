
from pymud.rule import Rule, Pass, Fail, StopException, Action
from pymud.util import *

### Condition Factories

def notfn(fn):
    def _p(rule,o):
        return not fn(rule,o)
    return _p

def andfn(*fns):
    def _p(rule,o):
        for fn in fns:
            if not fn(rule,o):
                return False
        return True
    return _p

def orfn(*fns):
    def _p(rule,o):
        for fn in fns:
            if fn(rule,o):
                return True
        return False
    return _p

def attributeEquals(attribute,value):
    def _p(rule,o):
        return getattr(o,attribute) == value
    return _p

def attributeLessThan(attribute,value):
    def _p(rule,o):
        return getattr(o,attribute) < value
    return _p

def attributeLessThanOrEqual(attribute,value):
    def _p(rule,o):
        return getattr(o,attribute) <= value
    return _p

def attributeGreaterThan(attribute,value):
    def _p(rule,o):
        return getattr(o,attribute) > value
    return _p

def attributeGreaterThanOrEqual(attribute,value):
    def _p(rule,o):
        return getattr(o,attribute) >= value
    return _p

def hasAttribute(attribute):
    def _p(rule,o):
        return hasattr(o,attribute)
    return _p

### Action Factories

def progn(*fns):
    def _a(rule,o):
        last = None
        for fn in fns:
            last = fn(rule,o)
        return last
    return _a

def increaseAttribute(attribute,amount):
    def _a(rule,o):
        setattr(o,attribute,getattr(o,attribute) + amount)
    return _a

def createInstanceInLocation(klass):
    print klass
    def _a(rule,o):
        i = createInstance(klass)
        o.location().add(i)
    return _a

def sendMessage(*args,**kwargs):
    def _a(rule,o):
        o.sendMessage(*args,**kwargs)
    return _a

def sendLocationMessage(*args,**kwargs):
    def _a(rule,o):
        o.sendLocationMessage(*args,**kwargs)
    return _a

### Conditions

LifeZero = attributeLessThanOrEqual('life',0)
LifetimeZero = attributeLessThanOrEqual('lifetime',0)

### Actions

def Decay(rule,o):
    o.delete()
    raise StopException()

def Die(rule,o):
    o.sendMessage('notice',notice='You died')
    o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
    o.delete()
    raise StopException()

DecreaseLifetime = increaseAttribute('lifetime',-1)

def ResetLifeTime(rule,o):
    if o.__dict__.has_key('lifetime'):
        del o.lifetime
    if hasattr(o.__class__,'lifetime'):
        o.lifetime = o.__class__.lifetime


def MutateAction(rule,o):
    o.__class__ = o.nextClass
    o.reschedule()
    ResetLifeTime(rule,o)

def SpreadFire(rule,o):
    from mm.rooms import Flammable, Fire
    for exit in o.exits.values():
        if exit and isinstance(exit(),Flammable):
            exit().__class__ = Fire
            exit().reschedule()
            ResetLifeTime(rule,exit())



### Rules

Death = Rule(andfn(hasAttribute('life'),LifeZero),Die)
Age = Rule(hasAttribute('lifetime'),DecreaseLifetime)
Mutate = Rule(andfn(hasAttribute('lifetime'),LifetimeZero),MutateAction)

Burn = Rule(Pass,SpreadFire)


### Rule Lists

mobRules = [ Death, Age, Mutate ]
mobChecks = [ Death, Age, Mutate ]

roomRules = [ Age, Mutate ]
roomChecks = [ Age, Mutate ]

