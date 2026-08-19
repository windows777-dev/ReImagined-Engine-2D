import pyray as pr
from enum import Enum
from config import *

class TweenType(Enum):
    LINEAR = 1
    EXPONENTIAL = 2
    ELASTIC = 3
    CUBIC = 4
    EASE_IN = 5
    EASE_OUT = 6
    EASE_INOUT = 7

class Tween:

    def __init__(self, tween_type, position, final_position, speed):
        self.tween_type = tween_type
        self.position = position
        self.final_position = final_position
        self.speed = speed

    def update(self):

        match self.tween_type:
            case TweenType.LINEAR:
                if self.position < self.final_position:
                        self.position.x += (self.final_position.x - self.position.x) * self.speed * Configuration.dt
                        self.position.y += (self.final_position.y - self.position.y) * self.speed * Configuration.dt

            case TweenType.EXPONENTIAL:
                dx = self.final_position.x - self.position.x
                dy = self.final_position.y - self.position.y

                self.position.x += dx * self.speed * Configuration.dt
                self.position.y += dy * self.speed * Configuration.dt
        
        

        

        