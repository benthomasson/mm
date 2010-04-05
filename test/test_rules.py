
from pymud.rule import *
from mm.rules import *

import py

class Struct(object): pass

def test_pass():
    assert Pass(None,None)

def test_fail():
    assert not Fail(None,None)

def test_null_action():
    assert not NullAction(None,None,None)

def test_and():
    assert And(Pass,Pass)(None,None)

def test_rule():
    assert not Rule(Pass,NullAction)(None)

def test_lifezero():
    o = Struct()
    o.life = 0
    assert LifeZero(None,o)
    o.life = 1
    assert not LifeZero(None,o)


class MockSim(object):

    def __init__(self):
        self.deleted = False
        self.name = 'mock'

    def delete(self):
        self.deleted = True

    def sendMessage(self,*args,**kwargs):
        pass

    def sendLocationMessage(self,*args,**kwargs):
        pass

def test_delete():
    o = MockSim()
    o.life = 0
    o.delete()
    assert o.deleted

def test_death():
    o = MockSim()
    o.life = 0
    assert HasAttribute('life')(None,o)
    assert LifeZero(None,o)
    py.test.raises(StopException,Death,o)
    assert o.deleted

def test_age():
    o = MockSim()
    o.lifetime = 10
    assert HasAttribute('lifetime')(None,o)
    Age(o)
    assert o.lifetime == 9


def test_mob_rules():
    o = MockSim()
    o.lifetime = 10
    o.life = 10
    runRules(o,mobRules)
    assert not o.deleted 
    assert o.lifetime == 9

def test_room_rules():
    o = MockSim()
    o.lifetime = 10
    o.life = 10
    runRules(o,roomRules)
    assert not o.deleted 
    assert o.lifetime == 9


