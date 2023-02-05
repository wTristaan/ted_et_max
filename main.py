# Importation des modules.
import pygame

from tuto import show_tuto
from settings import show_setting
from level_menu import show_level_menu
from Class.Window import Window

# initialisation de pygame
pygame.init()
clock = pygame.time.Clock()

# Création de la fenêtre
window = Window(1280, 720, pygame.RESIZABLE)

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
running = True

# boucle principale.
while running:

    # Affichage du background et défilement.
    window.draw_bg(bg_images, bg_width, scroll)

    # Auto scroll
    scroll += 1
    if scroll > bg_width:
        scroll = 0
    clock.tick(FPS)

    # Affichage des trois boutons
    screen.blit(play_button, (window.get_screen_size()[0] / 2 - play_button.get_width() / 2,
                              window.get_screen_size()[1] / 2 - play_button.get_height() / 2 - 200))
    screen.blit(play_button2, (window.get_screen_size()[0] / 2 - play_button2.get_width() / 2,
                               window.get_screen_size()[1] / 2 - play_button2.get_height() / 2 + 0))
    screen.blit(play_button3, (window.get_screen_size()[0] / 2 - play_button3.get_width() / 2,
                               window.get_screen_size()[1] / 2 - play_button3.get_height() / 2 + 200))

    # Gestion des évènements dans le menu principal.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.VIDEORESIZE:
            bg_images, bg_width = window.load_bg()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Aventure
                aventure = True
            if event.key == pygame.K_RIGHT:  # Option
                option = True
            if event.key == pygame.K_DOWN:  # Fermeture
                pygame.quit()
                exit()

    # Si le joueur décide de lancer le menu aventure.
    if aventure:
        # Vérifie le cache pour savoir si le joueur à déjà fait le tuto.
        value = open("cache.txt").read()
        if not value:
            window.change_menu_fx.play()
            aventure = show_tuto(window)
            if aventure:
                with open("cache.txt", 'w') as f:
                    f.write(str(1))
        else:
            window.change_menu_fx.play()
            aventure = False
            show_level_menu(window)

    # Si le joueur lance les options.
    if option:
        window.change_menu_fx.play()
        option = show_setting(window)
        window.change_menu_fx.play()
    window.update()
