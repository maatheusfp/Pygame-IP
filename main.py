import pygame as pg
from character.player import Player
from levels.maps import Level1
 
screenWidth, screenHeight = 1920, 1080

pg.init()

clock = pg.time.Clock() #frames por segundo

def main():
    level = Level1(screenWidth, screenHeight)
    player = Player(100,100, level)
    while True:
        for entrada in pg.event.get():
            if entrada.type == pg.QUIT:
                pg.quit()
                exit()
        

        level.desenhar()
        player.desenhaJogador(level.tela)
        player.atualiza()
        clock.tick(30)

main()