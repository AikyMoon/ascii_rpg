from __future__ import annotations
from enum import Enum, auto


class Entities(Enum):
    Player = auto
    Enemy = auto
    Wall = auto
    Finish = auto


class GameObject:
    def __init__(self, x: int, y: int, entity_type: Entities) -> None:
        self.x = x
        self.y = y
        self.entity_type = entity_type



class Player(GameObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, Entities.Player)
    

    
