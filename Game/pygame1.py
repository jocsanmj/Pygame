import pygame  # Importa el módulo pygame para manejar gráficos y eventos.
import random  # Importa el módulo random para generar posiciones aleatorias de los enemigos.
from personaje import Cubo  # Importa la clase Cubo desde el archivo 'personaje.py'.
from enemigo import Enemigo  # Importa la clase Enemigo desde el archivo 'enemigo.py'.
from bala import Bala #Importa la clase Bala desde el archivo 'bala.py'.
pygame.init() # Inicializa todos los módulos de Pygame.

# Definir el tamaño de la ventana.
ANCHO = 1000  # Ancho de la ventana.
ALTO = 800  # Alto de la ventana.
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Crea la ventana del juego con las dimensiones especificadas.
FPS = 60  # Define la tasa de cuadros por segundo.
FUENTE = pygame.font.SysFont("Comic Sans", 40)

# Inicializa variables del juego.
jugando = True  # Bandera para controlar el bucle del juego.
reloj = pygame.time.Clock()  # Crea un objeto reloj para controlar el tiempo.
vidas = 5 # Inicializa el número de vidas del jugador.
puntos = 0 # Inicializa el número de puntos del jugador
tiempo_pasado = 0  # Variable para rastrear el tiempo pasado.
tiempo_entre_enemigos = 500  # Intervalo entre la aparición de nuevos enemigos en milisegundos.
cubo = Cubo(ANCHO/2, ALTO-75)  # Crea una instancia de la clase Cubo en la posición (100, 100).
enemigos = []  # Lista para almacenar enemigos.
balas = [] # Lista para almacenar las balas
ultima_bala = 0  # Almacena el tiempo en el que se disparó la última bala.
tiempo_entre_balas = 200  # Define el tiempo en milisegundos que debe pasar entre cada disparo.

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
    # Si se preciona 'Espacio' se creara una bala
    if teclas[pygame.K_SPACE]: 
        crear_bala() #Llamar a la funcion que hace que se creen las balas

# Definimos la función que creará las balas
def crear_bala():
    global ultima_bala  # Usamos la variable 'ultima_bala' que se actualizará con el tiempo de la última bala disparada.

    # Verifica si ha pasado suficiente tiempo desde que se disparó la última bala, para disparar una nueva.
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        # Si ha pasado suficiente tiempo, se crea una nueva instancia de la clase 'Bala'.
        # La nueva bala se posiciona en el centro del cubo, tomando las coordenadas 'centerx' y 'centery' del cubo.
        balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))

        # Actualiza el tiempo de la última bala disparada al tiempo actual.
        ultima_bala = pygame.time.get_ticks()


# Bucle principal del juego, se ejecuta mientras el jugador tenga vidas.
while jugando and vidas > 0:
    tiempo_pasado += reloj.tick(FPS)  # Controla la velocidad de fotogramas y actualiza el tiempo pasado.

    # Verifica si es el momento de crear un nuevo enemigo.
    if tiempo_pasado > tiempo_entre_enemigos:
        # Añade un nuevo enemigo en una posición aleatoria en el eje X y fuera de la pantalla en el eje Y.
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_pasado = 0  # Reinicia el tiempo pasado.

    eventos = pygame.event.get()  # Obtiene todos los eventos que han ocurrido.
    
    # Obtiene el estado de las teclas presionadas.
    teclas = pygame.key.get_pressed()

    # Renderiza el texto de las vidas en pantalla.
    texto_vida = FUENTE.render(f"Vida: {vidas}", True, "white") # Crea un objeto de texto para mostrar el número de vidas.

    # Renderiza el texto de los puntos en pantalla.
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white") # Crea un objeto de texto para mostrar el número de puntos del jugador.

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

        # Verifica si el cubo colisiona con un enemigo.
        if pygame.Rect.colliderect(cubo.rect,enemigo.rect):  # Si hay colisión entre el cubo y un enemigo.
            vidas -= 1 # Resta una vida al jugador
            print(f"Te quedan {vidas} Vidas")  # Muestra el número de vidas restantes.
            enemigos.remove(enemigo)  # Elimina al enemigo que colisionó.

        if enemigo.y > ALTO: #Si el enemigo pasa debajo de la pantalla
            puntos += 1 #Sumamos un punto
            enemigos.remove(enemigo) #Eiminamos el cuadro enemigo para dar el punto al jugador 

        for bala in balas:  # Recorre cada bala en la lista de balas.
            # Verifica si la bala colisiona con el enemigo.
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):  # Si la colisión entre la bala y el enemigo ocurre.
                enemigo.vida -= 1 #Disminuye la vida del enemigo por cada bala que lo coliciona
                balas.remove(bala)  # Elimina la bala de la lista de balas ya que impactó en el enemigo.
                puntos += 1 #Suma un punto por cada enemigo eliminado

        # Verifica si la vida del enemigo esta completa
        if enemigo.vida <= 0: # Si la vida del enemigo es menor que 0
            enemigos.remove(enemigo ) # Se elmina al enemigo y se nos suma 1 punto

    # Dibuja todas las balas
    for bala in balas:
        bala.dibujar(VENTANA) #Dibuja cada bala en el cubo
        bala.movimiento()# Actualiza las posiciones de las balas

    # Dibuja el texto de vidas en la pantalla.
    VENTANA.blit(texto_vida, (20,20)) # Muestra el número de vidas en la parte superior izquierda.

    # Dibuja el texto de puntos en la pantalla.
    VENTANA.blit(texto_puntos, (20,60)) # Muestra el número de puntos abajo de las vidas
    # Actualiza la pantalla para reflejar los cambios.
    pygame.display.update()

# Finaliza la ejecución de todos los módulos de Pygame y cierra las ventanas abiertas
pygame.quit()

# Solicita al jugador que introduzca su nombre mediante la consola
nombre = input("Introduce tu nombre: ")
# Abre (o crea si no existe) un archivo de texto llamado 'puntuaciones.txt' en modo de anexado ('a') asegura que se agregue contenido al final del archivo sin sobrescribir los datos existentes
with open ('puntuaciones.txt', 'a') as archivo:
    # Escribe en el archivo el nombre del jugador y su puntuación actual, separados por un guion
    archivo.write(f"{nombre} - {puntos}\n")


quit()  # Finaliza pygame cuando el bucle termina.
