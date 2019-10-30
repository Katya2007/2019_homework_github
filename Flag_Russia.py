import pygame


def draw_flagpole():
    color = pygame.Color("bisque4")
    pygame.draw.rect(screen, color, (20, 20, 10, 200), 0)

def draw_red_flag():
    color = pygame.Color("firebrick1")
    pygame.draw.rect(screen, color, (26, 20, 130, 35*3), 0)
    print("I was painted over")

def draw_white_stripe():
    color = pygame.Color("cornsilk")
    pygame.draw.rect(screen, color, (26, 20, 130, 35), 0)

def draw_blue_stripe():
    color = pygame.Color("cornflowerblue")
    pygame.draw.rect(screen, color, (26, 55, 130, 35), 0)


pygame.init()
size = width, height = 200, 250
screen = pygame.display.set_mode(size)

draw_flagpole()
draw_red_flag()
draw_blue_stripe()
draw_white_stripe()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
