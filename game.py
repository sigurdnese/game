import pygame

pygame.init()

display_width = 1024
display_height = 768

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

# sprite size
sprite_width = 48
sprite_height = 96

charImg = pygame.image.load('char.png')
charImg = pygame.transform.scale(charImg, (sprite_width, sprite_height))

# char size
char_width = 48
char_height = 96

charImg_rect = charImg.get_rect()

def char(x, y, orientation):
    if orientation == "right":
        gameDisplay.blit(charImg,(x,y))
    else:
        gameDisplay.blit(pygame.transform.flip(charImg, True, False),(x,y))

x = (display_width * 0.45)
y = (display_height - sprite_height)

x_change = 0
y_change = 0

#jump bool
jumping = False

#character orientation
char_orientation = "right"

crashed = False

while not crashed:

    # bounds check
    if y >= (display_height - char_height):
        jumping = False
        y_change = 0
        y = display_height - char_height

    if x >= (display_width - sprite_width):
        x = display_width - sprite_width

    if x < 0:
        x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += -5
                char_orientation = "left"
            if event.key == pygame.K_RIGHT:
                x_change += 5
                char_orientation = "right"
            if event.key == pygame.K_UP and jumping == False:
                y_change += -8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change += 5
            if event.key == pygame.K_RIGHT:
                x_change += -5

    # x movement
    x += x_change

    # y movement
    if y < (display_height - char_height):
        jumping = True
        y_change += 0.4

    y += y_change

    gameDisplay.fill((100,100,255))
    char(x, y, char_orientation)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
