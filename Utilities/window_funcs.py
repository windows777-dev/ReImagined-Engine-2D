import pyray as pr
import os

class WindowUtils:

    @staticmethod
    def GetBackground(fileName):
        return pr.load_texture(os.path.join("assets", "backgrounds", fileName))

    @staticmethod
    def SetBackground(bg):
        pr.draw_texture(bg, 0,0, pr.WHITE)

    def SetTitle(title):
        pr.set_window_title(title)
