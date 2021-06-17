import pygame
import sys
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
size = SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Giochino")
# attiva ripetizione
pygame.key.set_repeat(300, 30)

# Variabili
loop = True
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
mago = pygame.image.load("0.png")
x = (SCREEN_WIDTH * 0.5)
y = (SCREEN_HEIGHT * 0.5)
scale = 1
dx = 0
dy = 0

#Definisci le funzioni

def Draw(x, y):
    screen.blit(mago, (x, y))
#screen.fill(white)

# Gioco
while loop == True:
    if __name__ == "__main__":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = 2
                elif event.key == pygame.K_LEFT:
                    dx = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    dx = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy = -2
                elif event.key == pygame.K_DOWN:
                    dy = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy = 0

           #print(event)
        #screen.fill(white)
        x = x + dx
        y = y + dy
        Draw(x, y)

        pygame.display.flip()
        screen.fill(white)
        #pygame.display.update()


