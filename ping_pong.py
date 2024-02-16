from pygame import *

class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def rezet(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Game_sprite):
    def update_r(self):
        case = key.get_pressed()
        if case[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if case[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed 
    def update_l(self):
        case = key.get_pressed()
        if case[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if case[K_s] and self.rect.y < 420:
            self.rect.y += self.speed 

roket1 = Player('left.png',30, 200, 4, 50, 100)
roket2 = Player('Right.png', 520, 200, 4, 50, 100)
ball = Game_sprite('tenisball.png', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)

lose1 = font.render(input('Введите ваше имя 1')+', ты проиграл!', True, (180, 0, 0))
lose2 = font.render(input('Введите ваше имя 2')+', ты проиграл!', True, (180, 0, 0))

back = (51, 148, 204)
window = display.set_mode((600, 500))
window.fill(back)
game = True
finish = False
clock = time.Clock()
fps = 60





while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        roket1.update_l()
        roket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(roket1, ball) or sprite.collide_rect(roket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            #game = False
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200, 200))
            #game = False
        roket1.rezet()
        roket2.rezet()
        ball.rezet()
    display.update()
    clock.tick(fps)