import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B

velocidadeRocket = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    rectRocket.move_ip(velocidadeRocket, 0)

    tela.fill(preto)
    tela.blit(imagemRocket, rectRocket)

    pygame.display.update()
