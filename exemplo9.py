import pygame
import random
import Pyro4

pygame.init()
clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600))
#Um objeto font é necessário para escrever valores na HUD do jogo
fonte = pygame.font.SysFont("arial", 40)

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

imagemLaser = pygame.image.load("Spacepack/LaserBeam.png")
imagemLaser = pygame.transform.scale(imagemLaser, (100,100))
rectLaser = imagemLaser.get_rect()

imagemUFO = pygame.image.load("Spacepack/UFOBoss.png")
imagemUFO = pygame.transform.scale(imagemUFO, (200, 200))
rectUFO = imagemUFO.get_rect()
rectUFO = rectUFO.move(400, 300)

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
velocidadeRocket = 5
velocidadeLaser = 18
atirou = False
pontos = 0

#Obtendo referência remota do inimigo
inimigoRemoto = Pyro4.Proxy("PYRONAME:capirotauro")

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Controle de disparos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and atirou == False:
                atirou = True
                rectLaser.x = rectRocket.x + 100
                rectLaser.y = rectRocket.y
    #Movimentação do personagem
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectRocket.move_ip(velocidadeRocket, 0)
    if tecla[pygame.K_a]:
        rectRocket.move_ip(-velocidadeRocket, 0)
    if tecla[pygame.K_w]:
        rectRocket.move_ip(0, -velocidadeRocket)
    if tecla[pygame.K_s]:
        rectRocket.move_ip(0, velocidadeRocket)

    #Desenho do background
    tela.fill(preto)

        
    #Desenhar os sprites do player e do inimigo (sempre)
    tela.blit(imagemRocket, rectRocket)
    tela.blit(imagemUFO, rectUFO)
    
    
    #Lógica para tratar a exibição dos disparos na tela
    if atirou == True:
        #Movimentar o disparo na tela
        rectLaser.move_ip (velocidadeLaser, 0)
        #Teste para determinar se o disparo deve ser eliminado 
        if rectLaser.left > tela.get_width():
            atirou = False
        #Desenho do disparo (apenas realizado quando houver disparo
        tela.blit(imagemLaser, rectLaser)

    #Tratamento de colisão do disparo com um inimigo
    if rectLaser.colliderect(rectUFO):
        
        #Retirar o disparo da tela, movendo-o para uma posição externa "segura"
        #rectLaser = rectLaser.move (1000, 1000) 

        #Sortear uma nova posicao para o inimigo
        #novoX = random.randint(100, 600)
        #novoY = random.randint(100, 400)

        #Modificar as coordenadas de posicao do inimigo        
        #rectUFO.x = novoX
        #rectUFO.y = novoY
        
        #Computar os pontos para o player
        pontos += 100
        inimigoRemoto.levar_dano(10)
        

    
    #Desenhar a HUD
    score = fonte.render ("Score: " + str(pontos), True, (255, 255, 255))
    tela.blit(score, (10,5))
    
    pygame.display.update()
    clock.tick(60)









    
