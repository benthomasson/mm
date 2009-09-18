
from pymud.mob import Mob
from pymud.chainedmap import ChainedMap

class TestGoblin(Mob):
    
    commands = ChainedMap( parent=Mob.commands, 
                            map = { } )
    scripts = ChainedMap( parent=Mob.scripts, 
                            map = {
'wander': """\
trigger failure do wander
loop {
    wander
    wait 100
}
""",
'random':"""\
trigger failure do random
loop {
random {
get thing
drop thing
look
map
wander
go east
go west
go north
go south
}
wait 10
}
""",
                                } )
    triggers = ChainedMap( parent=Mob.triggers, 
                            map = { 
                                'enter':'map',
                                } )

    description = "a green goblin"
    detail = "a nasty tricky little goblin"
    attributes = []
    name = 'goblin'
    slotNames = ['head','hand']
