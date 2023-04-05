import arcade
import main
from Tools import patlib as pl

BUTTON_WIDTH = 25
BUTTON_LENGTH = 100
BUTTON_BORDER_WIDTH = 3
BUTTON_SPEED = 25
BUTTON_COLOR = arcade.color.BLACK_OLIVE
BUTTON_BORDER_COLOR = arcade.color.WHITE

class BaseButtonEntity:

    def __init__(self, x, y, text, ID, alignment):
        self.center_x = x
        self.center_y = y
        self.text = text
        self.id = ID
        self.alignment = alignment

    def draw(self,fs):
        """arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     BUTTON_LENGTH,
                                     BUTTON_WIDTH,
                                     BUTTON_BORDER_COLOR)"""

        """arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     BUTTON_LENGTH - BUTTON_BORDER_WIDTH,
                                     BUTTON_WIDTH - BUTTON_BORDER_WIDTH,
                                     BUTTON_COLOR)"""
        arcade.draw_text(self.text,
                         (self.center_x - 50) * pl.gfssf(fs,main.SCREEN_WIDTH),
                         (self.center_y - 4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                         arcade.color.WHITE,
                         10 * pl.gfssf(fs,main.SCREEN_WIDTH),
                         100 * pl.gfssf(fs,main.SCREEN_WIDTH),
                         self.alignment)

class PauseBG:
    def __init__(self, x, y, x_scale, y_scale):
        self.center_x = x
        self.center_y = y
        self.size_x = x_scale
        self.size_y = y_scale

    def draw(self,fs):
        arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     self.size_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     self.size_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     BUTTON_BORDER_COLOR)

        arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     (self.size_x - BUTTON_BORDER_WIDTH) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     (self.size_y - BUTTON_BORDER_WIDTH) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                     BUTTON_COLOR)