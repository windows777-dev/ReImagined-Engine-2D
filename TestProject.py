from pyray import *
from config import *
from UI.button import *
from UI.frame import *
from UI.font_helper import *
from Utilities.timer import *
from Utilities.window_funcs import *
from Utilities.actor import *

init_window(Configuration.WIDTH, Configuration.HEIGHT, Configuration.TITLE)
set_target_fps(120)
toggle_fullscreen()

icon = load_image("ElixrFC_Icon.png")
set_window_icon(icon)

bg = WindowUtils.GetBackground("yes.png")


test_frame = Frame(x=(get_screen_width() - 500) / 2, y=(get_screen_height() - 500) / 2)
test_button = Button(x=test_frame.x + (test_frame.width - 300) / 2, y=test_frame.y + 50, animation_growth_size=1, font_size=36, font_path=FontHelper.GetFontPath("Fredoka-SemiBold.ttf"), text="Play")
test_actor = Actor("aaron-wilder", 500, 500)

fredoka = FontHelper.LoadFont("Fredoka-SemiBold.ttf")

def draw():
    WindowUtils.SetBackground(bg)
    test_frame.draw()
    test_button.draw()
    test_actor.draw()

def update():
    pass


while not window_should_close():
    Configuration.dt = get_frame_time()

    begin_drawing()

    draw()
    update()


    end_drawing()
    
close_window()