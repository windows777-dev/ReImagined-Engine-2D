import pyray as pr
import os

class FontHelper:

    @staticmethod
    def GetFontPath(font_name):
        return os.path.join("assets", "fonts", font_name)

    @staticmethod
    def LoadFont(font_path):
        return pr.load_font_ex(os.path.join("assets", "fonts", font_path), 64, None, 0)
    