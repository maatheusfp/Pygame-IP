import pygame

# Esse objeto é o que o jogador precisa pegar para poder passar de fase
class Key():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x,self.y),(width, height))


    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)


# Esse objeto é o que o jogador deve pegar para passar de fase
class Door():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x,self.y),(width, height))


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)


# Esses objetos darão mais tempo ao jogador
class Time():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x,self.y),(width, height))


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 0), self.rect)