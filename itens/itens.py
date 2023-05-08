import pygame

class Vem:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.color = (255, 255, 0)
        self.coletado = False

    def draw(self, surface):
        if not self.coletado:
            pygame.draw.rect(surface, self.color, self.rect)
    
    def colisao(self, player_rect):
            if player_rect.colliderect(self.rect):
                self.coletado = True
                
                return True

class Key:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.color = (230, 0, 125)
        self.coletado = False
    
    def draw(self, surface):
         if not self.coletado:
              pygame.draw.rect(surface, self.color, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect):
              self.coletado = True
              
              return True

class Mochila:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x,y), (width, height))
        self.color = (230, 123, 125)
        self.coletado = False
    
    def draw(self, surface):
         if not self.coletado:
              pygame.draw.rect(surface, self.color, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect):
              self.coletado = True
              
              return True

class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x, y), (width, height))
        self.color = (0,0,0)


    def draw(self, surface):
         pygame.draw.rect(surface, self.color, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect) :

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
    


          

