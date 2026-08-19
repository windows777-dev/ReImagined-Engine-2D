import pyray as pr
import os

class Button:

    def __init__(self, x=50, y=50, width=300, height=150, color=pr.BLUE, hover_colour=pr.DARKBLUE, smoothness=0.1, border_size=5, font_path="test/path", font_size=14, text="Test", text_colour=pr.BLACK, animation_growth_size=5, command=lambda: print("Hello World!")):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.smoothness = smoothness
        self.border_size = border_size
        self.font_path = font_path
        self.font_size = font_size
        self.animation_growth_size = animation_growth_size
        self.text = text
        self.command = command
        self.text_colour = text_colour
        self.hover_colour = hover_colour

        self.width_grown = width + (5 * animation_growth_size)
        self.height_grown = height + (5 * animation_growth_size)

        self._width = width
        self._height = height

        self._colour = color

        if not os.path.exists(font_path):
            print("ReImagined Engine: [DEBUG]: Font path is invalid or doesn't exist!")
        
        self._font = pr.load_font(font_path)
        

        self.rect = pr.Rectangle(x, y, width, height) # Dont expect this to move around but us programmers are weird, hence we update it in the render function

    def _update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

    def is_hovered(self):
        return pr.check_collision_point_rec(pr.get_mouse_position(), self.rect)
    def is_clicked(self):
        return self.is_hovered() and pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT)


    def draw(self):
        self._update_rect()

        t_w = pr.measure_text(self.text, self.font_size)
        t_h = self.font_size

        text_x = int(self.x + (self.width - t_w) / 2)
        text_y = int(self.y + (self.height - t_h) / 2)

        pr.draw_rectangle_rounded(self.rect, self.smoothness, 4, self.color)
        pr.draw_rectangle_rounded_lines_ex(self.rect, self.smoothness, 4, self.border_size, pr.BLACK)
        pr.draw_text_ex(self._font, self.text, pr.Vector2(text_x, text_y), self.font_size, 1.0, self.text_colour)

        if self.is_hovered():
            self.color = self.hover_colour
            self.width = self.width_grown
            self.height = self.height_grown
        else:
            self.color = self._colour
            self.width = self._width
            self.height = self._height
            

        if self.is_clicked():
            self.command()
            self.color = self._colour
            self.width = self._width
            self.height = self._height

    def set_size(self, w, h):
        self._width = w
        self._height = h
        self.width = w
        self.height = h
