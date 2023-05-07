import pygame 

class Player():
    def __init__(self, x, y, width, height):
        #cria o retangulo do jogador
        self.rect = pygame.Rect((x, y),(width, height))
        self.direcao = pygame.math.Vector2(0,0)

        #velocidades 
        self.velocidade = 2
        self.velocidade_Y = 4
        self.aceleracao = 2

        #variáveis de controle de pulo
        self.pulando = False
        self.altura_pulo = 100
        self.contador_pulo = 0
        self.podePular = True
    
    def moveX(self, dx):
        self.rect.x += dx * self.velocidade
    
    def moveY(self, dy):
        self.rect.y += dy * self.velocidade_Y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

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
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1 

        if keys[pygame.K_SPACE] and self.podePular:
            if not self.pulando:
                self.pulando = True
                self.contador_pulo = 0
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

