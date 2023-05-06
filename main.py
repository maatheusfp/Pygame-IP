import pygame as pg
from character.player import Player
from levels.maps import Level1
 
screenWidth, screenHeight = 1920, 1080 # 1920x1080 (Full HD)
pg.display.set_caption("Jogo Plataforma") # Nome da janela

pg.init()

clock = pg.time.Clock() #frames por segundo

def main():
    level = Level1(screenWidth, screenHeight)
    player = Player(100,100, level)
    run = True
    # Loop que executa o jogo
    while run:
        for entrada in pg.event.get(): # Faz uma lista de todos os eventos capturados pelo pygame do teclado, mouse, etc.
            if entrada.type == pg.QUIT:
                pg.quit()
                exit()
        
        level.desenhar()
        player.desenhaJogador(level.tela)
        player.atualiza()
        clock.tick(60)


if __name__ == "__main__":
    main()