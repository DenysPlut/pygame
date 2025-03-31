import pygame

MAX_X = 800
MAX_Y = 600
game_over = False

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My first pygame game! :")

myimage = pygame.image.load("intel-i9-3.webp").convert()

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_over = True

    screen.blit(myimage,(100, 100))
    pygame.display.flip()

