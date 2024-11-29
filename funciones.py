import pygame
import sys
from cancha import champions_1
from cancha import champions_2
from cancha import libertadores_1
from cancha import libertadores_2
from cancha import mundial_1
from cancha import mundial_2
def Champions_League():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("HAXBALL")
    pantalla = pygame.image.load("Imagenes/champions.jpg").convert()
    pygame.mixer.music.load('Sonido/sonido_2.mp3')
    pygame.mixer.music.play(1)
    class Boton2:
        def __init__(self, imagen, pos, texto_input, fuente, base_color, resaltado_color):
            self.imagen = imagen
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.fuente = fuente
            self.base_color = base_color
            self.resaltado_color = resaltado_color
            self.texto_input = texto_input
            self.text = self.fuente.render(self.texto_input, True, self.base_color)
            if self.imagen is not None:
                self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
            else:
                self.rect = pygame.Rect(self.x_pos - 100, self.y_pos - 25, 200, 50)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.imagen is not None:
                screen.blit(self.imagen, self.rect)
            screen.blit(self.text, self.text_rect)

        def check_for_input(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                return True
            return False

        def change_color(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                self.text = self.fuente.render(self.texto_input, True, self.resaltado_color)
            else:
                self.text = self.fuente.render(self.texto_input, True, self.base_color)

    equipo1_imagen = pygame.image.load("imagenes/logo3.png")
    equipo2_imagen = pygame.image.load("imagenes/logo2.png")

    font_title = pygame.font.Font(None, 50)
    team1_imagen = pygame.transform.scale(equipo1_imagen, (110, 160))
    team2_imagen = pygame.transform.scale(equipo2_imagen, (140, 150))

    fuente = pygame.font.Font(None, 50)
    titulo = font_title.render("¿Qué equipo quieres jugar?", True, "White")
    title_rect = titulo.get_rect(center=(600, 100))

    boton1 = Boton2(imagen=team1_imagen, pos=(400, 300), texto_input=".", fuente=fuente, base_color="Yellow", resaltado_color="Green")
    boton2 = Boton2(imagen=team2_imagen, pos=(800, 300), texto_input=".", fuente=fuente, base_color="White", resaltado_color="Green")
    atras_boton = Boton2(imagen=None, pos=(600, 550), texto_input="Atrás", fuente=fuente, base_color="White", resaltado_color="Red")

    while True:
        screen.blit(pantalla, [0, 0])
        screen.blit(titulo, title_rect)
        mouse_pos = pygame.mouse.get_pos()

        for button in [boton1, boton2, atras_boton]:
            button.change_color(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton1.check_for_input(mouse_pos):
                    champions_1()
                if boton2.check_for_input(mouse_pos):
                    champions_2()
                if atras_boton.check_for_input(mouse_pos):
                    return 

        pygame.display.update()
def Copa_Libertadores():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Seleccionar Equipo de Fútbol")
    pantalla=pygame.image.load("Imagenes/copa.jpg").convert()
    pygame.mixer.music.load('Sonido/sonido_3.mp3')
    pygame.mixer.music.play(1)
    class Boton2:
        def __init__(self, imagen, pos, texto_input, fuente, base_color, resaltado_color):
            self.imagen = imagen
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.fuente = fuente
            self.base_color = base_color
            self.resaltado_color = resaltado_color
            self.texto_input = texto_input
            self.text = self.fuente.render(self.texto_input, True, self.base_color)
            if self.imagen is not None:
                self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
            else:
                self.rect = pygame.Rect(self.x_pos - 100, self.y_pos - 25, 200, 50)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.imagen is not None:
                screen.blit(self.imagen, self.rect)
            screen.blit(self.text, self.text_rect)

        def check_for_input(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                return True
            return False

        def change_color(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                self.text = self.fuente.render(self.texto_input, True, self.resaltado_color)
            else:
                self.text = self.fuente.render(self.texto_input, True, self.base_color)
    equipo1_imagen = pygame.image.load("imagenes/river.png")
    equipo2_imagen = pygame.image.load("imagenes/flamen.png")

    font_title = pygame.font.Font(None, 50)
    team1_imagen = pygame.transform.scale(equipo1_imagen, (140, 150))
    team2_imagen = pygame.transform.scale(equipo2_imagen, (120, 150))


    fuente = pygame.font.Font(None, 50)
    titulo = font_title.render("¿Qué equipo quieres jugar?", True, "White")
    title_rect = titulo.get_rect(center=(600, 100))
    button1 = Boton2(imagen=team1_imagen, pos=(400, 300), texto_input=".", fuente=fuente, base_color="Black", resaltado_color="Green")
    button2 = Boton2(imagen=team2_imagen, pos=(800, 300), texto_input=".", fuente=fuente, base_color="Black", resaltado_color="Green")
    atras_boton = Boton2(imagen=None, pos=(600, 550), texto_input="Atrás", fuente=fuente, base_color="White", resaltado_color="Red")

    while True:
        screen.blit(pantalla, [0,0])
        screen.blit(titulo, title_rect)
        mouse_pos = pygame.mouse.get_pos()
        for button in [button1, button2,atras_boton]:
            button.change_color(mouse_pos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.check_for_input(mouse_pos):
                    libertadores_1()
                if button2.check_for_input(mouse_pos):
                    libertadores_2()
                if atras_boton.check_for_input(mouse_pos):
                    return  
        pygame.display.update()
def Mundial():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Seleccionar Equipo de Fútbol")
    pantalla=pygame.image.load("Imagenes/mundi.png").convert()
    pygame.mixer.music.load('Sonido/sonido_4.mp3')
    pygame.mixer.music.play(1)
    class Boton2:
        def __init__(self, imagen, pos, texto_input, fuente, base_color, resaltado_color):
            self.imagen = imagen
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.fuente = fuente
            self.base_color = base_color
            self.resaltado_color = resaltado_color
            self.texto_input = texto_input
            self.text = self.fuente.render(self.texto_input, True, self.base_color)
            if self.imagen is not None:
                self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
            else:
                self.rect = pygame.Rect(self.x_pos - 100, self.y_pos - 25, 200, 50)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.imagen is not None:
                screen.blit(self.imagen, self.rect)
            screen.blit(self.text, self.text_rect)

        def check_for_input(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                return True
            return False

        def change_color(self, position):
            if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
                self.text = self.fuente.render(self.texto_input, True, self.resaltado_color)
            else:
                self.text = self.fuente.render(self.texto_input, True, self.base_color)
    equipo1_imagen = pygame.image.load("imagenes/aleman.png")
    equipo2_imagen = pygame.image.load("imagenes/brazil.png")

    font_title = pygame.font.Font(None, 50)
    team1_imagen = pygame.transform.scale(equipo1_imagen, (140, 150))
    team2_imagen = pygame.transform.scale(equipo2_imagen, (120, 150))


    fuente = pygame.font.Font(None, 50)
    titulo = font_title.render("¿Qué equipo quieres jugar?", True, "White")
    title_rect = titulo.get_rect(center=(600, 100))
    boton1 = Boton2(imagen=team1_imagen, pos=(400, 300), texto_input=".", fuente=fuente, base_color="Red", resaltado_color="Green")
    boton2 = Boton2(imagen=team2_imagen, pos=(800, 300), texto_input=".", fuente=fuente, base_color="Dark Blue", resaltado_color="Green")
    atras_boton = Boton2(imagen=None, pos=(600, 550), texto_input="Atrás", fuente=fuente, base_color="White", resaltado_color="Red")

    while True:
        screen.blit(pantalla, [0,0])
        screen.blit(titulo, title_rect)
        mouse_pos = pygame.mouse.get_pos()
        for button in [boton1, boton2,atras_boton]:
            button.change_color(mouse_pos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton1.check_for_input(mouse_pos):
                    libertadores_1()
                if boton2.check_for_input(mouse_pos):
                    libertadores_2()
                if atras_boton.check_for_input(mouse_pos):
                    return  
        pygame.display.update()