from pyray import *
from config import *

class Event:

    def __init__(self, name, handler):
        self.name = name
        self.handler = handler
        self.invoked = False
        self.life_time = 0.0

    def invoke(self):
        self.invoked = True