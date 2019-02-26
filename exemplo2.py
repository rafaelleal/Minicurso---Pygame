import pygame
pygame.init()
tela = pygame.display.set_mode((1024, 768))

cor = (80, 60, 70)

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.fill(cor)        
    pygame.display.update()
