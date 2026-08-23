import pyray as pr
from UI.font_helper import *

class Text:

    def __init__(self, x=20, y=20, text="TextLabel", font="Montserrat-ExtraBold.ttf", font_size=18, colour=pr.BLACK):
        self.text = text
        self.font = FontHelper.LoadFont(font)
        self.x=x
        self.y=y
        self.colour = colour
        pr.set_texture_filter(self.font.texture, pr.TextureFilter.TEXTURE_FILTER_POINT)
        self.font_size = font_size
    def draw(self):
        pr.draw_text_ex(self.font, self.text, pr.Vector2(self.x,self.y), self.font_size, 1.0, self.colour)