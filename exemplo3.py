import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()