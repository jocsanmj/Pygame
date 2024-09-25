import pygame  # Importa el módulo pygame para manejar gráficos y eventos.

# Define la clase Enemigo.
class Enemigo:
    def __init__(self, x, y):
        # Inicializa las propiedades del enemigo.
        self.x = x  # Posición en el eje X.
        self.y = y  # Posición en el eje Y.
        self.ancho = 50  # Ancho del enemigo.
        self.alto = 50  # Alto del enemigo.
        self.velocidad = 5  # Velocidad del enemigo.
        self.color = "purple"  # Color del enemigo.
        
        # Crea un rectángulo para representar el enemigo en pantalla.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # Método para dibujar el enemigo en la ventana.
    def dibujar(self, ventana):
        # Actualiza la posición del rectángulo con las coordenadas actuales del enemigo.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        # Dibuja un rectángulo en la ventana con las propiedades del enemigo.
        pygame.draw.rect(ventana, self.color, self.rect)

    # Método para mover el enemigo hacia abajo.
    def movimiento(self):
        self.y += self.velocidad  # Aumenta la coordenada Y para mover el enemigo hacia abajo.
