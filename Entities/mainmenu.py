import random
import arcade
from Tools import patlib

BUTTON_WIDTH = 25
BUTTON_LENGTH = 25
BUTTON_BORDER_WIDTH = 3
BUTTON_SPEED = 25
BUTTON_COLOR = arcade.color.RED
BUTTON_BORDER_COLOR = arcade.color.WHITE


class BaseButtonEntity:

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     BUTTON_WIDTH,
                                     BUTTON_LENGTH,
                                     BUTTON_BORDER_COLOR)

        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     BUTTON_WIDTH - BUTTON_BORDER_WIDTH,
                                     BUTTON_LENGTH - BUTTON_BORDER_WIDTH,
                                     BUTTON_COLOR)
        arcade.draw_text("test",
                         self.center_x - BUTTON_WIDTH * 2,
                         self.center_y,
                         arcade.color.PURPLE,
                         10,
                         100,
                         align="center")
