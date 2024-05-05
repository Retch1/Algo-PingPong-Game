from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Player(GameSprite):
    def updateP1(self):
        keys = key.get_pressed()
        if (keys[K_UP] or keys[K_w]) and self.rect.y > 10:
            self.rect.x -= self.speed
        if (keys[K_DOWN] or keys[K_s]) and self.rect.y < 500:
            self.rect.x += self.speed
    
    def updateP2(self):
        keys = key.get_pressed()
        if (keys[K_w]) and self.rect.y > 0:
            self.rect.x -= self.speed
        if (keys[K_s]) and self.rect.y < 500:
            self.rect.x += self.speed