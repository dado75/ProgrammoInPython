import pygame
import sys
import time
size = 500, 500
width, height = size
ORANGE = (248, 177, 24)
GREEN = (0, 128, 0)
NERO = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(ORANGE)

pygame.draw.circle(screen, GREEN, (250, 350), 50)
pygame.draw.line(screen, GREEN, (250, 350), (250, 480), 2)
pygame.display.update()
time.sleep(0.30)
screen.fill(ORANGE)

pygame.draw.circle(screen, GREEN, (250, 250), 50)
pygame.draw.line(screen, GREEN, (250, 250), (250, 380), 2)
pygame.display.update()
time.sleep(0.30)
screen.fill(ORANGE)

pygame.draw.circle(screen, GREEN, (250, 150), 50)
pygame.draw.line(screen, GREEN, (250, 150), (250, 280), 2)
pygame.display.update()
time.sleep(0.30)
screen.fill(ORANGE)

#pygame.draw.ellipse(screen,(GREEN), (200,150,100,50), 3)
#pygame.draw.line(screen,(GREEN), (200,250), (400,250), 3)
#pygame.draw.lines(screen,(GREEN), (200,250), (300,300), 3)

#while RIGA < 300:
#    pygame.draw.line(screen,(GREEN),(50,RIGA),(200,RIGA), 1)
#    RIGA += 1


#    time.sleep(0.1)



pygame.display.update()

while True:
    if __name__ == "__main__" :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
