import time

import arcade
from Entities import player, star, bullet, enemies, mainmenu, powerups
from Tools import patlib
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "SHMUP"

POWERUP_CHANCE = 10

POWERUP_GODMODE_WEIGHT = 5
POWERUP_HEALTH_WEIGHT = 100
POWERUP_TRIPPLESHOT_WEIGHT = 30

POWERUP_TOTAL_WEIGHT = 100

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.shootsound = arcade.Sound('sounds/shoot.wav')
        self.shootsoundspeed = 1
        self.enemyshootsound = arcade.Sound('sounds/enemyshoot.wav')
        self.enemyshootsoundspeed = 1
        self.powerupsound = arcade.Sound('sounds/powerup.wav')
        self.powerupsoundspeed = 1
        self.plydeathsound = arcade.Sound('sounds/playerdeath.wav')
        self.plydeathsoundspeed = 1
        self.deathsoundplayed = False
        self.buttonclicksound = arcade.Sound('sounds/click.wav')
        self.buttonclicksoundspeed = 1

        self.menuenemyang = 0

        self.menubuttonarray = []

        self.menubuttonarray.append(mainmenu.BaseButtonEntity(50, 300, "play", "BUTTON_START_GAME"))
        self.menubuttonarray.append(mainmenu.BaseButtonEntity(50, 265, "quit", "BUTTON_QUIT_GAME"))

        self.pausebuttonarray = []

        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 335, "resume", "BUTTON_RESUME_GAME"))
        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 265, "main menu", "BUTTON_GOTO_MENU"))
        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 230, "quit to desktop", "BUTTON_QUIT_GAME"))
        self.pausebuttonarray.append(mainmenu.BaseButtonEntity(500, 300, "retry", "BUTTON_RESET_GAME"))

        self.deathbuttonarray = []

        self.deathbuttonarray.append(mainmenu.BaseButtonEntity(500, 175, "main menu", "BUTTON_GOTO_MENU"))
        self.deathbuttonarray.append(mainmenu.BaseButtonEntity(500, 150, "quit to desktop", "BUTTON_QUIT_GAME"))
        self.deathbuttonarray.append(mainmenu.BaseButtonEntity(500, 200, "retry", "BUTTON_RESET_GAME"))

        self.pausebg = mainmenu.PauseBG(500, 280, 150, 140)
        self.deathbg = mainmenu.PauseBG(500, 215, 300, 180)

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
        self.poweruparray = []
        self.stararray = []
        self.menuenemyarray = []
        self.menustararray = []
        self.ply.godmode = False
        self.ply.trippleshot = False

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
        self.deathsoundplayed = False

        self.shooting = False
        self.canshoot = True
        self.shoottime = 0

        self.bulletarray = []
        self.enemyarray = []
        self.poweruparray = []
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

            # title text here
            arcade.draw_text("Space Flight Dog Fight",
                             35,
                             350,
                             arcade.color.WHITE,
                             50,
                             1000,
                             align="left"
                             )

        if self.gamestate == "playing" or self.gamestate == "lose" or self.gamestate == "pause":

            for s in self.stararray:
                s.draw()

            if self.gamestate != "lose":
                self.ply.draw()

            for b in self.bulletarray:
                b.draw()

            for p in self.poweruparray:
                p.draw()

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

                self.deathbg.draw()

                arcade.draw_text("You died",
                                 0,
                                 250,
                                 arcade.color.WHITE,
                                 30,
                                 1000,
                                 align="center")

                arcade.draw_text("score: " + str(self.ply.score),
                                 0,
                                 225,
                                 arcade.color.WHITE,
                                 15,
                                 1000,
                                 align="center")

                for b in self.deathbuttonarray:
                    b.draw()

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
                    self.menuenemyarray.append(enemies.DummyEnemy(random.randint(200, 600), random.randint(-90, -20), self.menuenemyang, 3, 0))

            for e in self.menuenemyarray:
                e.update()

        if self.gamestate == "playing" or self.gamestate == "lose":

            if self.gamestate == "playing":
                self.ply.update(self.mouse_x, self.mouse_y,self.time)

            if self.gamestate == "lose":
                self.shooting = False

            if self.shooting and self.canshoot and self.time > self.shoottime:
                self.bulletarray.append(bullet.BulletEntity(self.ply.center_x, self.ply.center_y, 25, 0, True, 1))

                if self.ply.trippleshot:
                    self.bulletarray.append(bullet.BulletEntity(self.ply.center_x, self.ply.center_y+15, 25, 0, True, 1))
                    self.bulletarray.append(bullet.BulletEntity(self.ply.center_x, self.ply.center_y-15, 25, 0, True, 1))

                self.shoottime = self.time + 0.1
                self.shootsound.play(self.shootsoundspeed,0)

            self.updateBullets()
            self.updateEnemies()
            self.updatePowerups()

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
                if not self.deathsoundplayed:
                    self.plydeathsound.play(self.plydeathsoundspeed,0)
                    self.deathsoundplayed = True

    def updatePowerups(self):
        for p in self.poweruparray:
            p.update()
            if patlib.distToPoint(p.center_x, p.center_y, self.ply.center_x, self.ply.center_y) < (player.RECT_WIDTH + powerups.POWERUP_WIDTH):
                self.powerupsound.play(self.powerupsoundspeed,0)
                if p.powerup == "POWERUP_HEALTH":
                    if self.ply.health <= 100:
                        self.ply.health += 10
                        if self.ply.health > 100:
                            self.ply.health = 100

                if p.powerup == "POWERUP_GODMODE":
                    self.ply.godmode = True
                    self.ply.godmodeexpiretime = p.powerupexpirytime
                    self.ply.health = 100

                if p.powerup == "POWERUP_TRIPLESHOT":
                    self.ply.trippleshot = True
                    self.ply.trippleshotexpiretime = p.powerupexpirytime

                self.poweruparray.remove(p)

            if p.center_y > 600 or p.center_y < -100 or p.center_x > 1100 or p.center_x < -100:
                self.poweruparray.remove(p)

    def updateEnemies(self):
        for e in self.enemyarray:

            e.update(self.ply.center_x, self.ply.center_y, self.time)

            for b in self.bulletarray:
                if patlib.distToPoint(e.center_x, e.center_y, b.center_x, b.center_y) < 25 and b.ownedbyplayer:
                    if not e.invincible:

                        if self.ply.trippleshot:
                            e.health -= b.damage*3
                        else:
                            e.health -= b.damage


                        if e.health <= 0:
                            self.ply.score += e.scorevalue
                            if random.randint(0,100) < POWERUP_CHANCE:
                                self.spawnPowerup(e)
                            if e in self.enemyarray:
                                self.enemyarray.remove(e)
                        if not self.ply.piercing:
                            if b in self.bulletarray:
                                self.bulletarray.remove(b)
                    else:
                        if b in self.bulletarray:
                            self.bulletarray.remove(b)

            if patlib.distToPoint(e.center_x, e.center_y, self.ply.center_x, self.ply.center_y) < 40:
                if not self.ply.godmode:
                    self.ply.health -= e.meleedamage
                    if self.ply.health < 0:
                        self.ply.health = 0

                if e in self.enemyarray:
                    self.enemyarray.remove(e)

            if e.__class__ == enemies.ShooterEnemy:
                if e.center_y > 500 or e.center_y < 0:
                    self.enemyarray.remove(e)
                if e.shoottime < self.time and len(self.bulletarray) < 30 and e.center_x < 1000:
                    e.shoottime = self.time + 1
                    self.bulletarray.append(bullet.BulletEntity(e.center_x, e.center_y, -10, 0, False, 10))
                    self.enemyshootsound.play(self.enemyshootsoundspeed, 0)


            if not -200 < e.center_x < 1200 or not -200 < e.center_y < 700:
                self.enemyarray.remove(e)


    def updateBullets(self):
        for b in self.bulletarray:
            b.update()
            if patlib.distToPoint(b.center_x, b.center_y, self.ply.center_x,
            self.ply.center_y) < 40 and not self.ply.godmode and not b.ownedbyplayer:
                self.ply.health -= b.damage
                if self.ply.health < 0:
                    self.ply.health = 0
                self.bulletarray.remove(b)
            if b.center_x > 1100 or b.center_x < -100 or b.center_y > 600 or b.center_y < -100:
                if b in self.bulletarray:
                    self.bulletarray.remove(b)

    def spawnPowerup(self, e):
        powerup_weight = random.uniform(0, POWERUP_TOTAL_WEIGHT)
        if POWERUP_GODMODE_WEIGHT > powerup_weight:
            self.poweruparray.append(
                powerups.PowerupEntity(e.center_x, e.center_y, e.change_x, e.change_y, "POWERUP_GODMODE",self.time + 10))
        elif POWERUP_TRIPPLESHOT_WEIGHT > powerup_weight:
            self.poweruparray.append(
                powerups.PowerupEntity(e.center_x, e.center_y, e.change_x, e.change_y, "POWERUP_TRIPLESHOT",self.time + 10))
        elif POWERUP_HEALTH_WEIGHT > powerup_weight:
            self.poweruparray.append(
                powerups.PowerupEntity(e.center_x, e.center_y, e.change_x, e.change_y, "POWERUP_HEALTH", self.time + 0))

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
        return 1

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

                    self.buttonclicksound.play(self.buttonclicksoundspeed,0)

                    if b.id == "BUTTON_START_GAME":
                        self.gamestate = "playing"

                    if b.id == "BUTTON_QUIT_GAME":
                        time.sleep(0.1)
                        arcade.exit()

        if self.gamestate == "pause":
            for b in self.pausebuttonarray:
                if b.center_x - mainmenu.BUTTON_LENGTH / 2 < x < b.center_x + mainmenu.BUTTON_LENGTH / 2 and \
                    b.center_y - mainmenu.BUTTON_WIDTH / 2 < y < b.center_y + mainmenu.BUTTON_WIDTH / 2:

                    self.buttonclicksound.play(self.buttonclicksoundspeed,0)

                    if b.id == "BUTTON_RESUME_GAME":
                        self.gamestate = "playing"

                    if b.id == "BUTTON_QUIT_GAME":
                        time.sleep(0.1)
                        arcade.exit()

                    if b.id == "BUTTON_GOTO_MENU":
                        self.retry()
                        self.gamestate = "menu"

                    if b.id == "BUTTON_RESET_GAME":
                        self.retry()

        if self.gamestate == "lose":
            for b in self.deathbuttonarray:
                if b.center_x - mainmenu.BUTTON_LENGTH / 2 < x < b.center_x + mainmenu.BUTTON_LENGTH / 2 and \
                    b.center_y - mainmenu.BUTTON_WIDTH / 2 < y < b.center_y + mainmenu.BUTTON_WIDTH / 2:

                    self.buttonclicksound.play(self.buttonclicksoundspeed,0)

                    if b.id == "BUTTON_QUIT_GAME":
                        time.sleep(0.1)
                        arcade.exit()

                    if b.id == "BUTTON_GOTO_MENU":
                        self.retry()
                        self.gamestate = "menu"

                    if b.id == "BUTTON_RESET_GAME":
                        self.retry()

    def on_mouse_release(self, x, y, button, key_modifiers):
        self.shooting = False


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
