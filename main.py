import pygame as pg
from character.player import Player
from levels.maps import Level1
 
screenWidth, screenHeight = 1920, 1080
tela = pg.display.set_mode((screenWidth, screenHeight))

pg.init()

clock = pg.time.Clock() #frames por segundo

def main():
    jogador = Player()
    level = Level1

    while True:
        for entrada in pg.event.get():
            if entrada.type == pg.QUIT:
                pg.quit()
                exit()
        
        level.draw()  #cria a função que desenha o mapa 
        jogador.draw() #cria a função que desenha o jogador (ainda não fiz)


main()