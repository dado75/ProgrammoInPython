import pygame
import sys
import time

size = 800, 500
width, height = size
ORANGE = (248, 177, 24)
GREEN = (0, 128, 0)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
dimpal = 38
lcorda = 30
priga = 500 - dimpal - lcorda
pcolonna = 100
vel = 0.03

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Palloncino in volo')
screen.fill(ORANGE)


def volo (vel, colorep, ccorda, sfondo):
        pygame.draw.circle(screen, colorep, (pcolonna, priga), dimpal)
        pygame.draw.line(screen, ccorda, (pcolonna, priga + dimpal), (pcolonna, priga + dimpal + lcorda))
        pygame.display.update()
        time.sleep(vel)
        screen.fill(sfondo)


# pygame.display.flip()
#volomov = volo(0.01, GREEN, NERO, ORANGE)
#volomov.rect = volomov.get_rect()

while True:
    while priga > 0 + dimpal:
        volo(0.001, NERO, GREEN, ORANGE)
        priga -= 1
    pcolonna += 50
    dimpal += 20
    while priga < 500 - dimpal:
        volo(0.001, GREEN, NERO, ORANGE)
        priga += 1
        # pcolonna -= 1
    # pygame.display.update()
    if __name__ == "__main__":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_ESCAPE:
            #        pygame.quit()
            #        sys.exit()
           # if event.type == pygame.KEYDOWN:
           #     if event.key == pygame.K_BACKSPACE:
