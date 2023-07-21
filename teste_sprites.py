import pygame
from sys import exit
from pygame.locals import *

pygame.init()
posição_x = 640
posição_y = 480
tela = pygame.display.set_mode((posição_x, posição_y))
pygame.display.set_caption('sprites')
relogio = pygame.time.Clock()

pos_x = 300
pos_y = 200

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/m_cam_0.png'))
        self.sprites.append(pygame.image.load('sprites/m_cam_1.png'))
        self.sprites.append(pygame.image.load('sprites/m_cam_2.png'))        
        # self.sprites.append(pygame.image.load('sprites/m_pulando.png'))
        # self.sprites.append(pygame.image.load('sprites/m_baixo.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (15*3, 32*3))
        

        self.rect = self.image.get_rect()
        self.rect.topleft = pos_x, pos_y

        self.animar = False

    def andar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (15*3, 32*3))


todas_sprites = pygame.sprite.Group()
mario = Mario()
todas_sprites.add(mario)

while True:
    relogio.tick(30)
    tela.fill((0,0,0))    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            mario.andar()

    todas_sprites.draw(tela)
    todas_sprites.update()

    if pygame.key.get_pressed()[K_RIGHT]:
        pos_x = pos_x + 20
    if pygame.key.get_pressed()[K_LEFT]:
        pos_x = pos_x - 20
            

   
  
    pygame.display.flip()
