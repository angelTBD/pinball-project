import pygame
from random import randint

pygame.init()
#inicializamos la ventana del juego
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pin Ball')

#bucle principal del juego
jugando=True
while jugando:
    #comprobamos los eventos
    #comprobamos si se ha pulsado el boton de cierre de ventana
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            jugando = False
    #se pinta la ventana de un color
    #esto borra los posibles elementos anteriores
    ventana.fill((255,255,255))
    #todos los elementos se vuelven a dibujar
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()