import sys
import pygame
from skysettings import SkySettings

def run_game():
    pygame.init()
    screen_settings = SkySettings()
    screen = pygame.display.set_mode((screen_settings.screen_width,screen_settings.screen_height))
    pygame.display.set_caption("SKY")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(screen_settings.screen_color)
        pygame.display.flip()

run_game()