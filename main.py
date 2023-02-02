# Importation des modules.
import pygame

from tuto import tutorial
from infinite_level import infinite_level
from Class.Window import Window


# initialisation de pygame
pygame.init()
clock = pygame.time.Clock()

# Création de la fenêtre
window = Window(900, 700, pygame.RESIZABLE)

# Initialisation des variables.
screen = window.get_screen()
w, h = window.get_screen_size()
FPS = 60
scroll = 0
play_button = pygame.image.load("assets/Menu/button1.png")
play_button = pygame.transform.scale(play_button, (550, 200))
play_button_rect = play_button.get_rect()
play_button2 = pygame.image.load("assets/Menu/button2.png")
play_button2 = pygame.transform.scale(play_button2, (550, 200))
play_button2_rect = play_button2.get_rect()
play_button3 = pygame.image.load("assets/Menu/button3.png")
play_button3 = pygame.transform.scale(play_button3, (550, 200))
play_button3_rect = play_button3.get_rect()
aventure = False
option = False
close_window = False
bg_images, bg_width = window.load_bg()
scroll = 0

# boucle principale.
while True:
    window.draw_bg(bg_images, bg_width, scroll)

    # auto scroll
    scroll += 1
    if scroll > bg_width:
        scroll = 0
    clock.tick(FPS)

    # affichage des trois boutons
    screen.blit(play_button, (window.get_screen_size()[0] / 2 - play_button.get_width() / 2,
                                           window.get_screen_size()[1] / 2 - play_button.get_height() / 2 - 200))
    screen.blit(play_button2, (window.get_screen_size()[0] / 2 - play_button2.get_width() / 2,
                                            window.get_screen_size()[1] / 2 - play_button2.get_height() / 2 + 0))
    screen.blit(play_button3, (window.get_screen_size()[0] / 2 - play_button3.get_width() / 2,
                                            window.get_screen_size()[1] / 2 - play_button3.get_height() / 2 + 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.VIDEORESIZE:
            bg_images, bg_width = window.load_bg()
        # faire lancer le jeu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # aventure
                aventure = True
            if event.key == pygame.K_LEFT:  # option
                option = True
            if event.key == pygame.K_DOWN:  # fermeture
                pygame.quit()

    if aventure:
        value = open("cache.txt").read()
        print(value)
        if value == "0":
            tutorial(window=window, bg_images=bg_images, bg_width=bg_width)
            with open("cache.txt", 'w') as f:
                f.write(str(1))
            infinite_level(window=window, bg_images=bg_images, bg_width=bg_width)
        else:
            infinite_level(window=window, bg_images=bg_images, bg_width=bg_width)
    window.update()
