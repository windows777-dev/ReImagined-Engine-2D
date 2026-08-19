import pyray as pr
from config import *

class Timer:

    def __init__(self, length):
        self.length = length
        self.current = 0.0
    def tick(self):
        self.current += Configuration.dt
        if (self.current >= self.length):
            return True
        else:
            return False