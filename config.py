import pyray as pr

class Configuration:
    WIDTH = pr.get_monitor_width(1)
    HEIGHT = pr.get_monitor_height(1)
    TITLE = "Wallahis left: 1"
    mode = "main_menu"

    gravity = 500

    dt = 0

    solid_objects = []
    