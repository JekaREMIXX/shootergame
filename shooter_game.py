#Создай собственный Шутер!

from pygame import *
import random
from time import time as t
font.init()

font=font.SysFont('Arial', 40)
window = display.set_mode((700,500))
display.set_caption("pygame window")
background =transform.scale(image.load("galaxy.jpg"), (700,500))
rocket=transform.scale(image.load("rocket.png"), (100,100))
bullet =transform.scale(image.load("bullet.png"), (25,25))
ufo =transform.scale(image.load("ufo.png"), (100,100))
asteroid=transform.scale(image.load("asteroid.png"), (100,100)) 

x1=300
y1=400
x2=300
y2=10
x3=1
y3=1
speed=10
speed_player=10
class GameSprite(sprite.Sprite):
    def __init__(self,rocket,x1,y1,speed):
        super().__init__()
        self.image = rocket
        self.speed = speed_player
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    global bullet
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >5:
            self.rect.x -=10
        if keys_pressed[K_RIGHT] and self.rect.x <600:
            self.rect.x +=10
    def fire(self):
        bullet1= Bullet(bullet, self.rect.centerx,self.rect.top,-15)
        bullets.add(bullet1)

ammo=5
numammo=0
score=0
lost=0
waitseconds=t()
wait=False
direction="down"
textscore=font.render("Счет: " + str(score), 1, (255, 255, 255))
textlose=font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
finishlose=font.render("YOU LOSE", 1, (255, 0, 0))
finishwin=font.render("YOU WIN", 1, (255, 0, 0))
class Enemy(GameSprite):
    def update(self):
        global direction
        global lost
        speed=2
        if direction=="down":
            self.rect.y +=random.randint(1,5)
        if self.rect.y>600:
            self.rect.y =0
            lost = lost+1
            self.rect.x = random.randint(10,600)
class Asteroid(GameSprite):
    def update(self):
        global direction
        global lost
        speed=2
        if direction=="down":
            self.rect.y +=random.randint(1,5)
        if self.rect.y>600:
            self.rect.y =0
            lost = lost+1
            self.rect.x = random.randint(10,600)
class Bullet(GameSprite):
    def update(self):
        speed=8
        direction="up"
        if direction=="up":
            self.rect.y -=1
        if self.rect.y<5:
            self.kill()

                
    
finish=False
game=True
clock = time.Clock()
FPS = 60
monsters=sprite.Group()
monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
asteroids=sprite.Group()
asteroids.add(Asteroid(asteroid,random.randint(10,600),y2,speed))
asteroids.add(Asteroid(asteroid,random.randint(10,600),y2,speed))
asteroids.add(Asteroid(asteroid,random.randint(10,600),y2,speed))
bullets=sprite.Group()



gamesprite1 = Player(rocket,x1,y1,speed)
gamesprite2 = Player(ufo,x1,y1,speed)
gamesprite3 = Enemy(ufo,random.randint(10,600),y2,speed)
gamesprite4 = Bullet(bullet,x1,y1,speed)
gamesprite5 = Asteroid(asteroid,random.randint(10,600),y2,speed)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if ammo>=0 and wait==False:
                        gamesprite1.fire()
                        ammo=ammo-1
                    if ammo<=0 and wait==False:
                        waitseconds=t()
                        wait=True
                    timer=t()
                    if timer-waitseconds>=1 and wait==True:
                        ammo=5
                        wait=False
    if finish != True:
        window.blit(background,(0,0))
        clock.tick(FPS)
        gamesprite1.reset()
        gamesprite1.update()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.draw(window)
        bullets.update()
        if sprite.groupcollide(monsters, bullets, True, True):
            score = score+1
            monsters.add(Enemy(ufo,random.randint(10,600),y2,speed))
        textscore=font.render("Счет: " + str(score), 1, (255, 255, 255))
        textlose=font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        if lost>3 or sprite.spritecollide(gamesprite1, monsters, True):
            window.blit(finishlose,(300, 300))
            finish = True
        if lost>3 or sprite.spritecollide(gamesprite1, asteroids, True):
            window.blit(finishlose,(300, 300))
            finish = True
            

        if score==10:
            window.blit(finishwin,(300, 300))
            finish = True
        window.blit(textscore,(10, 20))
        window.blit(textlose,(10, 50))
        display.update()