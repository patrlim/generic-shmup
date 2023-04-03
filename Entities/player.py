import arcade

RECT_WIDTH = 15
RECT_COLOR = arcade.color.GREEN
HEALTH_COLOR = arcade.color.GREEN
HEALTH_BORDER_COLOR = arcade.color.WHITE
HEALTH_WIDTH = 100
HEALTH_HEIGHT = 10
HEALTH_BORDER = 2


class PlayerEntity:

    def __init__(self,x ,y):

        # Set up attribute variables

        # Where we are
        self.center_x = x
        self.center_y = y
        self.change_y = 0
        self.health = 100
        self.piercing = False
        self.score = 0
        self.godmode = False
        self.godmodeexpiretime = 0

    def update(self, mouse_x, mouse_y, time):
        # Move the rectangle
        self.change_y = -0.1 * (self.center_y - mouse_y)
        self.change_x = -0.1 * (self.center_x - mouse_x)
        self.center_y += self.change_y
        self.center_x += self.change_x

        if time > self.godmodeexpiretime:
            self.godmode = False

    def draw(self):
        # Draw the rectangle
        if self.godmode:
            arcade.draw_circle_filled(self.center_x,
                                      self.center_y,
                                      RECT_WIDTH,
                                      arcade.color.WHITE,
                                      90,
                                      3
                                      )
        else:
            arcade.draw_circle_filled(self.center_x,
                                      self.center_y,
                                      RECT_WIDTH,
                                      RECT_COLOR,
                                      90,
                                      3
                                      )

        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y + 25,
                                     HEALTH_WIDTH,
                                     HEALTH_HEIGHT,
                                     HEALTH_BORDER_COLOR)

        arcade.draw_rectangle_filled(self.center_x + ((HEALTH_WIDTH - HEALTH_BORDER) * self.health/200) - (HEALTH_WIDTH - HEALTH_BORDER)/2,
                                     self.center_y + 25,
                                     (HEALTH_WIDTH - HEALTH_BORDER) * (self.health/100),
                                     (HEALTH_HEIGHT - HEALTH_BORDER),
                                     HEALTH_COLOR)
