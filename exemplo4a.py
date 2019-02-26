import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()
rectRocket.move_ip(100, 200)
velocidade = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    rectRocket.move_ip(velocidade, 0)
    tela.fill((255, 0, 0))
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()
