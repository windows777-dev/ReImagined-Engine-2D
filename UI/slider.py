import pyray as pr

class Slider:

    def __init__(self, x=20, y=20, width=300, height=50, slider_colour=pr.WHITE, background_colour = pr.WHITE, slider_point_radius = 30.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.slider_colour = slider_colour
        self.background_colour = background_colour
        self.dragging = False
        self.slider_point_radius = slider_point_radius

        self.slider_x = self.x # Not an offset
        self.value = 0

        if self.value != 0:
            self.value = (self.slider_x / self.width) * 100

    def is_dragging(self):
        return pr.check_collision_point_circle(pr.get_mouse_position(), pr.Vector2(self.slider_x, self.y), self.slider_point_radius) and pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT)
    def update(self):
        self.dragging = self.is_dragging()

        if self.dragging:
            self.slider_x = max(self.x, min(pr.get_mouse_x(), self.x + self.width))
            self.value = ((self.slider_x - self.x) / self.width) * 100

    def draw(self):
        self.update()

        pr.draw_rectangle_rounded(pr.Rectangle(self.x, self.y, self.width, self.height), 1,  4, self.background_colour)
        pr.draw_rectangle_rounded_lines_ex(pr.Rectangle(self.x, self.y, self.width, self.height), 1, 4, 5, pr.BLACK)

        pr.draw_circle(int(self.slider_x), int(self.y + self.slider_point_radius - 3), self.slider_point_radius + 10, pr.BLACK)
        pr.draw_circle(int(self.slider_x), int(self.y + self.slider_point_radius - 3), self.slider_point_radius, self.slider_colour)
        

        print(self.value)