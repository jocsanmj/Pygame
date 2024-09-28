import pygame  # Importa el módulo pygame para manejar gráficos y eventos.

# Define la clase Bala.
class Bala:
    def __init__(self, x, y):
        # Inicializa las propiedades de la bala.
        self.x = x  # Posición en el eje X.
        self.y = y  # Posición en el eje Y.
        self.ancho = 20  # Ancho de la bala.
        self.alto = 20  # Alto de la bala.
        self.velocidad = 10  # Velocidad de la bala.
        self.color = "white"  # Color de la bala.
        
        # Crea un rectángulo para representar la bala en pantalla.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # Método para dibujar la bala en la ventana.
    def dibujar(self, ventana):
        # Actualiza la posición del rectángulo con las coordenadas actuales de la bala.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        # Dibuja un rectángulo en la ventana con las propiedades de la bala.
        pygame.draw.rect(ventana, self.color, self.rect)

    # Método para mover la bala hacia arriba.
    def movimiento(self):
        self.y -= self.velocidad  # Disminuye la coordenada Y para mover el enemigo hacia arriba.
