import pygame
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, ferrari_player, ferrari_x, ferrari_y, ferrari_speed):
        super()._init_()

        self.image = transform.scale(image.load(ferrari_player), (0,0))

        self.speed = ferrari_speed

        self.rect = self.image.get.get_rect()
        self.rect.x = ferrari_x
        self.rect.y = ferrari_y












win_width = 700
win_height = 500

window = display.set.mode((win_width, win_height))
background = transform.scale(image.load("background_1.png"), (win_width, win_height))
    





   
    