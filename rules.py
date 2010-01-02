
from pymud.rule import Rule, Pass, Fail, StopException, Action

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

LifeZero = attributeLessThanOrEqual('life',0)

def Delete(self,o):
    o.sendMessage('notice',notice='You died')
    o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
    o.delete()
    raise StopException()

Death = Rule(LifeZero,Delete)

rules = [ Death ]

