from pygame import *

class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.tect.y = player_y
    def rezet(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

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
    display.update()
    clock.tick(fps)