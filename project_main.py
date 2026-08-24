from pyray import *
from config import *
from UI.button import *
from UI.frame import *
from UI.font_helper import *
from UI.textbox import *
from UI.slider import *
from UI.text import *
from Utilities.timer import *
from Utilities.window_funcs import *
from Utilities.actor import *
from Tween.tweenhelper import *

set_config_flags(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE)
init_window(Configuration.WIDTH, Configuration.HEIGHT, Configuration.TITLE)
set_target_fps(120)



def draw():
    pass

def update():
    pass


while not window_should_close():
    Configuration.dt = get_frame_time()

    begin_drawing()

    draw()
    update()


    end_drawing()