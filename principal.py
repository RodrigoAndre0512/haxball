import pygame
import sys 
from videojueog import futbol
from backend import penales
from America import americano
ANCHO=1200
ALTO=600
pygame.init()
pygame.display.set_caption("haxball")
principal=pygame.display.set_mode((ANCHO,ALTO))
pantalla=pygame.image.load("Imagenes/defiw.png").convert()
pygame.mixer.music.load('Sonido/Euro.mp3')
pygame.mixer.music.play(1)
inicio=False
class Boton:
    def __init__(self, texto, pos, fuente, base_color, resaltado_color):
        self.texto_input = texto
        self.fuente = fuente
        self.base_color = base_color
        self.resaltado_color = resaltado_color
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.text = self.fuente.render(self.texto_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def actualizar(self, screen):
        screen.blit(self.text, self.rect)

    def comprobar(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def cambio_de_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.fuente.render(self.texto_input, True, self.resaltado_color)
        else:
            self.text = self.fuente.render(self.texto_input, True, self.base_color)

fuente_boton = pygame.font.Font(None, 74)
fuente_titulo = pygame.font.Font(None, 50)
haxball = pygame.image.load("Imagenes/haxball.png")
haxball = pygame.transform.scale(haxball, (450, 120))
posicion_haxball1=(400,50)
futbol_boton = Boton(texto="Futbol", pos=(600, 300), fuente=fuente_boton , base_color="Black", resaltado_color="Red")
penales_boton = Boton(texto="Penales", pos=(600, 400), fuente=fuente_boton , base_color="Black", resaltado_color="Red")
america_boton = Boton(texto="Futbol americano", pos=(600, 500), fuente=fuente_boton , base_color="Black", resaltado_color="Red")
titulo = fuente_titulo.render("¿Qué modo de juego quieres jugar?", True, "White")
title_rect = titulo.get_rect(center=(600, 200))

while not inicio:
  mouse_pos = pygame.mouse.get_pos()
  pantalla.blit(titulo, title_rect)
  for boton in [futbol_boton, penales_boton, america_boton]:
        boton.cambio_de_color(mouse_pos)
        boton.actualizar(pantalla)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      inicio = True
    if event.type == pygame.MOUSEBUTTONDOWN:
            if futbol_boton.comprobar(mouse_pos):
                futbol()
            if penales_boton.comprobar(mouse_pos):
                penales()
            if america_boton.comprobar(mouse_pos):
                americano()
  principal.blit(pantalla, [0,0])
  principal.blit(haxball, posicion_haxball1)
  pygame.display.flip()


pygame.quit()

