import pygame

andando_direita = [pygame.image.load('assets/characterSprites/R1.png'), 
                   pygame.image.load('assets/characterSprites/R2.png'), 
                   pygame.image.load('assets/characterSprites/R3.png'), 
                   pygame.image.load('assets/characterSprites/R4.png'), 
                   pygame.image.load('assets/characterSprites/R5.png'), 
                   pygame.image.load('assets/characterSprites/R6.png'), 
                   pygame.image.load('assets/characterSprites/R7.png'), 
                   pygame.image.load('assets/characterSprites/R8.png')]

R1 = pygame.image.load("assets/characterSprites/R1.png")
R2 = pygame.image.load("assets/characterSprites/R2.png")
R3 = pygame.image.load("assets/characterSprites/R3.png")
R4 = pygame.image.load("assets/characterSprites/R4.png")
R5 = pygame.image.load("assets/characterSprites/R5.png")
R6 = pygame.image.load("assets/characterSprites/R6.png")
R7 = pygame.image.load("assets/characterSprites/R7.png")
R8 = pygame.image.load("assets/characterSprites/R8.png")

andando_esquerda = [pygame.transform.flip(R1, True, False), 
                    pygame.transform.flip(R2, True, False), 
                    pygame.transform.flip(R3, True, False), 
                    pygame.transform.flip(R4, True, False), 
                    pygame.transform.flip(R5, True, False), 
                    pygame.transform.flip(R6, True, False), 
                    pygame.transform.flip(R7, True, False), 
                    pygame.transform.flip(R8, True, False)]
parado = pygame.image.load("assets/characterSprites/standing.png")

class Player():
    def __init__(self, x, y, width, height):
        # Cria o retangulo do jogador
        self.rect = pygame.Rect((x, y),(width, height))
        self.direcao = pygame.math.Vector2(0,0)

        # Booleanas
        self.pulando = False
        self.contagem_pulo = 10
        self.esquerda = False
        self.direita = False
        self.contagem_passos = 0

        #velocidades 
        self.velocidade = 4
        self.aceleracao = 2

#		self.image = self.images_right[self.index]
#		self.rect = self.image.get_rect()
#		screen.blit(self.image, self.rect)
    
    def draw(self, surface):

        if self.contagem_passos + 1 >= 23:
            self.contagem_passos = 0
        
        if self.esquerda:
            surface.blit(andando_esquerda[self.contagem_passos//3], (self.rect.x, self.rect.y))
            self.contagem_passos += 1
        elif self.direita:
            surface.blit(andando_direita[self.contagem_passos//3], (self.rect.x, self.rect.y))
            self.contagem_passos += 1
        else:
            surface.blit(parado, (self.rect.x, self.rect.y))
            self.contagem_passos = 0


    def moveX(self, dx):
        self.rect.x += dx * self.velocidade
    

    def moveY(self, dy):
        self.rect.y += dy * self.velocidade


    def check_collision(self, player_rect, obstacles, dx, dy):
        temp_rect = player_rect.copy()
        temp_rect.x += dx * self.velocidade
        temp_rect.y += dy * self.velocidade
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


    def controle(self, obstacles):

        self.gravidade(obstacles)

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
            self.direcao.x = -1
            self.direcao.y = 0
            self.esquerda = True
            self.direita = False
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
            self.direcao.x = 1
            self.direcao.y = 0
            self.esquerda = False
            self.direita = True
        else:
            self.esquerda = False
            self.direita = False
            self.contagem_passos = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
            self.direcao.y = -1
            self.direcao.x = 0
            self.pulando = True
            self.esquerda = False
            self.direita = False
            self.contagem_passos = 0

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        if not self.check_collision(self.rect, obstacles, dx, 0):
            self.moveX(dx)

        if not self.check_collision(self.rect, obstacles, 0, dy):
            self.moveY(dy)

        return dx, dy