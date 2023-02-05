# Importations des modules.
import pygame

from Levels.infinite_level import infinite_level

# Initialisation de pygame.
pygame.init()

# Initialisation des variables.
running = True
scroll = 0


def show_level_menu(window):
    """Fonction qui affiche la fenêtre des niveaux lorsque le joueur à déjà fait le tuto.

    :param window: Window
    :return: None
    """
    global running, scroll
    bg_images, bg_width = window.load_bg()
    screen = window.get_screen()
    level_one_image = pygame.image.load("assets/Menu/Levels/level_1.png")
    level_one_image_scaled = pygame.transform.scale(level_one_image, (350, 150))
    level_one_rect = level_one_image_scaled.get_rect(topleft=(100, 100))

    level_two_image = pygame.image.load("assets/Menu/Levels/level_2.png")
    level_two_image_scaled = pygame.transform.scale(level_two_image, (350, 150))
    level_two_rect = level_two_image_scaled.get_rect(topleft=(500, 100))

    level_three_image = pygame.image.load("assets/Menu/Levels/level_3.png")
    level_three_image_scaled = pygame.transform.scale(level_three_image, (350, 150))
    level_three_rect = level_three_image_scaled.get_rect(topleft=(100, 300))

    level_four_image = pygame.image.load("assets/Menu/Levels/level_4.png")
    level_four_image_scaled = pygame.transform.scale(level_four_image, (350, 150))
    level_four_rect = level_four_image_scaled.get_rect(topleft=(500, 300))

    while running:
        # Affichage du background et défilement.
        window.draw_bg(bg_images, bg_width, scroll)

        # auto scroll
        scroll += 1
        if scroll > bg_width:
            scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:  # Si le bouton "musique" est cliqué
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if level_one_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        window.lock_sound_fx.play()
                    if level_two_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        window.lock_sound_fx.play()
                    if level_three_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        window.lock_sound_fx.play()
                    if level_four_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        window.change_menu_fx.play()
                        infinite_level(window)

        screen.blit(level_one_image_scaled, level_one_rect)
        screen.blit(level_two_image_scaled, level_two_rect)
        screen.blit(level_three_image_scaled, level_three_rect)
        screen.blit(level_four_image_scaled, level_four_rect)

        window.update()
