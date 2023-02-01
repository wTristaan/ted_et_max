import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # création des 3 boutons du menu
    def display_buttons(self, screen, button1, button2, button3):
        screen.blit(button1, (0, 0))
        screen.blit(button2, (0, 0))
        screen.blit(button3, (0, 0))

    # afficher le bouton "Aventure"
    def display_button1(self, screen, button1):
        screen.blit(button1, (0, 0))

    # afficher le bouton "Options"
    def display_button2(self, screen, button2):
        screen.blit(button2, (0, 0))

    # afficher le bouton "Quitter"
    def display_button3(self, screen, button3):
        screen.blit(button3, (0, 0))
