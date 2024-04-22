from pygame import*
from random import*

okno = display.set_mode((1200,600))
fps = time.Clock()
game = True

fon = image.load('mramor.jpg')
fon = transform.scale(fon, (1000,600))

points1 = 0
points2= 0
font.init()
wr = font.Font("Niagara Engraved.ttf", 35)
wr2 = font.Font("Niagara Engraved.ttf", 70)

class gameobj(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class player(gameobj):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 7
        elif kn[K_RIGHT] and self.rect. x < 930:
            self.rect.x += 7
platform = player('purple.png', 480,520,100,30)

class player2(gameobj):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_a] and self.rect.x > 0:
            self.rect.x -= 7
        elif kn[K_d] and self.rect. x < 930:
            self.rect.x += 7
platform2 = player2('purple.png', 480,80,100,30)

class baton(gameobj):
    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
vihod = baton('123.png', 1050,550,100,30)

ball=gameobj("circle.png",600,300,40,40)
dx =1
dy =-1

plita = []
enemies = []

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    okno.fill((106, 90, 205))
    okno.blit(fon,(0,0))
    hp = wr.render("P1: " + str(points1), False, (255,255,255))
    pp = wr.render("P2: " + str(points2), False, (255,0,255))
    okno.blit(hp, (1100,40))
    okno.blit(pp, (1100,80))
    
    platform.move()
    platform2.move()
    ball.ris()
    vihod.ris()
    ball.rect.x +=dx
    ball.rect.y +=dy

    if sprite.collide_rect(ball, platform2):
        dy*= -1
        dx = choice([-2,-1,1,2])
        ball.rect.y +=dy
    if sprite.collide_rect(ball, platform):
        dy*= -1
        dx = choice([-2,-1,1,2])
        ball.rect.y +=dy
    if ball.rect.x <= 0:
        dx*= -1
        #dy = choice([-2,-1,1,2])
    if ball.rect.x >= 1000 - ball.rect.width:
        dx*= -1
        #dy = choice([-2,-1,1,2])

    if ball.rect.y <= 0:
        points2+=1
        ball.rect.y=300
        if points2 == 10:
            p3 = wr2.render("P2 Wins!" , False, (255,0,0))
            okno.blit(p3, (500,200))
            game = False

    if ball.rect.y >= 600:
        points1+=1
        ball.rect.y=300
        if points1 == 10:
            p3 = wr2.render("P1 Wins!" , False, (255,0,0))
            okno.blit(p3, (500,200))
            game = False
    fps.tick(100)
    display.update()
time.wait(2000)    