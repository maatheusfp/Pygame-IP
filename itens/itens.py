import pygame

class Vem:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.image = pygame.image.load("assets/vem.png")
        self.coletado = False

    def draw(self, surface):
        if not self.coletado:
            surface.blit(self.image, self.rect)
    
    def colisao(self, player_rect):
            if player_rect.colliderect(self.rect):
                self.coletado = True
                
                return True

class Key:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.image = pygame.image.load("assets/chave.png")
        self.coletado = False
    
    def draw(self, surface):
         if not self.coletado:
              surface.blit(self.image, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect):
              self.coletado = True
              
              return True

class Mochila:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.image = pygame.image.load("assets/mochila.png")
        self.coletado = False
    
    def draw(self, surface):
         if not self.coletado:
              surface.blit(self.image, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect):
              self.coletado = True
              
              return True

class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x, y), (width, height))
        self.image = pygame.image.load("assets/porta.png")
        self.temMochila = False
        self.temChave = False
        self.temVem = False


    def draw(self, surface):
         surface.blit(self.image, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect) and self.temMochila and self.temChave and self.temVem:

              return True
  
class ContadorItem:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome
        self.counter = 0
        self.font = pygame.font.SysFont(None, 30)
    
    def adiciona(self):
         self.counter += 1
    
    def render(self, surface):
         text = self.font.render(f'{self.nome} coletados: {self.counter}', True, (255, 255, 255))
         surface.blit(text, (self.x, self.y))
    


          

