import pygame
pygame.init()
screen = pygame.display.set_mode((1000,800))
while True:
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            print(event.key)