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
                        self.position += (self.final_position - self.position) * self.speed * Configuration.dt

            case TweenType.EXPONENTIAL:
                  distance = self.final_position - self.position

                  self.position += distance * self.speed * Configuration.dt
        
        

        

        