import pygame  # Importa el módulo pygame para manejar gráficos y eventos.
from personaje import Cubo  # Importa la clase Cubo desde el archivo 'personaje.py'.

# Definir el tamaño de la ventana.
ANCHO = 1000  # Ancho de la ventana.
ALTO = 800  # Alto de la ventana.
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Crea la ventana del juego con las dimensiones especificadas.

# Inicializa variables del juego.
jugando = True  # Bandera para controlar el bucle del juego.
cubo = Cubo(100, 100)  # Crea una instancia de la clase Cubo en la posición (100, 100).

# Bucle principal del juego.
while jugando:
    eventos = pygame.event.get()  # Obtiene todos los eventos que han ocurrido.
    
    # Recorre cada evento para verificar si el jugador cierra la ventana.
    for evento in eventos:
        if evento.type == pygame.QUIT:  # Si se detecta un evento de cierre de ventana.
            jugando = False  # Finaliza el bucle del juego.
    
    # Dibuja el cubo en la ventana.
    cubo.dibujar(VENTANA)
    
    # Actualiza la pantalla para reflejar los cambios.
    pygame.display.update()

quit()  # Finaliza pygame cuando el bucle termina.
