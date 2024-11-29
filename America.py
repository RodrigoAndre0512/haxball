import pygame
import sys
def americano():
    pygame.init()

    ancho_pantalla, alto_pantalla = 1200, 600
    pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    pygame.display.set_caption("Juego de Touchdown")

    AZUL = (0, 0, 255)
    ROJO = (255, 0, 0)
    NEGRO = (0, 0, 0)
    CAFE = (139, 69, 19)
    imagen_cancha = pygame.image.load("Imagenes/cancha.jpg")
    rect_cancha = imagen_cancha.get_rect()

    x_cancha = (ancho_pantalla - rect_cancha.width) // 2
    y_cancha = (alto_pantalla - rect_cancha.height) // 2
    pos_jugador1 = [x_cancha + 50, y_cancha + rect_cancha.height // 2]
    pos_jugador2 = [x_cancha + rect_cancha.width - 50, y_cancha + rect_cancha.height // 2]
    pos_balón = pos_jugador1[:]
    radio_jugador = 20
    radio_balón = 10
    velocidad = 10
    puntaje1 = 0
    puntaje2 = 0
    fuente = pygame.font.Font(None, 48)

    jugador1_tiene_balón = True


    def dibujar_marcador():
        texto_puntaje1 = fuente.render(f"{puntaje1}", True, AZUL)
        texto_puntaje2 = fuente.render(f"{puntaje2}", True, ROJO)
        pantalla.blit(texto_puntaje1, (50, 10))
        pantalla.blit(texto_puntaje2, (ancho_pantalla - 50 - texto_puntaje2.get_width(), 10))
    def animaciones(pantalla, animacion):
        for frame in animacion:
            pantalla.blit(frame, (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)

    Campeon1 = []
    for j in range(1, 5): 
        frame = pygame.image.load("Imagenes/W8.png") 
        Campeon1.append(frame)
    Campeon2 = []
    for j in range(1, 5):  
        frame = pygame.image.load("Imagenes/W9.png") 
        Campeon2.append(frame)
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            pos_jugador1[1] -= velocidad
        if teclas[pygame.K_s]:
            pos_jugador1[1] += velocidad
        if teclas[pygame.K_a]:
            pos_jugador1[0] -= velocidad
        if teclas[pygame.K_d]:
            pos_jugador1[0] += velocidad


        if teclas[pygame.K_UP]:
            pos_jugador2[1] -= velocidad
        if teclas[pygame.K_DOWN]:
            pos_jugador2[1] += velocidad
        if teclas[pygame.K_LEFT]:
            pos_jugador2[0] -= velocidad
        if teclas[pygame.K_RIGHT]:
            pos_jugador2[0] += velocidad

        pos_jugador1[0] = max(x_cancha + radio_jugador, min(x_cancha + rect_cancha.width - radio_jugador, pos_jugador1[0]))
        pos_jugador1[1] = max(y_cancha + radio_jugador, min(y_cancha + rect_cancha.height - radio_jugador, pos_jugador1[1]))
        pos_jugador2[0] = max(x_cancha + radio_jugador, min(x_cancha + rect_cancha.width - radio_jugador, pos_jugador2[0]))
        pos_jugador2[1] = max(y_cancha + radio_jugador, min(y_cancha + rect_cancha.height - radio_jugador, pos_jugador2[1]))


        if jugador1_tiene_balón:
            pos_balón = pos_jugador1[:]
        else:
            pos_balón = pos_jugador2[:]

        distancia = ((pos_jugador1[0] - pos_jugador2[0]) ** 2 + (pos_jugador1[1] - pos_jugador2[1]) ** 2) ** 0.5
        if distancia < 2 * radio_jugador:
            pos_jugador1 = [x_cancha + 50, y_cancha + rect_cancha.height // 2]
            pos_jugador2 = [x_cancha + rect_cancha.width - 50, y_cancha + rect_cancha.height // 2]
            jugador1_tiene_balón = not jugador1_tiene_balón

        if jugador1_tiene_balón and pos_balón[0] >= x_cancha + rect_cancha.width - 100:
            puntaje1 += 1
            pos_jugador1 = [x_cancha + 50, y_cancha + rect_cancha.height // 2]
            pos_jugador2 = [x_cancha + rect_cancha.width - 50, y_cancha + rect_cancha.height // 2]
            jugador1_tiene_balón = False
        elif not jugador1_tiene_balón and pos_balón[0] <= x_cancha + 100:
            puntaje2 += 1
            pos_jugador1 = [x_cancha + 50, y_cancha + rect_cancha.height // 2]
            pos_jugador2 = [x_cancha + rect_cancha.width - 50, y_cancha + rect_cancha.height // 2]
            jugador1_tiene_balón = True
        if puntaje1 >= 3:
            animaciones(pantalla, Campeon2)
            ejecutando = False
        if puntaje2 >= 3:
            animaciones(pantalla, Campeon1)
            ejecutando = False
        pantalla.fill(NEGRO)
        pantalla.blit(imagen_cancha, (x_cancha, y_cancha))
        pygame.draw.circle(pantalla, AZUL, pos_jugador1, radio_jugador)
        pygame.draw.circle(pantalla, ROJO, pos_jugador2, radio_jugador)
        pygame.draw.circle(pantalla, CAFE, pos_balón, radio_balón)
        dibujar_marcador()
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    americano()