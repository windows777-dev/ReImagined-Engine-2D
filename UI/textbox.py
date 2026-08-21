import pyray as pr
from font_helper import *

class TextBox:
    def __init__(self, x=20, y=20, width=300, height=150, text="Enter text here...", font=FontHelper.GetFontPath("Fredoka-Semibold"), font_size=14, text_colour=pr.BLACK, highlighted_colour=pr.BLUE, text_highlighted_colour = pr.BLUE, background_colour=pr.WHITE, smoothness=0.1, border_size=5):
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