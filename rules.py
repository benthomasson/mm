
from pymud.rule import Rule, Pass, Fail, StopException, Action

def LifeZero(self,o):
    return o.life == 0

def Delete(self,o):
    o.sendMessage('notice',notice='You died')
    o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
    return o.delete()

Death = Rule(LifeZero,Delete)

rules = {
    '0_Death': Death
}
