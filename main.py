import pygame 
from character.player import Player
from levels.maps import *
import sys

pygame.display.set_caption("Jogo Plataforma") # Nome da janela

pygame.init()

clock = pygame.time.Clock() #frames por segundo
obstacles = []
screen = pygame.display.set_mode((screenWidth, screenHeight))

x = y = 0
for row in layout:
    for col in row:
        if col == 'x':
            obstacle_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            obstacles.append(obstacle_rect)
        if col == 'P':
            player_rect = pygame.Rect(x, y, tile_Width, tile_Height)
        
        x += tile_Width
    y += tile_Height
    x = 0 
player = Player(player_rect.x, player_rect.y, player_rect.width, player_rect.height)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.controle(obstacles)

        screen.fill((255, 255, 255))
        for obstacle in obstacles:
            pygame.draw.rect(screen, (0, 0, 255), obstacle)
        player.draw(screen)
        clock.tick(100)
        pygame.display.update()


if __name__ == "__main__":
    main()