from pyray import *
from UI.font_helper import *


class Listbox:

    def __init__(self, x=20, y=20, width=500, height=700, corner_radius=0.1, border_radius=5, font=F"Montserrat-ExtraBold.ttf", font_size=24, pady=10, element_height=50, bg_colour=Color(255,255,255,255), element_colour=Color(58,58,58,255), hover_colour=Color(62, 108, 249, 255), element_text_colour = Color(255,255,255,255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.corner_radius=corner_radius
        self.border_radius = border_radius
        self.font = FontHelper.LoadFont(font)
        self.font_size = font_size
        self.pady = pady

        self.element_height = element_height
        self.element_colour = element_colour
        self.bg_colour = bg_colour
        self.element_text_colour = element_text_colour

        self.hover_colour = hover_colour


        self.selected_element = None

        self.elements = []
        self._elements = []
        self.offset_y = 0 

        self.element_hovered_index = None
        self.element_hovered = None
        

        
    def add_element(self, text):
        

        index = len(self.elements)

        internal_element = {
            "x" : self.x + 10,
            "y" : self.y + (self.element_height + 10) * index,
            "width" : self.width - 20,
            "height" : self.element_height,
            "text" : text
        }

        self.elements.append(text)
        self._elements.append(internal_element)

    def check_element_hovered(self):
        pos = get_mouse_position()
        self.element_hovered = False
        self.element_hovered_index = False
        for i, element in enumerate(self._elements):
            if check_collision_point_rec(pos, Rectangle(element["x"], element["y"] + self.offset_y, element["width"], element["height"])):
                self.element_hovered_index = i
                self.element_hovered = element
                break

    def update(self):
        if check_collision_point_rec(get_mouse_position(), Rectangle(self.x, self.y, self.width, self.height)):
            self.offset_y -= int(get_mouse_wheel_move() * 7)
        
    def draw(self):
        self.update()
        self.check_element_hovered()

        draw_rectangle_rounded(Rectangle(self.x, self.y, self.width, self.height), self.corner_radius, 4, self.bg_colour)
        draw_rectangle_rounded_lines_ex(Rectangle(self.x, self.y, self.width, self.height), self.corner_radius, 4, self.border_radius, BLACK)

        begin_scissor_mode(int(self.x), int(self.y), int(self.width), int(self.height))

        for element in self._elements:
            if element == self.element_hovered:
                draw_rectangle_rounded(Rectangle(element["x"], element["y"] + self.offset_y, element["width"], element["height"]), self.corner_radius, 4, self.hover_colour)
            else:
                draw_rectangle_rounded(Rectangle(element["x"], element["y"] + self.offset_y, element["width"], element["height"]), self.corner_radius, 4, self.element_colour)

            draw_rectangle_rounded_lines_ex(Rectangle(element["x"], element["y"] + self.offset_y, element["width"], element["height"]), self.corner_radius, 4, self.border_radius, BLACK)

            t_w = pr.measure_text(element["text"], self.font_size)
            t_h = self.font_size

            text_x = int(element["x"] + (element["width"] - t_w) / 2)
            text_y = int((element["y"] + self.offset_y) + (element["height"] - t_h) / 2)


            draw_text_ex(self.font, element["text"], Vector2(text_x, text_y), self.font_size, 1.0, self.element_text_colour)
            
        end_scissor_mode()
