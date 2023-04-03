import random
import arcade

POWERUP_WIDTH = 30
POWERUP_BORDER_WIDTH = 5
POWERUP_HEALTH_COLOR = arcade.color.GREEN
POWERUP_HEALTH_CROSS_WIDTH = 25
POWERUP_HEALTH_CROSS_HEIGHT = 5
POWERUP_HEALTH_BORDER_COLOR = arcade.color.WHITE

POWERUP_GODMODE_COLOR = arcade.color.GOLD

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

    def draw(self):
        if self.powerup == "POWERUP_HEALTH":
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_WIDTH,
                                         POWERUP_WIDTH,
                                         POWERUP_HEALTH_BORDER_COLOR
                                      )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_WIDTH - POWERUP_BORDER_WIDTH,
                                         POWERUP_WIDTH - POWERUP_BORDER_WIDTH,
                                         POWERUP_HEALTH_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_HEALTH_CROSS_WIDTH,
                                         POWERUP_HEALTH_CROSS_HEIGHT,
                                         POWERUP_HEALTH_BORDER_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_HEALTH_CROSS_HEIGHT,
                                         POWERUP_HEALTH_CROSS_WIDTH,
                                         POWERUP_HEALTH_BORDER_COLOR
                                         )
        if self.powerup == "POWERUP_GODMODE":
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_WIDTH,
                                         POWERUP_WIDTH,
                                         POWERUP_GODMODE_COLOR
                                      )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_WIDTH - POWERUP_BORDER_WIDTH,
                                         POWERUP_WIDTH - POWERUP_BORDER_WIDTH,
                                         POWERUP_GODMODE_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_HEALTH_CROSS_WIDTH,
                                         POWERUP_HEALTH_CROSS_HEIGHT,
                                         POWERUP_GODMODE_COLOR
                                         )
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_HEALTH_CROSS_HEIGHT,
                                         POWERUP_HEALTH_CROSS_WIDTH,
                                         POWERUP_GODMODE_COLOR
                                         )

        if self.powerup == "POWERUP_TRIPLESHOT":
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         POWERUP_WIDTH,
                                         POWERUP_WIDTH,
                                         POWERUP_HEALTH_BORDER_COLOR
                                      )


