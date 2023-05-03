import pygame 

class Player():
    def __init__(self, x, y, level):
        #coordenadas
        self.x = x
        self.y = y

        #movimento
        self.direcao = pygame.math.Vector2(0,0)
        self.velocidade = 6
        self.gravidade = 0.09
        self.noAr = False

        #caracteristicas
        self.rect = pygame.Rect((self.x,self.y),(100,100))

        #colisao
        self.posicaoValida = level.posicoesValidas

    def movimentacao(self):
        velocidadePulo = -6
        """ self.pulando = False """

        if pygame.key.get_pressed()[pygame.K_RIGHT]: 
            self.direcao.x = 1
        
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direcao.x = -1
        
        else:
            self.direcao.x = 0
        
        #Para não dar um pulo duplo
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.noAr:
            self.direcao.y = velocidadePulo
            """ self.pulando = True """

        """ if self.pulando:
            self.y = -velocidadePulo
            self.noAr = True
            self.pulando = False """
        
    def gravitacao(self):
        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y

    def desenhaJogador(self, screen):
        cor = (255, 255, 255)
        pygame.draw.rect(screen, cor, self.rect)
        pygame.display.update()
    
    def colisaoHorizontal(self):
        for sprite in self.posicaoValida:
            if self.rect.colliderect(sprite):
                if self.direcao.x < 0:
                    self.direcao.x = 1
                
                elif self.direcao.x > 0:
                    self.direcao.x = -1
    
    def colisaoVertical(self):
        for sprite in self.posicaoValida:
            if self.rect.colliderect(sprite):
                if self.direcao.y < 0:
                    self.direcao.y = -0.09
                
                elif self.direcao.y > 0:
                    self.direcao.y = 0.09


    def atualiza(self):
        self.colisaoVertical()
        self.colisaoHorizontal()
        self.movimentacao()
        self.rect.x += self.direcao.x * self.velocidade
        self.gravitacao()