import pygame  # Importa el módulo pygame para manejar gráficos y eventos.
import random  # Importa el módulo random para generar posiciones aleatorias de los enemigos.
from personaje import Cubo  # Importa la clase Cubo desde el archivo 'personaje.py'.
from enemigo import Enemigo  # Importa la clase Enemigo desde el archivo 'enemigo.py'.

# Definir el tamaño de la ventana.
ANCHO = 1000  # Ancho de la ventana.
ALTO = 800  # Alto de la ventana.
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Crea la ventana del juego con las dimensiones especificadas.
FPS = 60  # Define la tasa de cuadros por segundo.

# Inicializa variables del juego.
jugando = True  # Bandera para controlar el bucle del juego.
reloj = pygame.time.Clock()  # Crea un objeto reloj para controlar el tiempo.
tiempo_pasado = 0  # Variable para rastrear el tiempo pasado.
tiempo_entre_enemigos = 500  # Intervalo entre la aparición de nuevos enemigos en milisegundos.
cubo = Cubo(ANCHO/2, ALTO-75)  # Crea una instancia de la clase Cubo en la posición (100, 100).
enemigos = []  # Lista para almacenar enemigos.

# Añade un enemigo en el centro de la parte superior de la ventana.
enemigos.append(Enemigo(ANCHO / 2, 100))  # Crea una instancia de la clase Enemigo en la posición (ANCHO/2, 100).

# Función para gestionar el movimiento del cubo mediante las teclas W, A, S, D.
def gestionar_teclas(teclas):
    # Si se presiona 'W', el cubo se mueve hacia arriba.
    #if teclas[pygame.K_w]:
        #cubo.y -= cubo.velocidad  # Reduce la coordenada Y para mover el cubo hacia arriba.
    # Si se presiona 'S', el cubo se mueve hacia abajo.
    #if teclas[pygame.K_s]:
        #cubo.y += cubo.velocidad  # Aumenta la coordenada Y para mover el cubo hacia abajo.
    # Si se presiona 'A', el cubo se mueve hacia la izquierda.
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad  # Reduce la coordenada X para mover el cubo a la izquierda.
    # Si se presiona 'D', el cubo se mueve hacia la derecha.
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad  # Aumenta la coordenada X para mover el cubo a la derecha.

# Bucle principal del juego.
while jugando:
    tiempo_pasado += reloj.tick(FPS)  # Controla la velocidad de fotogramas y actualiza el tiempo pasado.

    # Verifica si es el momento de crear un nuevo enemigo.
    if tiempo_pasado > tiempo_entre_enemigos:
        # Añade un nuevo enemigo en una posición aleatoria en el eje X y fuera de la pantalla en el eje Y.
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_pasado = 0  # Reinicia el tiempo pasado.

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

    # Dibuja todos los enemigos en la ventana y actualiza su posición.
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)  # Dibuja cada enemigo en la ventana.
        enemigo.movimiento()  # Actualiza la posición del enemigo.
    
    # Actualiza la pantalla para reflejar los cambios.
    pygame.display.update()

quit()  # Finaliza pygame cuando el bucle termina.
