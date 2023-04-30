import pygame 

class Player():
    def __init__(self):
        #coordenadas
        self.x = int()
        self.y = int()
        self.direcao = pygame.math.Vector2(0,0)  #pra gravidade

        #movimento
        self.velocidade = 6
        self.gravidade = 0.9
        self.esquerda = False
        self.direita = False
        self.noAr = True

        #caracteristicas
        self.player_rect = pygame.Rect((100,100),(30,30))

    def movimentacao(self):
        velocidadePulo = 15
        self.pulando = False

        #Para apertar apenas um botão por vez
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  
            self.direcao.x = 1
            self.esquerda = False
            self.direita = True
        
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direcao.x = -1
            self.direita = False
            self.esquerda = True
        
        else:
            self.direcao.x = 0
            self.esquerda = False
            self.direita = False
        
        #Para não dar um pulo duplo
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.noAr:
            self.pulando = True

        if self.pulando:
            self.direcao.y = -velocidadePulo
            self.noAr = True
            self.pulando = False
        
        if self.direita:
            self.x += self.velocidade
        
        if self.esquerda: 
            self.x -= self.velocidade
        
    def gravitacao(self):
        self.direcao.y += self.gravidade