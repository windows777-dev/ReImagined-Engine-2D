import pyray as pr
from EventManager.eventmanager import *

class Game:
    WIDTH = pr.get_monitor_width(1)
    HEIGHT = pr.get_monitor_height(1)
    TITLE = "Test"
    mode = "main_menu"

    gravity = 500

    dt = 0
    event_mgr = EventManager()

    solid_objects = []
    