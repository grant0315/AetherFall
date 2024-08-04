import pygame

import lib.entity as entity

class MoveableEntity(entity.Entity):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color, speed)
        
    def update(self):
        pass