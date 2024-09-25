import pygame  # Importa el módulo pygame para manejar gráficos y eventos.
from personaje import Cubo  # Importa la clase Cubo desde el archivo 'personaje.py'.

# Definir el tamaño de la ventana.
ANCHO = 1000  # Ancho de la ventana.
ALTO = 800  # Alto de la ventana.
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Crea la ventana del juego con las dimensiones especificadas.

# Inicializa variables del juego.
jugando = True  # Bandera para controlar el bucle del juego.
cubo = Cubo(100, 100)  # Crea una instancia de la clase Cubo en la posición (100, 100).

# Función para gestionar el movimiento del cubo mediante las teclas W, A, S, D.
def gestionar_teclas(teclas):
    # Si se presiona 'W', el cubo se mueve hacia arriba.
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad  # Reduce la coordenada Y para mover el cubo hacia arriba.
    # Si se presiona 'S', el cubo se mueve hacia abajo.
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad  # Aumenta la coordenada Y para mover el cubo hacia abajo.
    # Si se presiona 'A', el cubo se mueve hacia la izquierda.
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad  # Reduce la coordenada X para mover el cubo a la izquierda.
    # Si se presiona 'D', el cubo se mueve hacia la derecha.
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad  # Aumenta la coordenada X para mover el cubo a la derecha.

# Bucle principal del juego.
while jugando:
    eventos = pygame.event.get()  # Obtiene todos los eventos que han ocurrido.
    
    # Obtiene el estado de las teclas presionadas.
    teclas = pygame.key.get_pressed()

    # Llama a la función para gestionar el movimiento del cubo según las teclas presionadas.
    gestionar_teclas(teclas)
    
    # Recorre cada evento para verificar si el jugador cierra la ventana.
    for evento in eventos:
        if evento.type == pygame.QUIT:  # Si se detecta un evento de cierre de ventana.
            jugando = False  # Finaliza el bucle del juego.
    
    VENTANA.fill("black")  # Limpia la pantalla y la llena con color negro.
    
    # Dibuja el cubo en la ventana.
    cubo.dibujar(VENTANA)
    
    # Actualiza la pantalla para reflejar los cambios.
    pygame.display.update()

quit()  # Finaliza pygame cuando el bucle termina.
