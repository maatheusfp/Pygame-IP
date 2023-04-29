# Importa o módulo pygame e o renomeia para "pg"; Inicializa o pygame
import pygame as pg
pg.init()
#from pygame.locals import *
#from sys import exit

class Player:
    # Definição de atributos
    def __init__(self, win, x, y, esquerda, direita, cima, baixo, cor, pulo, jumping=False):
        self.win = win # Janela
        self.x = x # Coordenada horizontal
        self.y = y # Coordenada vertical

        self.esquerda = esquerda
        self.direita = direita
        self.cima = cima
        self.baixo = baixo
        self.pulo = pulo
        self.jumping = jumping
        self.jumpCount = 10
        self.neg = 1
        # Características do Player
        self.altura = 30
        self.largura = 30
        self.velocidade = 6
        self.cor = cor
    # Definição de métodos
    def control(self): # Controlar o jogador
        keys = pg.key.get_pressed() # Checando as teclas pressionadas
        # VERIFICAR COMO DEPENDE DO TAMANHO DA TELA
        if (keys[self.esquerda]) and (self.x > 0):
            self.x -= self.velocidade
        if (keys[self.direita]) and (self.x < 1920 - self.largura - self.velocidade):
            self.x += self.velocidade
        if not (self.jumping): ###
            #if (keys[self.cima]) and (self.y > 0): CASO ELE SE MOVIMENTE PARA CIMA
            #    self.y -= self.velocidade
            if (keys[self.baixo]) and (self.y < 1080 - self.altura - self.velocidade):
                self.y += self.velocidade
            # Se apertar o espaço deve pular
            if (keys[self.pulo]) or (keys[self.cima]):
                self.jumping = True
                #isJump = True
        else:
            if self.jumpCount >= -10: # botei self em um monte
                self.neg = 1
                if self.jumpCount < 0:
                    self.neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * self.neg
                self.jumpCount -= 1
            else:
                self.jumping = False
                #isJump = False
                self.jumpCount = 10
        # Se apertar ESC, fecha o jogo
        if keys[pg.K_ESCAPE]:
            pg.quit()
            quit()

    def draw(self):
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.altura, self.largura))


def main():
    # Define o título da janela, depois o display, depois a taxa de atualização dos frames(?), depois o jogador, depois se o loop deve terminar
    pg.display.set_caption("Jogo OPP - Python")
    screenWidth, screenHeight = 1920, 1080
    screen = pg.display.set_mode((screenWidth, screenHeight))
    clock = pg.time.Clock()
    # Criando o jogador; ele screen pois é uma superfície plana, a posição inicial de x e depois y, as teclas de movimento e a cor
    player = Player(screen, 80, 1040, pg.K_a, pg.K_d, pg.K_w, pg.K_s, (255, 255, 255), pg.K_SPACE)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        player.control() # Chamando método para mover jogador
        screen.fill((40, 40, 40)) # Preencher a tela para não ver os frames anteriores, preenche com a cor definida pelo rgb
        player.draw()
        pg.display.flip()
        #pg.display.update()
        clock.tick(75)


if __name__ == '__main__':
    main()