import pygame  # Importa el módulo pygame para manejar gráficos y eventos.

# Define la clase Cubo.
class Cubo:
    def __init__(self, x, y):
        # Inicializa las propiedades del cubo.
        self.x = x  # Posición en el eje X.
        self.y = y  # Posición en el eje Y.
        self.ancho = 50  # Ancho del cubo.
        self.alto = 50  # Alto del cubo.
        self.velocidad = 1  # Velocidad del cubo.
        self.color = "red"  # Color del cubo.
        
        # Crea un rectángulo para representar el cubo en pantalla.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # Método para dibujar el cubo en la ventana.
    def dibujar(self, ventana):
        # Dibuja un rectángulo en la ventana con las propiedades del cubo.
        pygame.draw.rect(ventana, self.color, self.rect)
