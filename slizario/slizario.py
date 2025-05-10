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
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed, timer):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y = 0
        self.timer = timer

    def update(self):
        print(self.timer)
        self.timer -= 1
        if self.timer <= 0:
            self.image = transform.scale(image.load("New Piskel.png"), (69, 69))
            self.kill()




main_player = Player("New Piskel (2).png", 300, 400, 30, 30, 30)
 
prize = GameSprite("New Piskel (1).png", randint(80, 635), 100, 30, 30, randint(16, 23)*30)

tails = sprite.Group()


game = True
finish = False


score = 1

wait = 0
while game:
    if finish != True:
        if wait == 0:
            window.blit(background,(0, 0))
            main_player.update()
            main_player.reset()
            prize.update()
            prize.reset()
            tail = Tail("New Piskel.png", main_player.rect.x - main_player.speed_x, main_player.rect.y - main_player.speed_y, 29, 29, 0, score)
            tails.add(tail)
            tails.update()
            tails.draw(window)
            if main_player.colliderect(prize):
                score += 1
                prize.rect.x = randint(0, 23)*30
                prize.rect.y = randint(0, 16.5)*30
            if sprite.spritecollide(main_player, tails, True):
                finish = True
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