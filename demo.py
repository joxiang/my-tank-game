import sys, random, math, pygame
from pygame.locals import*
from const import*
from tank import*
from bullet import*
def ButtonSense():
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        exit()
    if keys[K_w]:
        player1.move(up, 0.0)
    elif keys[K_s]:
        player1.move(down, 180)
    elif keys[K_a]:
        player1.move(left, 90)
    elif keys[K_d]:
        player1.move(right, 270)
    if bullet.alive == False:
        if keys[K_SPACE]:
            bullet.x=player1.x
            bullet.y=player1.y
            bullet.hp=1
            bullet.alive=True
            bullet.dir=player1.dir
            bullet.angle=player1.angle
bg = "bg.jpg"
def init():
    global bg;#全局变量
    bg = pygame.image.load(bg).convert();
    bg = pygame.transform.smoothscale(bg,(sw,sh))

def disBg(win):
    win.blit(bg,(0,0))
pygame.init()
win = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("TANK")

player1 = Tank("tank.png", 0, 0)
player1.health = 3
player1.alive = True
bullet=Bullet("bullet.png",player1.x, player1.y)
bullet.step = 1
init()
worldTime = 0
while True:
    # print(bullet.alive, bullet.x, bullet.y)
    worldTime+=1
    for event in pygame.event.get():
        if event.type == QUIT: exit()
    #stuff that happen:        
    disBg(win)#finished a background display
    ButtonSense()
    bullet.move(bullet.dir, bullet.angle)
    bullet.drawImgd()
    player1.drawImgd(worldTime)

    pygame.display.update()