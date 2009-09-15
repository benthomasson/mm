
from pymud.room import Room


class Grass(Room):

    description = "tall green grass"
    detail = "green blades waving in the wind"

    def __init__(self,id=None):
        Room.__init__(self,id)



