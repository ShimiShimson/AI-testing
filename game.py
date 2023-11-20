import pygame

# initialize Pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# set the background color
screen.fill((255, 255, 255))

# draw some shapes on the screen
pygame.draw.rect(screen, (0, 0, 255), (100, 100, 300, 200))
pygame.draw.circle(screen, (0, 0, 255), (400, 400, 50))

# update the screen
pygame.display.update()

# quit Pygame
pygame.quit()