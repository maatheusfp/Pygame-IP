import pygame
import math

class GameBackground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game background")
        self.bg = pygame.image.load("assets/game_background.jpg").convert()
        self.bg_width = self.bg.get_width()
        self.bg_rect = self.bg.get_rect()
        self.scroll = 0
        self.tiles = math.ceil(self.width / self.bg_width) + 1

    def update(self):
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
            self.bg_rect.x = i * self.bg_width + self.scroll

        self.scroll -= 5

        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

    def run(self):
        clock = pygame.time.Clock()
        FPS = 60
        run = True
        while run:
            clock.tick(FPS)
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()

game = GameBackground(1500, 600)
game.run()
