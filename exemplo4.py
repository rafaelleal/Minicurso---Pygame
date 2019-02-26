import pygame
pygame.init()
tela = pygame.display.set_mode((800,600))

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100) )

rectRocket = imagemRocket.get_rect()

rectRocket.move_ip(100, 200)

while True: #Game Loop
    #Update - modificar os dados dos componentes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #Drawing - desenhar os componentes na tela
    tela.fill( (0,0,50) )
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()
