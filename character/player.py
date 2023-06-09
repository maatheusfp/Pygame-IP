import pygame 

R1 = pygame.image.load("assets/characterSprites/R1.png")
R2 = pygame.image.load("assets/characterSprites/R2.png")
R3 = pygame.image.load("assets/characterSprites/R3.png")
R4 = pygame.image.load("assets/characterSprites/R4.png")
R5 = pygame.image.load("assets/characterSprites/R5.png")
R6 = pygame.image.load("assets/characterSprites/R6.png")
R7 = pygame.image.load("assets/characterSprites/R7.png")
R8 = pygame.image.load("assets/characterSprites/R8.png")
R1 = pygame.transform.scale(R1, (70, 120))
R2 = pygame.transform.scale(R2, (70, 120))
R3 = pygame.transform.scale(R3, (70, 120))
R4 = pygame.transform.scale(R4, (70, 120))
R5 = pygame.transform.scale(R5, (70, 120))
R6 = pygame.transform.scale(R6, (70, 120))
R7 = pygame.transform.scale(R7, (70, 120))
R8 = pygame.transform.scale(R8, (70, 120))
andando_direita = [R1, R2, R3, R4, R5, R6, R7, R8]

andando_esquerda = [pygame.transform.flip(R1, True, False), 
                    pygame.transform.flip(R2, True, False), 
                    pygame.transform.flip(R3, True, False), 
                    pygame.transform.flip(R4, True, False), 
                    pygame.transform.flip(R5, True, False), 
                    pygame.transform.flip(R6, True, False), 
                    pygame.transform.flip(R7, True, False), 
                    pygame.transform.flip(R8, True, False)]
parado_direita = pygame.image.load("assets/characterSprites/Standing.png")
parado_direita = pygame.transform.scale(parado_direita, (60, 120))
parado_esquerda = pygame.transform.flip(parado_direita, True, False)

class Player():
    def __init__(self, x, y, width, height):
        #cria o retangulo do jogador
        self.rect = pygame.Rect((x, y),(width, height))

        #velocidades 
        self.velocidade = 2
        self.velocidade_Y = 4
        self.aceleracao = 2

        # variáveis de controle de animação
        self.esquerda = False
        self.direita = False
        self.contagem_passos = 0
        self. direcao = 1 ######

        #variáveis de controle de pulo
        self.pulando = False
        self.altura_pulo = 100
        self.contador_pulo = 0
        self.podePular = True

    def draw(self, surface):
        self.contagem_passos = self.contagem_passos % 24

        if self.esquerda:
            surface.blit(andando_esquerda[self.contagem_passos//3], (self.rect.x, self.rect.y))
            self.contagem_passos += 1
        elif self.direita:
            surface.blit(andando_direita[self.contagem_passos//3], (self.rect.x, self.rect.y))
            self.contagem_passos += 1
        else:
            if self.direcao == 1:
                surface.blit(parado_direita, (self.rect.x, self.rect.y))
            elif self.direcao == -1:
                surface.blit(parado_esquerda, (self.rect.x, self.rect.y))
            self.contagem_passos = 0

    
    def moveX(self, dx):
        self.rect.x += dx * self.velocidade
    

    def moveY(self, dy):
        self.rect.y += dy * self.velocidade_Y


    def check_collision(self, player_rect, obstacles, dx, dy):
        temp_rect = player_rect.copy()
        temp_rect.x += dx * self.velocidade
        temp_rect.y += dy * self.velocidade_Y
        for obstacle in obstacles:
            if temp_rect.colliderect(obstacle):    #ele verifica o lado em que está tendo a colisão
                if dx == 1 and obstacle.left <= player_rect.right:
                    return True
                if dx == -1 and obstacle.right >= player_rect.left:
                    return True
                if dy == 1 and obstacle.top <= player_rect.bottom:
                    return True
                if dy == -1 and obstacle.bottom >= player_rect.top:
                    return True
        return False
    

    def gravidade(self, obstacles):
        if not self.check_collision(self.rect, obstacles, 0, 1):
            dy = 1
            self.rect.y += dy * self.aceleracao
            self.podePular = False
        
        else:
            self.podePular = True


    def controle(self, obstacles):

        self.gravidade(obstacles)

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0                                    #colisao com a tela                   
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            dx = -1
            self.esquerda = True
            self.direita = False
            self.direcao = -1
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < 1880:
            dx = 1
            self.esquerda = False
            self.direita = True
            self.direcao = 1
        if not (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.esquerda = False
            self.direita = False
            self.contagem_passos = 0

        if keys[pygame.K_SPACE] and self.podePular and self.rect.y > 0:
            if not self.pulando: 
                self.pulando = True 
                self.contador_pulo = 0
                self.esquerda = False
                self.direita = False
                self.contagem_passos = 0
                dy = -1

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        if not self.check_collision(self.rect, obstacles, dx, 0):
            self.moveX(dx)

        if not self.check_collision(self.rect, obstacles, 0, dy):
            self.moveY(dy)
        
        if self.pulando: 
            dy = -1
            self.contador_pulo += 1
            if self.contador_pulo > self.altura_pulo:
                self.pulando = False 

        if not self.check_collision(self.rect, obstacles, dx, 0):
            self.moveX(dx)

        if not self.check_collision(self.rect, obstacles, 0, dy):
            self.moveY(dy) 

        return dx, dy
