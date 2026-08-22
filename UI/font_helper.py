import pyray as pr
import os

class FontHelper:

    @staticmethod
    def GetFontPath(font_name):
        return os.path.join("assets", "fonts", font_name)

    @staticmethod
    def LoadFont(font_path):
        font = pr.load_font_ex(os.path.join("assets", "fonts", font_path), 64, None, 0)
        pr.set_texture_filter(font.texture, pr.TextureFilter.TEXTURE_FILTER_POINT)
        return font
    