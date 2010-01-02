
from pymud.rule import Rule, Pass, Fail, StopException, Action

def attributeEquals(attribute,value):
    def _p(self,o):
        return getattr(o,attribute) == value
    return _p

LifeZero = attributeEquals('life',0)

def Delete(self,o):
    o.sendMessage('notice',notice='You died')
    o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
    o.delete()
    raise StopException()

Death = Rule(LifeZero,Delete)

rules = {
    '0_Death': Death,
}
