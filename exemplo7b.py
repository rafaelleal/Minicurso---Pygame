import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
background = pygame.image.load("space.jpg").convert()
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

rectRocket = rectRocket.move(pygame.mouse.get_pos())

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
velocidadeRocket = 10

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.blit(background, (0,0))
    #tela.blit(imagemRocket, pygame.mouse.get_pos())

    x, y = pygame.mouse.get_pos()
    tela.blit(imagemRocket, (x - 100, y - 50))

    pygame.display.update()
    clock.tick(30) #30 FPS






