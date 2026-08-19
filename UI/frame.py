import pyray as pr

class Frame:

    def __init__(self, x=20, y=20, width=500, height=500, color=pr.WHITE, smoothness=0.1, border_size=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.smoothness = smoothness
        self.border_size = border_size

        self.rect = pr.Rectangle(x, y, width, height)

    def draw(self):
        pr.draw_rectangle_rounded(self.rect, self.smoothness, 4, self.color)
        pr.draw_rectangle_rounded_lines_ex(self.rect, self.smoothness, 4, self.border_size, pr.BLACK)