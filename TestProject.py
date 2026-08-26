from pyray import *
from config import *
from UI.button import *
from UI.frame import *
from UI.font_helper import *
from UI.textbox import *
from UI.slider import *
from UI.text import *
from UI.listbox import *
from Utilities.timer import *
from Utilities.window_funcs import *
from Utilities.actor import *
from EventManager.event import *
from EventManager.eventmanager import *
from Tween.tweenhelper import *

set_config_flags(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE)
init_window(Configuration.WIDTH, Configuration.HEIGHT, Configuration.TITLE)
set_target_fps(120)


icon = load_image("ElixrFC_Icon.png")
set_window_icon(icon)


bg = WindowUtils.GetBackground("yes.png")

event_mgr = EventManager()


test_frame = Frame(x=(get_screen_width() - 500) / 2, y=(get_screen_height() - 500) / 2)
test_button = Button(x=test_frame.x + (test_frame.width - 300) / 2, y=test_frame.y + 50, animation_growth_size=1, font_size=36, font_path=FontHelper.GetFontPath("Fredoka-SemiBold.ttf"), text="Play", command=lambda: draw_text("Pressed!", 200, 200, 36, RED))
test_actor = Actor("aaron-wilder", 500, 500)
test_tb = TextBox(x=500, y=500)

test_text = Text(x=500, y=500, text="TestText", font_size=72)

test_slider = Slider(x=500, y=500)

fredoka = FontHelper.LoadFont("Fredoka-SemiBold.ttf")

actor_tween = Tween(tween_type=TweenType.LINEAR, position=Vector2(test_actor.x, test_actor.y), final_position=Vector2(700, 700), speed=1.0)

test_event = Event(name="te")
test_listbox = Listbox()
test_listbox.add_element("test")
test_listbox.add_element("test2")

event_mgr.register_event(test_event)

def draw():
    clear_background(GRAY)
    
    #test_frame.draw()
    #test_button.draw()
    
    #actor_tween.update()
    test_actor.x = actor_tween.position.x
    test_actor.y = actor_tween.position.y

    test_listbox.draw()

    #test_actor.draw()
    #test_slider.draw()
    #test_tb.draw()
    #test_text.draw()

def update():

    if 2 == 2:
        test_event.invoke()

    event_mgr.update()
    

    if event_mgr.invoked("te"):
        print("Invoked!")


    

    

while not window_should_close():
    Configuration.dt = get_frame_time()

    begin_drawing()

    draw()
    update()


    end_drawing()
    
close_window()