import random
import arcade
import main
from Tools import patlib as pl

POWERUP_WIDTH = 30
POWERUP_BORDER_WIDTH = 5
POWERUP_HEALTH_COLOR = arcade.color.GREEN
POWERUP_HEALTH_CROSS_WIDTH = 25
POWERUP_HEALTH_CROSS_HEIGHT = 5
POWERUP_HEALTH_BORDER_COLOR = arcade.color.WHITE

POWERUP_GODMODE_COLOR = arcade.color.GOLD

POWERUP_TRIPLESHOT_COLOR = arcade.color.GOLD
POWERUP_TRIPLESHOT_ACCENT_COLOR = arcade.color.GOLDEN_BROWN
POWERUP_TRIPLESHOT_GAP = 15

class PowerupEntity:

    def __init__(self, x, y, x_vel, y_vel, powerup, time):
        self.center_x = x
        self.center_y = y
        self.change_x = x_vel - 3
        self.change_y = y_vel
        self.powerup = powerup
        self.powerupexpirytime = time

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self, fs):
        if self.powerup == "POWERUP_HEALTH":
            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_BORDER_COLOR
                                      )
            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH - POWERUP_BORDER_WIDTH) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH - POWERUP_BORDER_WIDTH) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_CROSS_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_CROSS_HEIGHT * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_BORDER_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_CROSS_HEIGHT * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_CROSS_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_HEALTH_BORDER_COLOR
                                         )
        if self.powerup == "POWERUP_GODMODE":
            arcade.draw_parabola_filled((self.center_x - POWERUP_WIDTH/2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (self.center_x + POWERUP_WIDTH/2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (POWERUP_WIDTH*2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_GODMODE_COLOR,
                                         180
                                      )

        if self.powerup == "POWERUP_TRIPLESHOT":
            arcade.draw_parabola_filled((self.center_x - POWERUP_WIDTH / 8) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (self.center_x + POWERUP_WIDTH / 8) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (POWERUP_WIDTH / 2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        POWERUP_TRIPLESHOT_COLOR,
                                        0
                                      )
            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH/4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_COLOR
                                         )

            arcade.draw_rectangle_filled(self.center_x * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (self.center_y-10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH/4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH/10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_ACCENT_COLOR
                                         )
            arcade.draw_parabola_filled((self.center_x - POWERUP_WIDTH / 8 + POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (self.center_x + POWERUP_WIDTH / 8 + POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (POWERUP_WIDTH / 2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        POWERUP_TRIPLESHOT_COLOR,
                                        0
                                        )
            arcade.draw_rectangle_filled((self.center_x + POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_COLOR
                                         )

            arcade.draw_rectangle_filled((self.center_x + POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (self.center_y - 10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_ACCENT_COLOR
                                         )
            arcade.draw_parabola_filled((self.center_x - POWERUP_WIDTH / 8 - POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (self.center_x + POWERUP_WIDTH / 8 - POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        (POWERUP_WIDTH / 2) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                        POWERUP_TRIPLESHOT_COLOR,
                                        0
                                        )
            arcade.draw_rectangle_filled((self.center_x - POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         self.center_y * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_WIDTH * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_COLOR
                                         )

            arcade.draw_rectangle_filled((self.center_x - POWERUP_TRIPLESHOT_GAP) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (self.center_y - 10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 4) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         (POWERUP_WIDTH / 10) * pl.gfssf(fs,main.SCREEN_WIDTH),
                                         POWERUP_TRIPLESHOT_ACCENT_COLOR
                                         )

