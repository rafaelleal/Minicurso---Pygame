import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
background = pygame.image.load("space.jpg").convert()
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()
preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
velocidadeRocket = 10
while True: #Game Loop
    
    for event in pygame.event.get(): #Event Loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rectRocket.move_ip(velocidadeRocket, 0)
            if event.key == K_a:
                rectRocket.move_ip(-velocidadeRocket, 0)
            if event.key == K_w:
                rectRocket.move_ip(0, -velocidadeRocket)
            if event.key == K_s:
                rectRocket.move_ip(0, velocidadeRocket)
    

    tela.blit(background, (0,0))
    tela.blit(imagemRocket, rectRocket)

    pygame.display.update()
    clock.tick(30) #30 FPS
