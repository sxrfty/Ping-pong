from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

back = (200, 255, 255)
window = display.set_mode((600, 500))

finish = False

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 36)
lose1 = font.render('Первый игрок проиграл', True, (180, 0, 0))
lose2 = font.render('Второй игрок проиграл', True, (180, 0, 0))




player = Player('racket.png', 10, 200, 10, 100, 10)
player2 = Player('racket.png', 580, 200, 10, 100, 10)
ball = GameSprite('tenis_ball.png', 300, 200, 50, 50, 3)


clock = time.Clock()
FPS = 60



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        player.update_l()
        player2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
                       
    if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True

    if ball.rect.x > 550:
        finish = True
        window.blit(lose2, (200, 200))
        game_over = True









    player2.update()
    player2.reset()
    player.update()
    player.reset()
    ball.update()
    ball.reset()
  
    display.update()
    clock.tick(FPS)