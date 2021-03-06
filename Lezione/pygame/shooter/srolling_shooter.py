import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
size = SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((size))
pygame.display.set_caption('Samuel')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variable
moving_left = False
moving_right = False
#define colours
BG = (144, 201, 120)
def draw_bg():
    screen.fill(BG)


class Animal(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(3):
            img = pygame.image.load(f'img/{self.char_type}/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0
        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.frame_index]

        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0



    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Animal('player', 400, 200, 0.5, 5)
enemy = Animal('enemy', 200, 200, 0.1, 5)
#player3 = Animal(600,200, 1)

while True:
       if __name__ == "__main__" :
        pygame.display.update()
        clock.tick(FPS)
        draw_bg()
        player.draw()
        enemy.update_animation()
        enemy.draw()
        #player2.draw()
        #player3.draw()

        #player.move(moving_left, moving_right)
        enemy.move(moving_left, moving_right)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #keyboard pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #keybord released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False


