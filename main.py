import arcade
from Entities import player, star, bullet, enemies, mainmenu
from Tools import patlib
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "SHMUP"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.menubuttonarray = []

        self.menubuttonarray.append(mainmenu.BaseButtonEntity(50, 300, "play", "BUTTON_START_GAME"))
        self.menubuttonarray.append(mainmenu.BaseButtonEntity(50, 265, "quit", "BUTTON_QUIT_GAME"))

        self.pausebuttonarray = []

        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 300, "resume", "BUTTON_RESUME_GAME"))
        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 265, "quit", "BUTTON_QUIT_GAME"))

        self.pausebg = mainmenu.PauseBG(500, 275, 150, 75)

        self.ply = player.PlayerEntity(100,250)
        self.mouse_x = 100
        self.mouse_y = 250

        self.showfps = False

        self.gamestate = "menu"
        self.time = 0
        self.deltatime = 0

        self.shooting = False
        self.canshoot = True
        self.shoottime = 0

        self.bulletarray = []
        self.enemyarray = []
        self.stararray = []
        self.menuenemyarray = []
        self.menustararray = []
        self.ply.godmode = False

        self.enemyselector = 0

        for i in range(128):
            self.menustararray.append(star.StarEntity(random.randint(0, 1000)))

        for i in range(64):
            self.stararray.append(star.StarEntity(random.randint(0, 1000)))

        for i in range(3):
            self.enemyarray.append(enemies.ChargerEnemy(1100, random.randint(-100, 700)))

        # If you have sprite lists, you should create them here,
        # and set them to None

    def retry(self):

        self.ply = player.PlayerEntity(100,250)

        self.gamestate = "playing"
        self.time = 1
        self.deltatime = 1

        self.shooting = False
        self.canshoot = True
        self.shoottime = 0

        self.bulletarray = []
        self.enemyarray = []
        self.stararray = []
        self.ply.godmode = False

        self.menuenemyang = 0

        self.enemyselector = 0

        for i in range(64):
            self.stararray.append(star.StarEntity(random.randint(0, 1000)))

        for i in range(3):
            self.enemyarray.append(enemies.ChargerEnemy(1100, random.randint(-100, 700)))

        # If you have sprite lists, you should create them here,
        # and set them to None


    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        self.clear()

        if self.showfps:
            arcade.draw_text("fps: "+str(round(1 / self.deltatime)),
                             890,
                             480,
                             arcade.color.RED,
                             10,
                             100,
                             align="right")

            arcade.draw_text("enemies: "+str(len(self.enemyarray)),
                             890,
                             455,
                             arcade.color.RED,
                             10,
                             100,
                             align="right")

            arcade.draw_text("bullets: "+str(len(self.bulletarray)),
                             890,
                             430,
                             arcade.color.RED,
                             10,
                             100,
                             align="right")
            arcade.draw_text("stars: "+str(len(self.stararray)),
                             890,
                             405,
                             arcade.color.RED,
                             10,
                             100,
                             align="right")

        if self.gamestate == "menu":

            for s in self.menustararray:
                s.draw()

            for e in self.menuenemyarray:
                e.draw()

            for b in self.menubuttonarray:
                b.draw()

            #title text here
            arcade.draw_text("PLACEHOLDER TITLE",
                             35,
                             350,
                             arcade.color.WHITE,
                             50,
                             1000,
                             align="left")

        if self.gamestate == "playing" or self.gamestate == "lose" or self.gamestate == "pause":

            for s in self.stararray:
                s.draw()

            self.ply.draw()

            for b in self.bulletarray:
                b.draw()

            for e in self.enemyarray:
                e.draw()

            if self.gamestate == "playing" or self.gamestate == "pause":
                arcade.draw_text(str(self.ply.score),
                                 10,
                                 460,
                                 arcade.color.RED,
                                 30,
                                 100,
                                 align="left")

            if self.gamestate == "lose":
                arcade.draw_text("You died",
                                 0,
                                 250,
                                 arcade.color.RED,
                                 30,
                                 1000,
                                 align="center")

                arcade.draw_text("press r to reset",
                                 0,
                                 225,
                                 arcade.color.RED,
                                 15,
                                 1000,
                                 align="center")

                arcade.draw_text("escape to go to main menu",
                                 0,
                                 200,
                                 arcade.color.RED,
                                 15,
                                 1000,
                                 align="center")

                arcade.draw_text("score: " + str(self.ply.score),
                                 0,
                                 175,
                                 arcade.color.RED,
                                 15,
                                 1000,
                                 align="center")

            if self.gamestate == "pause":
                self.pausebg.draw()
                for b in self.pausebuttonarray:
                    b.draw()

    def on_update(self, delta_time):

        self.time += delta_time
        self.deltatime = delta_time

        if self.gamestate == "menu":

            if 0 < self.time*1000 % random.randint(1,2) < 1:
                self.menustararray.append(star.StarEntity(1100))

            for s in self.menustararray:
                s.update(0, 0)
                if s.center_x < -100 or s.center_x > 1100 or s.center_y > 600 or s.center_y < -100:
                    self.menustararray.remove(s)

            if 0 < self.time*100 % random.randint(1,500) < 1 and random.randint(1,10) > 7:
                for i in range(3):
                    self.menuenemyang = random.uniform(-60,60)
                    self.menuenemyarray.append(enemies.DummyEnemy(random.randint(200, 600), random.randint(-90, -20), self.menuenemyang, 3, 0)) #x, y, ang, col, speed, turnspeed

            for e in self.menuenemyarray:
                e.update()

        if self.gamestate == "playing" or self.gamestate == "lose":

            if self.gamestate == "playing":
                self.ply.update(self.mouse_x, self.mouse_y)

            if self.gamestate == "lose":
                self.shooting = False

            if self.shooting and self.canshoot and self.time > self.shoottime:
                self.bulletarray.append(bullet.BulletEntity(self.ply.center_x, self.ply.center_y, 25, 0, True, 1))
                self.shoottime = self.time + 0.1

            for b in self.bulletarray:
                b.update()
                if patlib.distToPoint(b.center_x, b.center_y, self.ply.center_x, self.ply.center_y) < 40 and not self.ply.godmode and not b.ownedbyplayer:
                    self.ply.health -= b.damage
                    if self.ply.health < 0:
                        self.ply.health = 0
                    self.bulletarray.remove(b)
                if b.center_x > 1100 or b.center_x < -100 or b.center_y > 600 or b.center_y < -100:
                    self.bulletarray.remove(b)

            for e in self.enemyarray:

                e.update(self.ply.center_x, self.ply.center_y, self.time)

                for b in self.bulletarray:
                    if patlib.distToPoint(e.center_x, e.center_y, b.center_x, b.center_y) < 25 and b.ownedbyplayer:
                        if not e.invincible:
                            e.health -= b.damage
                            if e.health <= 0:
                                self.ply.score += e.scorevalue
                                self.enemyarray.remove(e)
                                break
                            if not self.ply.piercing:
                                self.bulletarray.remove(b)
                        else:
                            self.bulletarray.remove(b)

                if patlib.distToPoint(e.center_x, e.center_y, self.ply.center_x, self.ply.center_y) < 40 and not self.ply.godmode:
                    self.ply.health -= e.meleedamage
                    if self.ply.health < 0:
                        self.ply.health = 0
                    self.enemyarray.remove(e)
                    break

                if e.__class__ == enemies.ShooterEnemy:
                    if e.shoottime < self.time and len(self.bulletarray) < 30:
                        e.shoottime = self.time + 1
                        self.bulletarray.append(bullet.BulletEntity(e.center_x, e.center_y, -10, 0, False, 10))

                if not -200 < e.center_x < 1200 or not -200 < e.center_y < 700:
                    self.enemyarray.remove(e)
                    break


            for s in self.stararray:
                s.update(self.ply.change_x, self.ply.change_y)
                if s.center_x < -100 or s.center_x > 1100 or s.center_y > 600 or s.center_y < -100 or s.change_x < 0:
                    self.stararray.remove(s)


            if 0 < self.time*1000 % random.randint(1,2) < 1:
                self.stararray.append(star.StarEntity(1100))

            if 0 < self.time*1000 % random.randint(10,20) < 1 and len(self.enemyarray) < 20:
                self.enemyselector = random.randint(1,100)
                if 0 < self.enemyselector < 70 :
                    self.enemyarray.append(enemies.ChargerEnemy(1100, random.randint(0, 600)))
                if 70 < self.enemyselector < 90 :
                    self.enemyarray.append(enemies.ShooterEnemy(1100, random.randint(0, 600)))
                if 90 < self.enemyselector < 100 :
                    self.enemyarray.append(enemies.AsteroidEnemy(1100, random.randint(0, 600)))


            if self.ply.health <= 0:
                self.gamestate = "lose"

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.R:
            self.retry()
        if key == arcade.key.F6:
            if not self.showfps:
                self.showfps = True
            else:
                self.showfps = False

        if key == arcade.key.ESCAPE:
            if self.gamestate == "pause":
                self.gamestate = "playing"
            elif self.gamestate == "playing":
                self.gamestate = "pause"
            elif self.gamestate == "lose":
                self.retry()
                self.gamestate = "menu"

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.gamestate == "playing":
            self.shooting = True
        if self.gamestate == "menu":
            for b in self.menubuttonarray:
                if b.center_x - mainmenu.BUTTON_LENGTH / 2 < x < b.center_x + mainmenu.BUTTON_LENGTH / 2 and \
                    b.center_y - mainmenu.BUTTON_WIDTH / 2 < y < b.center_y + mainmenu.BUTTON_WIDTH / 2:

                    if b.id == "BUTTON_START_GAME":
                        self.gamestate = "playing"

                    if b.id == "BUTTON_QUIT_GAME":
                        arcade.exit()
        if self.gamestate == "pause":
            for b in self.pausebuttonarray:
                if b.center_x - mainmenu.BUTTON_LENGTH / 2 < x < b.center_x + mainmenu.BUTTON_LENGTH / 2 and \
                    b.center_y - mainmenu.BUTTON_WIDTH / 2 < y < b.center_y + mainmenu.BUTTON_WIDTH / 2:

                    if b.id == "BUTTON_RESUME_GAME":
                        self.gamestate = "playing"

                    if b.id == "BUTTON_QUIT_GAME":
                        arcade.exit()

    def on_mouse_release(self, x, y, button, key_modifiers):
        self.shooting = False


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
