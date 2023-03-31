import pygame
pygame.init()
monitor = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PP2 PYGAME')
pygame.display.set_icon(pygame.image.load('nike.jpg'))
check = True
square = pygame.Surface((60, 200))
while check:
    monitor.fill((177, 252, 3))
    monitor.blit(square, (50 ,50))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()