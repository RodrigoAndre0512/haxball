import pygame
import time
import datetime
import sys
def penales():
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 600
    COLOR_PELOTA = (0, 0, 0) 
    RADIO = 15
    RADIO_PELOTA = 10
    FPS = 60
    VELOCIDAD = 2.5
    VELOCIDAD_PELOTA = 2
    FRICCION = 0.99  
 
    timer_duracion = datetime.timedelta(minutes=3, seconds=30)
    inicio_time = None


    LIMITE_IZQUIERDO_arquero = 1075
    LIMITE_DERECHO_arquero = 1150
    LIMITE_SUPERIOR_arquero = 200
    LIMITE_INFERIOR_arquero = 400
    LIMITE_IZQUIERDO_pateador = 600
    LIMITE_DERECHO_pateador = 1100
    LIMITE_SUPERIOR_pateador = 8
    LIMITE_INFERIOR_pateador = 587

    LIMITE_IZQUIERDO = 100
    LIMITE_DERECHO = 1100
    LIMITE_SUPERIOR = 8
    LIMITE_INFERIOR = 587

    ARCO_SUPERIOR = 200
    ARCO_INFERIOR = 400

    def reproducir_musica_principal(musica_principal):
        pygame.mixer.music.load(musica_principal)
        pygame.mixer.music.play(-1)

    def dibujo_tiempo(tiempo, pantalla):
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f'{tiempo}', True, (0, 0, 0))
        timer_react = timer_text.get_rect(topleft=(1100, 10))
        pantalla.blit(timer_text, timer_react)

    def reset_positions(personajes):
        posiciones_iniciales = [(800, 300), (1100, 300)]
        for i, personaje in enumerate(personajes):
            personaje.x, personaje.y = posiciones_iniciales[i]
            personaje.actualizar_centro()

    def animaciones(pantalla, animacion):
        for frame in animacion:
            pantalla.blit(frame, (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)

    class Personaje:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color 
            self.actualizar_centro()

        def actualizar_centro(self):
            self.rect = pygame.Rect(self.x, self.y, RADIO * 2, RADIO * 2)

        def dibujar(self, pantalla):
            pygame.draw.circle(pantalla, self.color, (self.x, self.y), RADIO)

        def movimiento(self, delta_x, delta_y, otros_personajes):

            prev_x = self.x
            prev_y = self.y


            self.x += delta_x
            self.y += delta_y


            self.x = max(LIMITE_IZQUIERDO + RADIO, min(self.x, LIMITE_DERECHO - RADIO))
            self.y = max(LIMITE_SUPERIOR + RADIO, min(self.y, LIMITE_INFERIOR - RADIO))

            self.actualizar_centro()


            for personaje in otros_personajes:
                if personaje != self and self.colisiona(personaje):

                    self.x = prev_x
                    self.y = prev_y
                    self.actualizar_centro()
                    break

        def colisiona(self, otro_personaje):
            distancia = ((self.x - otro_personaje.x) ** 2 + (self.y - otro_personaje.y) ** 2) ** 0.5
            return distancia < 2 * RADIO

    class Pateador(Personaje):
        def __init__(self, x, y, color):
            super().__init__(x, y, color)  

        def movimiento(self, delta_x, delta_y, otros_personajes):
            prev_x = self.x
            prev_y = self.y

            self.x += delta_x
            self.y += delta_y

            self.x = max(LIMITE_IZQUIERDO_pateador + RADIO, min(self.x, LIMITE_DERECHO_pateador - RADIO))
            self.y = max(LIMITE_SUPERIOR_pateador + RADIO, min(self.y, LIMITE_INFERIOR_pateador - RADIO))

            self.actualizar_centro()

            for personaje in otros_personajes:
                if personaje != self and self.colisiona(personaje):
                    self.x = prev_x
                    self.y = prev_y
                    self.actualizar_centro()
                    break

    class Arquero(Personaje):
        def __init__(self, x, y, color):
            super().__init__(x, y, color) 
        def movimiento(self, delta_x, delta_y, otros_personajes):
            prev_x = self.x
            prev_y = self.y

            self.x += delta_x
            self.y += delta_y

            self.x = max(LIMITE_IZQUIERDO_arquero + RADIO, min(self.x, LIMITE_DERECHO_arquero - RADIO))
            self.y = max(LIMITE_SUPERIOR_arquero + RADIO, min(self.y, LIMITE_INFERIOR_arquero - RADIO))

            self.actualizar_centro()

            for personaje in otros_personajes:
                if personaje != self and self.colisiona(personaje):
                    self.x = prev_x
                    self.y = prev_y
                    self.actualizar_centro()
                    break

    class Pelota:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.vx = 0
            self.vy = 0
            self.actualizar_centro()
            self.tiempo_detencion = pygame.time.get_ticks()

        def actualizar_centro(self):
            self.center = (self.x, self.y)

        def dibujar(self, interfaz):
            pygame.draw.circle(interfaz, COLOR_PELOTA, self.center, RADIO_PELOTA)

        def movimiento(self, personajes):
            self.vx *= FRICCION
            self.vy *= FRICCION

            self.x += self.vx
            self.y += self.vy

            if self.x < LIMITE_IZQUIERDO + RADIO_PELOTA and not (ARCO_SUPERIOR < self.y < ARCO_INFERIOR):
                self.vx = -self.vx
                self.x = LIMITE_IZQUIERDO + RADIO_PELOTA
            if self.x > LIMITE_DERECHO - RADIO_PELOTA and not (ARCO_SUPERIOR < self.y < ARCO_INFERIOR):
                self.vx = -self.vx
                self.x = LIMITE_DERECHO - RADIO_PELOTA
            if self.y < LIMITE_SUPERIOR + RADIO_PELOTA:
                self.vy = -self.vy
                self.y = LIMITE_SUPERIOR + RADIO_PELOTA
            if self.y > LIMITE_INFERIOR - RADIO_PELOTA:
                self.vy = -self.vy
                self.y = LIMITE_INFERIOR - RADIO_PELOTA

            self.actualizar_centro()

            for personaje in personajes:
                if self.colisiona(personaje):
                    self.vx = (self.x - personaje.x) / RADIO * VELOCIDAD_PELOTA
                    self.vy = (self.y - personaje.y) / RADIO * VELOCIDAD_PELOTA
                    self.tiempo_detencion = pygame.time.get_ticks()

            if abs(self.vx) < 0.1 and abs(self.vy) < 0.1:
                self.vx = 0
                self.vy = 0
            global Marcador_equipo_1, Marcador_equipo_2, jugando
            if self.x <= LIMITE_IZQUIERDO - RADIO_PELOTA and (ARCO_SUPERIOR < self.y < ARCO_INFERIOR):
                Marcador_equipo_2 += 1
                animaciones(pantalla, animacion_gol)
                self.reset_position(personajes)
            elif self.x >= LIMITE_DERECHO + RADIO_PELOTA and (ARCO_SUPERIOR < self.y < ARCO_INFERIOR):
                Marcador_equipo_1 += 1
                animaciones(pantalla, animacion_gol)
                self.reset_position(personajes)

            arquero = personajes[1]
            if arquero.colisiona(self):
                animaciones(pantalla, Campeon2) 
                reset_positions(personajes)
                jugando = False


        def colisiona(self, personaje):
            distancia = ((self.x - personaje.x) ** 2 + (self.y - personaje.y) ** 2) ** 0.5
            return distancia < RADIO + RADIO_PELOTA

        def reset_position(self, personajes):
            self.x = 850
            self.y = 300
            self.vx = 0
            self.vy = 0
            self.actualizar_centro()
            reset_positions(personajes)


    global Marcador_equipo_1, Marcador_equipo_2,jugando
    Marcador_equipo_1 = 0
    Marcador_equipo_2 = 0
    jugando = True
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("HAXBALL")
    pantalla_cancha = pygame.image.load("Imagenes/cancha_3.png").convert()
    musica_principal = 'Sonido/sonido_6.mp3'  
    reproducir_musica_principal(musica_principal)
    reloj = pygame.time.Clock()

    marcador = pygame.image.load("Imagenes/123.png")
    marcador = pygame.transform.scale(marcador, (110, 100))
    posicion_marcador = (0, 0)
    start_time = time.time()

    personajes = [Pateador(800, 300, (255, 0, 0)), Arquero(1100, 300, (0, 0, 255))]
    pelota = Pelota(850, 300)
    font_title = pygame.font.Font(None, 90)
    font_title1 = pygame.font.Font(None, 90)

    animacion_gol = []
    for i in range(1, 5):  
        frame = pygame.image.load("Imagenes/Gol.png")  
        animacion_gol.append(frame)
    Campeon1 = []
    for j in range(1, 5):  
        frame = pygame.image.load("Imagenes/W7.png") 
        Campeon1.append(frame)
    Campeon2 = []
    for h in range(1, 5):  
        frame = pygame.image.load("Imagenes/W8.png")  
        Campeon2.append(frame)
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
        tiempo_transcurrido = time.time() - start_time
        tiempo_restante = timer_duracion - datetime.timedelta(seconds=int(tiempo_transcurrido))
        if tiempo_restante.total_seconds() <= 0:
            if Marcador_equipo_1 == Marcador_equipo_2:
                print("penales")
            elif Marcador_equipo_1 <= Marcador_equipo_2:
                animaciones(pantalla, Campeon2)
                jugando = False
            elif Marcador_equipo_1 >= Marcador_equipo_2:
                animaciones(pantalla, Campeon1)
                jugando = False
        if Marcador_equipo_2 >= 3:
            animaciones(pantalla, Campeon2)
            jugando = False
        elif Marcador_equipo_1 >= 3:
            animaciones(pantalla, Campeon1)
            jugando = False
        teclas = pygame.key.get_pressed()

        delta_x_1 = 0
        delta_y_1 = 0
        if teclas[pygame.K_LEFT]:
            delta_x_1 = -VELOCIDAD
        if teclas[pygame.K_RIGHT]:
            delta_x_1 = VELOCIDAD
        if teclas[pygame.K_UP]:
            delta_y_1 = -VELOCIDAD
        if teclas[pygame.K_DOWN]:
            delta_y_1 = VELOCIDAD
        if teclas[pygame.K_SPACE]:
            if personajes[1].colisiona(pelota):
                pelota.vx *= 2
                pelota.vy *= 2
        personajes[1].movimiento(delta_x_1, delta_y_1, personajes)

   
        delta_x_2 = 0
        delta_y_2 = 0
        if teclas[pygame.K_a]:
            delta_x_2 = -VELOCIDAD
        if teclas[pygame.K_d]:
            delta_x_2 = VELOCIDAD
        if teclas[pygame.K_w]:
            delta_y_2 = -VELOCIDAD
        if teclas[pygame.K_s]:
            delta_y_2 = VELOCIDAD
        if teclas[pygame.K_q]:
            if personajes[0].colisiona(pelota):
                pelota.vx *= 2
                pelota.vy *= 2
        personajes[0].movimiento(delta_x_2, delta_y_2, personajes)


        pelota.movimiento(personajes)


        title_text = font_title.render(str(Marcador_equipo_1), True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(80, 27))
        title_text1 = font_title1.render(str(Marcador_equipo_2), True, (255, 255, 255))
        title_rect1 = title_text1.get_rect(center=(80, 77))

        pantalla.blit(pantalla_cancha, [0, 0])
        pantalla.blit(marcador, posicion_marcador)
        pantalla.blit(title_text, title_rect)
        pantalla.blit(title_text1, title_rect1)
        for personaje in personajes:
            personaje.dibujar(pantalla)
        pelota.dibujar(pantalla)
        dibujo_tiempo(str(tiempo_restante), pantalla)
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    penales()