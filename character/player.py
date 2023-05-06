import pygame 

class Player():
    def __init__(self, x, y, width, height):
        #cria o retangulo do jogador
        self.rect = pygame.Rect((x, y),(width, height))
        self.direcao = pygame.math.Vector2(0,0)

        #velocidades 
        self.velocidade = 4
        """ self.gravidade = 0.09 """
        """ self.noAr = False """
    
    def moveX(self, dx):
        self.rect.x += dx * self.velocidade
    
    def moveY(self, dy):
        self.rect.y += dy * self.velocidade

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

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

    def controle(self, obstacles):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
            self.direcao.x = -1
            self.direcao.y = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
            self.direcao.x = 1
            self.direcao.y = 0
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
            self.direcao.y = -1
            self.direcao.x = 0
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1 
            self.direcao.y = 1
            self.direcao.x = 0

        if not self.check_collision(self.rect, obstacles, dx, 0):
            self.moveX(dx)

        if not self.check_collision(self.rect, obstacles, 0, dy):
            self.moveY(dy)

        return dx, dy

    """ def gravitacao(self):
        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y """

