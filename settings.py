# Importations des modules.
import pygame

# Initialisation de pygame.
pygame.init()

# Initialisation des variables
scroll = 0
control_font = pygame.font.Font(None, 40)
text_control = control_font.render("Contrôles :", True, "white")
text_left = control_font.render("Avancer : Flèche de droite", True, "white")
text_down = control_font.render("Reculer : Flèche de gauche", True, "white")
text_jump = control_font.render("Sauter : Espace", True, "white")
text_escape = control_font.render("Retour : Echap", True, "white")
text_musique = control_font.render("Musique", True, "white")
music_button_radius = 100
btn_color = (0, 255, 0)


def show_setting(window):
    """Function permettant l'affichage et le paramétrage des options du jeu.

    :param window: Window
    :return: None
    """
    global scroll, control_font, music_button_radius, btn_color
    screen = window.screen
    running = True
    while running:

        screen.fill((135, 206, 250))  # Couleur bleu clair

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONUP:  # Si le bouton "musique" est cliqué
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if (745 - mouse_pos[0]) ** 2 + (
                            150 - mouse_pos[1]) ** 2 <= music_button_radius ** 2:
                        # Si la musique est en pause, la jouer
                        if not pygame.mixer.music.get_busy():
                            pygame.mixer.music.play()
                            btn_color = (0, 255, 0)
                        # Si la musique est en cours de lecture, la mettre en pause
                        else:
                            pygame.mixer.music.pause()
                            btn_color = (255, 255, 255)

        # Affichage des contrôles
        screen.blit(text_control, (50, 50))
        screen.blit(text_left, (50, 100))
        screen.blit(text_down, (50, 150))
        screen.blit(text_jump, (50, 200))
        screen.blit(text_escape, (50, 250))
        screen.blit(text_musique, (687, 135))

        # Dessiner le bouton "musique"
        pygame.draw.circle(screen, btn_color, (745, 150), 80, 7)
        window.update()
