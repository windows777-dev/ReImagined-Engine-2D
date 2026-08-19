import pyray as pr
import os

class Actor:

    def __init__(self, image, inx=0, iny=0):
        super(Actor, self)
        self.surf = pr.load_texture(os.path.join("assets", "sprites", image+".png"))

        self.rect = pr.Rectangle(inx, iny, self.surf.width, self.surf.height)

        self.xvec = 0
        self.yvec = 0 

        @property
        def width(self):
            return self.rect.width

        @property
        def height(self):
            return self.rect.height


    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y
    def set_x(self, x):
        self.rect.x = x
    def set_y(self, y):
        self.rect.y = y

    def get_left(self):
        return self.rect.x
    def set_left(self, x):
        self.rect.x = x
    def get_right(self):
        return self.rect.x + self.rect.width
    def set_right(self, right):
        self.rect.x = right - self.rect.width
    def get_top(self):
        return self.rect.y
    def set_top(self, top):
        self.rect.y = top
    def get_bottom(self):
        return self.rect.y + self.rect.height
    def set_bottom(self, y):
        self.rect.y = y + (self.rect.height)
        
    def get_centerx(self):
        return self.rect.x + (self.rect.width / 2)
    def set_centerx(self, x):
        self.rect.x = x - (self.rect.width / 2)
    def get_centery(self):
        return self.rect.y + (self.rect.height / 2)
    def set_centery(self, y):
        self.rect.y = y - (self.rect.height / 2)

    left = property(fget=get_left, fset=set_left)
    right = property(fget=get_right, fset=set_right)
    top = property(fget=get_top, fset=set_top)
    bottom = property(fget=get_bottom, fset=set_bottom)
    centrex = property(fget=get_centerx, fset=set_centerx)
    centrey = property(fget=get_centery, fset=set_centery)
        
        
        

    x = property(fget=get_x, fset=set_x)
    y = property(fget=get_y, fset=set_y)

    def draw(self):
        pr.draw_texture(self.surf, int(self.x), int(self.y), pr.WHITE)
        