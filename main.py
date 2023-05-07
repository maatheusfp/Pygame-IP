import pygame 
from character.player import Player
from levels.maps import *
from assets.background import GameBackground
from itens.itens import Time, Door, Key
import sys

pygame.display.set_caption("Jogo Plataforma") # Nome da janela

if __name__ == '__main__':
    pygame.init()

clock = pygame.time.Clock() #frames por segundo
screen = pygame.display.set_mode((screenWidth, screenHeight))
game_background = GameBackground(screenWidth, screenHeight)

obstacles = []
itens = []
keys = []
qtdTime = []
qtdKeys = []

x = y = 0
for row in layout:
    for col in row:
        if col == 'x':
            obstacle_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            obstacles.append(obstacle_rect)
        if col == 'P':
            player_rect = pygame.Rect(x, y, tile_Width, tile_Height)
        if col == 't':
            time_rect = pygame.Rect(x,y, tile_Width, tile_Height)
            itens.append(time_rect)
        if col == 'k':
            key_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            keys.append(key_rect)
        if col == 'd':
            door_rect = pygame.Rect(x, y, tile_Width, tile_Height)


        x += tile_Width
    y += tile_Height
    x = 0 

door = Door(door_rect.x, door_rect.y, door_rect.width, door_rect.height)
player = Player(player_rect.x, player_rect.y, player_rect.width, player_rect.height)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.controle(obstacles)

        game_background.update()
        screen.blit(game_background.screen, (0, 0))

        for item in itens:
            time_item = Time(item.x, item.y, item.width, item.height)
            if time_item.colisao(player.rect):
                itens.remove(item)
                qtdTime.append(1)
            time_item.draw(screen)
        
        for key in keys:
            key_item = Key(key_rect.x, key_rect.y, key_rect.width, key_rect.height)
            if key_item.colisao(player.rect):
                keys.remove(key)
                qtdKeys.append(1)
            key_item.draw(screen)
        
        door.draw(screen)
        if door.colisao(player_rect):
            pygame.quit()
            sys.exit()

        for obstacle in obstacles:
            pygame.draw.rect(screen, (0, 0, 255), obstacle)
            
        player.draw(screen)
        
        #texto para mostrar quantidade de coletaveis (requisito)
        """ text_rect = pygame.Rect((700,100), (200,200))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(f'Keys coletadas: {len(qtdKeys)}, Timers coletados: {len(qtdTime)}', True, (255,255,255))
        text_surface = pygame.Surface((text_rect.width, text_rect.height))
        text_surface.fill((0,0,0))
        text_surface.blit(text, (0,0))
        screen.blit(text_surface, text_rect) """


        clock.tick(100)
        pygame.display.update()

if __name__ == "__main__":
    main()