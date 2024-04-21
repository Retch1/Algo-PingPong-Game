from pygame import *
from spriteModule import *

bg = (0, 0, 0)
window = display.set_mode((800, 500))
display.set_caption("Ping Pong")
clock = time.Clock()

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))

player1 = Player("sprites/paddle.png", 10, 200, 50, 100, 5)
player2 = Player("sprites/paddle.png", 750, 200, 50, 100, 5)
ball = GameSprite("sprites/ball.png", 350, 200, 25, 25, 5)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    window.fill(bg)

    player1.update()
    player2.update()
    reset(player1)
    reset(player2)

    clock.tick(60)
    display.update()