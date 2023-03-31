import random
import arcade
import math
from Tools import patlib

ENEMY_WIDTH = 25
ENEMY_SPEED = 25
ENEMY_COLOR = arcade.color.RED
ENEMY_BORDER_COLOR = arcade.color.WHITE

SHOOTER_ENEMY_COLOR = arcade.color.BLUE
SHOOTER_ENEMY_BORDER_COLOR = arcade.color.WHITE

ASTEROID_ENEMY_COLOR = arcade.color.BROWN


class BaseEnemyEntity:

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.health = random.randint(1,3)
        self.scorevalue = 100
        self.meleedamage = 10
        self.invincible = False

    def update(self, ply_x, ply_y,time):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.center_x,
                                     self.center_y,
                                     ENEMY_WIDTH,
                                     ENEMY_BORDER_COLOR,
                                     270,
                                     self.health + 2
                                  )
        arcade.draw_circle_filled(self.center_x,
                                  self.center_y,
                                  ENEMY_WIDTH-5,
                                  ENEMY_COLOR,
                                  270,
                                  self.health + 2
                                  )

class DummyEnemy(BaseEnemyEntity):

    def __init__(self, x, y, ang, speed, turnspeed):
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.ang = ang
        self.speed = speed
        self.change_angle = turnspeed
        self.sides = random.randint(3,5)

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.ang)

        # Use math to find our change based on our speed and angle
        self.center_x += self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

        # Rotate the ship
        self.ang += self.change_angle

    def draw(self):
        arcade.draw_circle_filled(self.center_x,
                                     self.center_y,
                                     ENEMY_WIDTH,
                                     ENEMY_BORDER_COLOR,
                                     self.ang,
                                     self.sides
                                  )
        arcade.draw_circle_filled(self.center_x,
                                  self.center_y,
                                  ENEMY_WIDTH-5,
                                  ENEMY_COLOR,
                                  self.ang,
                                  self.sides
                                  )

class ChargerEnemy(BaseEnemyEntity):

    def update(self, ply_x, ply_y,time):
        self.change_x = (ply_x - self.center_x) / patlib.distToPoint(self.center_x, self.center_y, ply_x, ply_y) * 5
        self.change_y = (ply_y - self.center_y) / patlib.distToPoint(self.center_x, self.center_y, ply_x, ply_y) * 5

        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.center_x,
                                     self.center_y,
                                     ENEMY_WIDTH,
                                     ENEMY_BORDER_COLOR,
                                     270,
                                     self.health + 2
                                  )
        arcade.draw_circle_filled(self.center_x,
                                  self.center_y,
                                  ENEMY_WIDTH-5,
                                  ENEMY_COLOR,
                                  270,
                                  self.health + 2
                                  )

class ShooterEnemy(BaseEnemyEntity):

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.health = 1
        self.scorevalue = 50
        self.meleedamage = 0
        self.invincible = False

        self.shoottime = 0

    def update(self, ply_x, ply_y,time):
        self.change_x = -0.1 * (self.center_x - 800)
        self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.center_x,
                                      self.center_y,
                                      ENEMY_WIDTH,
                                      SHOOTER_ENEMY_BORDER_COLOR,
                                      270,
                                      self.health + 2
                                  )
        arcade.draw_circle_filled(self.center_x,
                                      self.center_y,
                                      ENEMY_WIDTH-5,
                                      SHOOTER_ENEMY_COLOR,
                                      270,
                                      self.health + 2
                                  )

class AsteroidEnemy(BaseEnemyEntity):

    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.change_x = random.randint(-10,-3)
        self.change_y = random.randint(-3,3)
        self.health = 1
        self.scorevalue = 1000000000
        self.meleedamage = 100
        self.invincible = True
        self.rotation = 0

    def update(self, ply_x, ply_y,time):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.rotation += (self.change_x + self.change_y) / 5

    def draw(self):
        arcade.draw_circle_filled(self.center_x,
                                     self.center_y,
                                     ENEMY_WIDTH,
                                     ASTEROID_ENEMY_COLOR,
                                     self.rotation,
                                     6
                                  )