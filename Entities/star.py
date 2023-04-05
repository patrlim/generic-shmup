import random
import arcade
import main
from Tools import patlib as pl

STAR_COLOR = arcade.color.WHITE

class StarEntity:

    def __init__(self, x):
        self.center_x = x
        self.center_y = random.randint(1,600)
        self.depth = random.uniform(0.6,3)
        self.change_x = self.depth * 10 - 5
        self.width = self.depth + random.uniform(-0.5,0.5)
        self.scalef = 1

    def update(self, ply_x_vel, ply_y_vel):
        self.center_x -= self.change_x + (ply_x_vel * self.depth) / 10
        self.center_y -= (ply_y_vel * self.depth) / 10

    def draw(self,fs):
        arcade.draw_circle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                  self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                  self.width * pl.gfssf(fs,main.SCREEN_WIDTH),
                                  STAR_COLOR,
                                  0,
                                  16
                                  )