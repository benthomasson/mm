
from pymud.rule import Rule, Pass, Fail, StopException, And, Condition, Action
from pymud.util import *

### Condition Factories

class AttributeEquals(Condition):
    
    def __init__(self,attribute,value):
        self.attribute = attribute
        self.value = value

    def __call__(self,rule,o):
        return getattr(o,self.attribute) == self.value

class AttributeLessThan(Condition):
    
    def __init__(self,attribute,value):
        self.attribute = attribute
        self.value = value

    def __call__(self,rule,o):
        return getattr(o,self.attribute) < self.value

class AttributeLessThanOrEqual(Condition):
    
    def __init__(self,attribute,value):
        self.attribute = attribute
        self.value = value

    def __call__(self,rule,o):
        return getattr(o,self.attribute) <= self.value

class AttributeGreaterThan(Condition):
    
    def __init__(self,attribute,value):
        self.attribute = attribute
        self.value = value

    def __call__(self,rule,o):
        return getattr(o,self.attribute) > self.value

class AttributeGreaterThanOrEqual(Condition):
    
    def __init__(self,attribute,value):
        self.attribute = attribute
        self.value = value

    def __call__(self,rule,o):
        return getattr(o,self.attribute) >= self.value

class HasAttribute(Condition):
    
    def __init__(self,attribute):
        self.attribute = attribute

    def __call__(self,rule,o):
        return hasattr(o,self.attribute)

### Action Factories

class IncreaseAttribute(Action):
    
    def __init__(self,attribute,amount):
        self.attribute = attribute
        self.amount = amount

    def __call__(self,rule,o,result):
        setattr(o,self.attribute,getattr(o,self.attribute) + self.amount)

class CreateInstanceInLocation(Action):
    
    def __init__(self,klass):
        self.klass = klass

    def __call__(self,rule,o,result):
        i = createInstance(self.klass)
        o.location().add(i)

class SendMessage(Action):
    
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self,rule,o,result):
        o.sendMessage(*self.args,**self.kwargs)

class SendLocationMessage(Action):
    
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self,rule,o,result):
        o.sendLocationMessage(*self.args,**self.kwargs)

class MutateKlass(Action):
    
    def __init__(self,klass):
        self.klass = klass

    def __call__(self,rule,o,result):
        o.__class__ = self.klass
        o.reschedule()
        ResetLifeTime(rule,o)

### Conditions

LifeZero = AttributeLessThanOrEqual('life',0)
LifetimeZero = AttributeLessThanOrEqual('lifetime',0)

### Actions

class Decay(Action):
    
    def __call__(self,rule,o,result):
        o.delete()
        raise StopException()

class Die(Action):
    
    def __call__(self,rule,o,result):
        o.sendMessage('notice',notice='You died')
        o.sendLocationMessage('notice',notice='%s died' % o.name,exclude=o)
        o.delete()
        raise StopException()

DecreaseLifetime = IncreaseAttribute('lifetime',-1)

class ResetLifeTime(Action):
    
    def __call__(self,rule,o,result):
        if o.__dict__.has_key('lifetime'):
            del o.lifetime
        if hasattr(o.__class__,'lifetime'):
            o.lifetime = o.__class__.lifetime


class MutateAction(ResetLifeTime):
    
    def __call__(self,rule,o,result):
        o.__class__ = o.nextClass
        o.reschedule()
        ResetLifeTime.__call__(self,rule,o,result)


class SpreadFire(ResetLifeTime):
    
    
    def __call__(self,rule,o,result):
        from mm.rooms import Flammable, Fire
        for exit in o.exits.values():
            if exit and isinstance(exit(),Flammable):
                exit().__class__ = Fire
                exit().reschedule()
                ResetLifeTime.__call__(self,rule,exit(),result)

### Rules

Death = Rule(And(HasAttribute('life'),LifeZero),Die())
Age = Rule(HasAttribute('lifetime'),DecreaseLifetime)
Mutate = Rule(And(HasAttribute('lifetime'),LifetimeZero),MutateAction())

Burn = Rule(Pass,SpreadFire())


### Rule Lists

mobRules = [ Death, Age, Mutate ]
mobChecks = [ Death, Age, Mutate ]

roomRules = [ Age, Mutate ]
roomChecks = [ Age, Mutate ]

