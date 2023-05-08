import pygame 
from character.player import Player
from levels.maps import *
from assets.background import GameBackground
from itens.itens import Mochila, Door, Key, Vem, ContadorItem
import sys

pygame.display.set_caption("Jogo Plataforma") # Nome da janela

if __name__ == '__main__':
    pygame.init()

clock = pygame.time.Clock() #frames por segundo
screen = pygame.display.set_mode((screenWidth, screenHeight))
game_background = GameBackground(screenWidth, screenHeight)

plataforma = pygame.image.load('assets/plataforma.png')

obstacles = []
itensKeys = []
itensMochila = []
itensVem = []

x = y = 0
for row in layout:
    for col in row:
        if col == 'x':
            obstacle_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            obstacles.append(obstacle_rect)
        if col == 'P':
            player_rect = pygame.Rect(x, y, tile_Width, tile_Height*2)
        if col == 'm':
            mochila_rect = pygame.Rect(x,y, tile_Width, tile_Height)
            itensMochila.append(mochila_rect)
        if col == 'k':
            key_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            itensKeys.append(key_rect)
        if col == 'v':
            vem_rect = pygame.Rect(x, y, tile_Width, tile_Height)
            itensVem.append(vem_rect)
        if col == 'd':
            door_rect = pygame.Rect(x, y, tile_Width * 2, tile_Height * 2)

        x += tile_Width
    y += tile_Height
    x = 0 

door = Door(door_rect.x, door_rect.y, door_rect.width, door_rect.height)
player = Player(player_rect.x, player_rect.y, player_rect.width, player_rect.height)
contadorKeys = ContadorItem(10,10, 'Chaves')
contadorMochila = ContadorItem(10,35, 'Mochilas')
ContadorVem = ContadorItem(10,60, 'Vem')

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.controle(obstacles)

        game_background.update()
        screen.blit(game_background.screen, (0, 0))

        for mochila in itensMochila:
            mochila_item = Mochila(mochila.x, mochila.y, mochila.width, mochila.height)
            if mochila_item.colisao(player.rect):
                itensMochila.remove(mochila)
                contadorMochila.adiciona()
                door.temMochila = True
            mochila_item.draw(screen)
        
        for key in itensKeys:
            key_item = Key(key.x, key.y, key.width, key.height)
            if key_item.colisao(player.rect):
                itensKeys.remove(key)
                contadorKeys.adiciona()
                door.temChave = True
            key_item.draw(screen)
        
        for vem in itensVem:
            vem_item = Vem(vem.x, vem.y, vem.width, vem.height)
            if vem_item.colisao(player.rect):
                itensVem.remove(vem)
                ContadorVem.adiciona()
                door.temVem = True
            vem_item.draw(screen)
        
        door.draw(screen)
        if door.colisao(player.rect):
            pygame.quit()
            sys.exit()
            

        for obstacle in obstacles:
            screen.blit(plataforma, (obstacle.x, obstacle.y))
            
        player.draw(screen)
        contadorKeys.render(screen)
        contadorMochila.render(screen)
        ContadorVem.render(screen)

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()