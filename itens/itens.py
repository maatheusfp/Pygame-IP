import pygame

class Chave():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x,self.y),(width, height))


    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)