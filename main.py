from pygame import *
from spriteModule import *
import random

font.init()
victor = font.Font(None, 50)
P1_win = victor.render("P1 WIN", True, (255, 255, 255))
P2_win = victor.render("P2 WIN", True, (255, 255, 255))

bg = (0, 0, 0)
window = display.set_mode((800, 500))
display.set_caption("Ping Pong")
clock = time.Clock()

side = random.randrange(1, 3)
direction = random.randrange(1, 3)
p1_points = 0
p2_points = 0

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))

player1 = Player("sprites/paddle.png", 10, 200, 50, 100, 5)
player2 = Player("sprites/paddle.png", 750, 200, 50, 100, 5)
ball = GameSprite("sprites/ball.png", 370, 200, 25, 25, 2)

running = True
finish = False
while running:
    if not finish:
        window.fill(bg)

        player1.updateP1()
        player2.updateP2()

        reset(player1)
        reset(player2)
        reset(ball)

        # Movement
        collide_p1 = sprite.collide_rect(player1, ball)
        collide_p2 = sprite.collide_rect(player2, ball)

        if side == 1:
            ball.rect.x -= ball.speed
            if direction == 1:
                ball.rect.y += ball.speed
            else:
                ball.rect.y -= ball.speed
        else:
            ball.rect.x += ball.speed
            if direction == 1:
                ball.rect.y += ball.speed
            else:
                ball.rect.y -= ball.speed
        # Bounce
        if ball.rect.y > 470:
            direction = 2
        if ball.rect.y < 0:
            direction = 1
        
        if ball.rect.x < -30:
            finish = True
            window.blit(P2_win, (345, 230))
        if ball.rect.x > 810:
            finish = True
            window.blit(P1_win, (345, 230))
        if collide_p1:
            ball.speed+=.1
            side = 2
        if collide_p2:
            ball.speed+=.1
            side = 1

    for e in event.get():
        if e.type == QUIT:
            running = False
    clock.tick(60)
    display.update()