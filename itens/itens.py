import pygame

class Time:
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

class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect((x, y), (width, height))
        self.color = (0,0,0)


    def draw(self, surface):
         pygame.draw.rect(surface, self.color, self.rect)
    
    def colisao(self, player_rect):
         if player_rect.colliderect(self.rect) :

              return True
    
class Contador:
     def __init__(self, keysColetadas, timerColetados):
          self.font = pygame.font.SysFont('Arial', 20)
          self.rect = pygame.Rect(700, 100, (200,100))
