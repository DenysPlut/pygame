import pygame

MAX_X = 1366
MAX_Y = 768
IMG_SIZE = 100

game_over = False
bg_color = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My first pygame game! :")

myimage = pygame.image.load("intel-i9-3.webp").convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE,IMG_SIZE))

x = 500
y = 100

move_right = False
move_left = False
move_up = False
move_down = False


while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        if x > MAX_X-IMG_SIZE:
            x = MAX_X-IMG_SIZE

    if move_up == True:
        y -= 1
        if y < 0:
            y = 0

    if move_down == True:
        y += 1
        if y > MAX_Y-IMG_SIZE:
            y = MAX_Y-IMG_SIZE




    screen.fill(bg_color)
    screen.blit(myimage,(x, y))
    pygame.display.flip()

