import arcade

BULLET_WIDTH = 25
BULLET_HEIGHT = 5
FRIENDLY_BULLET_COLOR = arcade.color.YELLOW
ENEMY_BULLET_COLOR = arcade.color.RED

class BulletEntity:

    def __init__(self, x, y, x_vel, y_vel, owner, damage):
        self.center_x = x
        self.center_y = y
        self.change_x = x_vel
        self.change_y = y_vel
        self.damage = damage
        self.ownedbyplayer = owner

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        if self.ownedbyplayer:
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         BULLET_WIDTH,
                                         BULLET_HEIGHT,
                                         FRIENDLY_BULLET_COLOR)
        else:
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y,
                                         BULLET_WIDTH,
                                         BULLET_HEIGHT,
                                         ENEMY_BULLET_COLOR)