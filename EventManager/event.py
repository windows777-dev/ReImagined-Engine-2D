from pyray import *
from config import *

class Event:

    def __init__(self, name):
        self.name = name
        self.invoked = False
        self.life_time = 0.0
        self.data = {}
        

    def invoke(self, **kwargs):
        self.invoked = True
        self.data = kwargs