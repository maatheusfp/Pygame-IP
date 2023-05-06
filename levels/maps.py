import pygame

screenWidth, screenHeight = 1920, 1080

layout = ['................',
          '................',
          '................',
          '................',
          'xxxxxxxxxxx.....',
          '................',
          '................',
          '..............xx',
          '................',
          'xxxxxxxxxxxxxxxx'
          ]

class Level1():
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura
        self.posicoesValidas = []  


    def desenhar(self):
        self.tela = pygame.display.set_mode((self.largura, self.altura),0)

        blocoWidth = self.largura / 16
        blocoHeight = self.altura / 12
        for linha in enumerate(layout):
            for coluna in range(0,16):
                x = coluna * blocoWidth
                y = linha[0] * blocoHeight
                bloco = layout[linha[0]][coluna]
                cor = (0,0,0)

                if bloco == "x":
                    bloco_rect = pygame.Rect((x,y),(blocoWidth, blocoHeight))
                    cor = (255, 255, 0)
                    self.posicoesValidas.append(bloco_rect)

                pygame.draw.rect(self.tela, cor, ((x,y),(blocoWidth, blocoHeight)), 2)
        
        pygame.display.update()