
from pymud.rule import Rule, Pass, Fail, StopException, Action

def notfn(fn):
    def _p(self,o):
        return not fn(self,o)
    return _p

def andfn(*fns):
    def _p(self,o):
        for fn in fns:
            if not fn(self,o):
                return False
        return True
    return _p

def orfn(*fns):
    def _p(self,o):
        for fn in fns:
            if fn(self,o):
                return True
        return False
    return _p

def attributeEquals(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) == value
    return _p

def attributeLessThan(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) < value
    return _p

def attributeLessThanOrEqual(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) <= value
    return _p

def attributeGreaterThan(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) > value
    return _p

def attributeGreaterThanOrEqual(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) >= value
    return _p

def hasAttribute(attribute):
    def _p(self,o):
        return hasattr(o,attribute)
    return _p

def increaseAttribute(attribute,amount):
    def _a(self,o):
        setattr(o,attribute,getattr(o,attribute) + amount)
    return _a

### Conditions

LifeZero = attributeLessThanOrEqual('life',0)
LifetimeZero = attributeLessThanOrEqual('lifetime',0)

### Actions

def Delete(self,o):
    o.sendMessage('notice',notice='You died')
    o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
    o.delete()
    raise StopException()

DecreaseLifetime = increaseAttribute('lifetime',-1)

def MutateAction(self,o):
    o.__class__ = o.nextClass
    o.mutate()

def SpreadFire(self,o):
    from mm.rooms import Flammable, Fire
    for exit in o.exits.values():
        if exit and isinstance(exit(),Flammable):
            exit().__class__ = Fire
            exit().mutate()



### Rules

Death = Rule(andfn(hasAttribute('life'),LifeZero),Delete)
Age = Rule(hasAttribute('lifetime'),DecreaseLifetime)
Mutate = Rule(andfn(hasAttribute('lifetime'),LifetimeZero),MutateAction)

Burn = Rule(Pass,SpreadFire)

mobRules = [ Death, Age, Mutate ]

roomRules = [ Age, Mutate ]

