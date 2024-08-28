import pygame
import sys

pygame.init()

PANTALLA = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Aventura marina')

BLANCO = (255, 255, 255)
PANTALLA.fill(BLANCO)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()