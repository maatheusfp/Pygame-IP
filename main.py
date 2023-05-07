import pygame 
from character.player import Player
from levels.maps import *
import sys

pygame.display.set_caption("Jogo Plataforma") # Nome da janela

pygame.init()

clock = pygame.time.Clock() #frames por segundo
obstacles = []
time_itens = []
screen = pygame.display.set_mode((screenWidth, screenHeight))

x = y = 0
for row in layout:
    for col in row:
        if col == 'x':
            obstacle_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            obstacles.append(obstacle_rect)
        if col == 'P':
            player_rect = pygame.Rect(x, y, tile_Width, tile_Height)
        if col == 'k':
            key_rect = pygame.Rect(x, y, tile_Width, tile_Height)
        if col == 'd':
            door_rect = pygame.Rect(x, y, tile_Width, tile_Height)
        if col == 't':
            time_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            time_itens.append(time_rect)
        
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
        key = player.check_collision(player.rect, obstacles, player.direcao.x, player.direcao.y)
        #player.inteact(["key", "door", "time"])

        screen.fill((255, 255, 255))
        for obstacle in obstacles:
            pygame.draw.rect(screen, (0, 0, 255), obstacle)
        player.draw(screen)
        pygame.draw.rect(screen, (0, 255, 0), key_rect)
        pygame.draw.rect(screen, (0, 0, 0), door_rect)
        for time_rect in time_itens:
            pygame.draw.rect(screen, (255, 255, 0), time_rect)
        clock.tick(100)
        pygame.display.update()


if __name__ == "__main__":
    main()