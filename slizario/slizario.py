from pygame import *
from random import randint
window = display.set_mode((700, 500))
background = transform.scale(image.load("New Piskel (3).png"), (700, 500))

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y = 0
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
class Tail(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y = 0

main_player = Player("New Piskel (2).png", 300, 400, 70, 70, 30)
 
prize = GameSprite("New Piskel (1).png", randint(80, 635), 100, 100, 100, randint(16, 23)*30)

tails = sprite.Group()




game = True
finish = False


score = 0

wait = 0
while game:
    if finish != True:
        
        if wait == 0:
            window.blit(background,(0, 0))
            main_player.update()
            main_player.reset()
            prize.update()
            prize.reset()
            tail.update()
            tail = ("New Piskel", player.rect.x-player.speed_x, player.rect.y-player.speed_y)
                tails.add(tail)
            if player.colliderect(prize):
                score += 1
                prize.rect.x = randint(0, 23)*30
                prize.rect.y = randint(0, 16)*16
            wait = 30   
        wait -= 1
    keys = key.get_pressed()
    if keys[K_LEFT]:
        main_player.speed_x = -main_player.speed
        main_player.speed_y = 0
    if keys[K_RIGHT]:
        main_player.speed_x = main_player.speed
        main_player.speed_y = 0
    if keys[K_UP]:
        main_player.speed_y = -main_player.speed
        main_player.speed_x = 0
    if keys[K_DOWN]:
        main_player.speed_y = main_player.speed
        main_player.speed_x = 0
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)