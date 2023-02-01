import pygame
pygame.init()

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((0, 0, 0))
        pygame.display.set_caption("Ted & Max")

    def update(self):
        pygame.display.update()

    def get_window(self):
        return self.window
    