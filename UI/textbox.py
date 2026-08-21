import pyray as pr
from UI.font_helper import *

class TextBox:
    def __init__(self, x=20, y=20, width=300, height=150, text="Enter text here...", font=FontHelper.GetFontPath("Fredoka-Semibold.ttf"), font_size=24, text_colour=pr.BLACK, highlighted_colour=pr.BLUE, text_highlighted_colour = pr.BLUE, background_colour=pr.WHITE, smoothness=0.1, border_size=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font = font
        self.text_colour = text_colour
        self.text_highlighted_colour = text_highlighted_colour
        self.highlighted_colour = highlighted_colour
        self.background_colour = background_colour
        self.smoothness = smoothness
        self.border_size = border_size
        self.activated = False
        self._font = pr.load_font(font)
        self._internal_text = ""
    def get_text(self):
        return self._internal_text # Only do this because I dont trust accessing the variable directly
    def clear_text(self):
        self._internal_text = ""

    def is_hover(self):
        return pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(self.x, self.y, self.width, self.height))
    def is_click(self):
        return self.is_hover() and pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT)

    def update(self):

        if self.is_click():
            self.activated = True
        if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT) and not self.is_hover():
            self.activated = False
            self.clear_text()

        if (self.activated):
            key = pr.get_key_pressed()

            if key > 0:

                if key == pr.KEY_BACKSPACE:
                    self._internal_text = self._internal_text[:-1]
                elif key == pr.KEY_SPACE:
                    self._internal_text += " "
                else:
                    key_name = pr.get_key_name(key)
                    self._internal_text += key_name
                

    def draw(self):
        self.update()
        
        pr.draw_rectangle_rounded(pr.Rectangle(self.x, self.y, self.width, self.height), self.smoothness, 4, self.background_colour)

        max_width = self.width - (self.border_size + 4)

        display_text = self._internal_text
        while pr.measure_text_ex(self._font, display_text, self.font_size, 1).x > max_width and len(display_text) > 0:
            display_text = display_text[1:]

            

        if (self.activated):
            pr.draw_rectangle_rounded_lines_ex(pr.Rectangle(self.x, self.y, self.width, self.height), self.smoothness, 4, self.border_size, self.highlighted_colour)
            pr.draw_text_ex(self._font, display_text, pr.Vector2(self.x + 10, self.y + 10), self.font_size, 1.0, self.text_colour)

            text_x = self.x + pr.measure_text_ex(self._font, display_text, self.font_size, 1).x
            text_y = self.y


            pr.draw_line(int(text_x + 15), int(text_y + 7), int(text_x + 15), int(text_y + 40), pr.BLACK)

        else:
            pr.draw_rectangle_rounded_lines_ex(pr.Rectangle(self.x, self.y, self.width, self.height), self.smoothness, 4, self.border_size, pr.BLACK)
            pr.draw_text_ex(self._font, self.text, pr.Vector2(self.x + 10, self.y + 10), self.font_size, 1.0, pr.Color(36, 36, 36, 100))