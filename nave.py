import pygame
from sys import exit
from pygame.locals import *

pygame.init()
posição_x = 1180
posição_y = 710
tela = pygame.display.set_mode((posição_x, posição_y))
pygame.display.set_caption('Galaga')
relogio = pygame.time.Clock()
#running = True

#Importe imagens
import_play1 = pygame.image.load('Imagens/1.png')
import_tiro = pygame.image.load('Imagens/tiro.png')
bg = pygame.image.load('Imagens/Stars.png')

posx_play1 = 590
posy_play1 = 550

#Tamanho imagens
play1 = pygame.transform.scale(import_play1, (75, 75))
tiro = pygame.transform.scale(import_tiro, (75, 75))

while True:
    relogio.tick(30)
    tela.fill((0,0,0))    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_UP]:
        posy_play1 = posy_play1 - 20
    if pygame.key.get_pressed()[K_DOWN]:
        posy_play1 = posy_play1 + 20
    if pygame.key.get_pressed()[K_RIGHT]:
        posx_play1 = posx_play1 + 20
    if pygame.key.get_pressed()[K_LEFT]:
        posx_play1 = posx_play1 - 20
            


    
    #tela.blit(bg, (0, 0))
    tela.blit(play1, (posx_play1, posy_play1))
    tela.blit(tiro, (posx_play1, posy_play1))
  
    pygame.display.update()

    #relogio.tick(60)

pygame.quit()
