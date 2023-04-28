import pygame

from pygame.locals import *

from sys import exit


pygame.init()
pygame.display.set_caption('Joguinho Facul')

altura = 480
largura = 640
tamCirc = 40
x = altura//2
y = 0
tela = pygame.display.set_mode((altura, largura))
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(tela, (0,122,159), (x, y), tamCirc)

    if x >= altura:
        x = 0
    if y >= largura:
        y = 0
    if y < 0:
        y = largura-0.1
    if x < 0:
        x = altura-0.1

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    pygame.display.update()