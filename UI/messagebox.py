from pyray import *
from UI.font_helper import *
from UI.button import *
from enum import Enum

class MessageBoxButtons(Enum):
    OK = 1
    OK_CANCEL = 2
    YES_NO = 3
    OK_CANCEL_ABORT = 4


class MessageBox:
    def hide(self):
     self.visible = False

    def __init__(self, x=20, y=20, width=600, height=500, title="Test", message="Hello World!", draggable=True, font="Montserrat-Extrabold.ttf", font_size=28, background_colour=Color(255,255,255,255), foreground_colour=(0,0,0,255), border_radius=0.1, border_size=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.message=message
        self.draggable = draggable
        self.font = FontHelper.LoadFont(font)
        self.font_size = font_size
        self.bg_colour = background_colour
        self.fg_colour = foreground_colour
        self.border_radius = border_radius
        self.border_size = border_size
        self.dragging = True
        self.line_spacing = self.font_size + 4
        self.visible = True
        self._button = Button(x=self.x + (self.width - 300) / 2, y=self.y + self.height - 170, text="Ok", color=GREEN, hover_colour=DARKGREEN, animation_growth_size=1, command=self.hide, font_path=FontHelper.GetFontPath("Montserrat-ExtraBold.ttf"), height=100, font_size=28)

    def is_dragging(self):
        self.dragging = check_collision_point_rec(get_mouse_position(), Rectangle(self.x, self.y, self.width, self.height - 150)) and is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)

    def update_window_position(self):
        if self.dragging:
            self.x = get_mouse_x() - (self.width / 2)
            self.y = get_mouse_y() - 20

    def update(self):
        self.is_dragging()
        self.update_window_position()
        self._button.x = self.x + (self.width - 300) / 2
        self._button.y = self.y + self.height - 120

    def draw(self):

        if self.visible:
            self.update()

            draw_rectangle_rounded(Rectangle(self.x, self.y, self.width, self.height), self.border_radius, 4, self.bg_colour)
            draw_rectangle_rounded_lines_ex(Rectangle(self.x, self.y, self.width, self.height), self.border_radius, 4, self.border_size, BLACK)


            ti_w = measure_text(self.title, self.font_size)

            text_x = int(self.x + (self.width - ti_w) / 2)
            text_y = int(self.y + 10)

            draw_text_ex(self.font, self.title, Vector2(text_x, text_y), self.font_size, 1.0, self.fg_colour)

            max_width = self.width - 40  # Left 20px + Right 20px padding
            lines = []
            current_line = ""

            for word in self.message.split(' '):
                test_line = f"{current_line} {word}".strip()
                
                # Check if this test line fits inside your max width
                if measure_text(test_line, self.font_size) <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)



            for i, line in enumerate(lines):
                draw_text_ex(self.font, line, Vector2(self.x + 20, self.y + 20 + self.font_size + (i * self.line_spacing)), self.font_size, 1.0, self.fg_colour)

            self._button.draw()


        