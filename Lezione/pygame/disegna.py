import pygame
import sys
import time
size = 500, 500
width, height = size
#width = 800
#height = 400
ORANGE = (248, 177, 24)
GREEN = (0, 128, 0)
RIGA = 100

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(GREEN)
"""pygame.draw.circle(screen,(ORANGE),(200, 400), 25, 2)
#pygame.draw.circle(screen,(GREEN),(200,250),25, 5)
pygame.draw.ellipse(screen, (ORANGE), (250, 250, 100, 200))
pygame.draw.line(screen,(ORANGE), (250, 250), (350, 250))
pygame.draw.line(screen,(ORANGE), (250, 250), (250, 450))
#pygame.draw.line(screen,(ORANGE), (200,250), (300,300), 2)
pygame.draw.rect(screen, (ORANGE), (25, 60, 100, 50))
pygame.draw.rect(screen, (ORANGE), (25, 60, 200, 100), 2)
pygame.draw.rect(screen, (ORANGE), pygame.Rect(60, 190, 200, 50), 1, 10) """

while RIGA < 300:
    pygame.draw.line(screen,(ORANGE),(50,RIGA),(200,RIGA), 1)
    RIGA += 1
    time.sleep(0.1)
#pygame.draw.line(screen,(GREEN),(200,100),(200,300), 3)
#pygame.draw.line(screen,(GREEN),(200,300),(50,300), 3)
#pygame.draw.line(screen,(GREEN),(50,300),(50,100), 3)





    pygame.display.update()

while True:
    if __name__ == "__main__" :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
