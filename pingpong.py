
from pygame import*
class GameSprite(sprite.Sprite):
 #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

       #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

      

       #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #method drawing the character on the window

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
   #method to control the sprite with arrow keys
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed       
 #method to "shoot" (use the player position to create a bullet there)

   
back = (200,255,255)
win_with = 600
win_height = 500
window = display.set_mode((win_with,win_height))
game = True
finish = False
clock = time.Clock()
FPS = 60






platform_left = Player('racket.png',30,250,40,100,15)
platform_right = Player('racket.png',520,250,40,100,15)
lopta = GameSprite('tenis_ball.png',200,200,50,50,20)

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None,36)
player1win = font1.render('PLAYER 1  WIN', True,(190,0,0))
player2win = font1.render('PLAYER 2  WIN', True,(190,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish :
        window.fill(back) 
        platform_left.reset()
        platform_right.reset()
        lopta.reset()
        platform_left.update_l()
        platform_right.update_r()
        lopta.rect.x += speed_x
        lopta.rect.y += speed_y
    if lopta.rect.y > win_height-50 or lopta.rect.y < 0:

        speed_y *= -1
    if sprite.collide_rect(platform_left, lopta) or sprite.collide_rect(platform_right, lopta):
        speed_y *= 1
        speed_x *= -1
    if  lopta.rect.x > win_with:
        finish = True
        window.blit(player1win,(200,200))
    if  lopta.rect.x < 0:
        finish = True
        window.blit(player2win,(200,200))
















    display.update()
    clock.tick(FPS)        



