# Importations des modules.
import pygame
import time

from Class.Mouse import Mouse

# Initialisation de pygame.
pygame.init()


# Définitions de méthodes.
def typing(text, window):
    """Fonction qui bloque le joueur et affiche un texte en mode "machine à écrire".

    :param text: Str
    :param window: Window
    :return: Bool
    """
    global spacing, line, text_end, index, space_text
    while not text_end:
        if index < len(text):
            screen_x, y = window.screen.get_size()
            text_img = font.render(text[index], True, "white")
            text_width = text_img.get_width()
            if spacing >= screen_x - 50:
                line += 20
                spacing = 50
            window.screen.blit(text_img, (spacing, line))
            index += 1
            spacing += text_width
            time.sleep(0.01)
            window.typing_sound_fx.play()
            window.update()
        else:
            window.screen.blit(space_text, (50, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    return True
        window.update()


def show_mouse(window):
    """Fonction qui fait apparaitre le joueur et le bloque jusqu'à ce qu'il avance.

    :param window: Window
    :return: List
    """
    global user_left_used, right_text
    mouse = Mouse(x=10, y=545, w=75, h=75)
    screen = window.get_screen()
    while not user_left_used:
        mouse.display(screen)
        window.screen.blit(right_text, (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    return [mouse, True]

        window.update()


def show_space(window, text_to_show):
    """Fonction qui affiche un text et bloque le joueur jusqu'à ce qu'il saute.

    :param window: Window
    :param text_to_show: Str
    :return: Bool
    """
    global user_space
    while not user_space:
        window.screen.blit(text_to_show, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        window.update()


# Initialisation des variables.
running = True
scroll = 0
font = pygame.font.SysFont(None, 24)
story_text = "C’est l’histoire d’un petit rat un peu maladroit. Le rat est très radin et ne veux pas utiliser sa " \
             "nourriture. Alors, il trouve comme moyen de voler toute la nourriture qu’il voit. “On peut en effet " \
             "dire que c’est un sacré rat”."
story_text = [*story_text]
spacing = 50
line = 50
text_end = False
index = 0
space_text = font.render("Espace pour continuer", False, "WHITE")
right_text = font.render("Flèche de droite pour avancer", False, "WHITE")
user_space_text = font.render("Espace pour sauter", False, "WHITE")
text_tuto_end = font.render("Fin du tuto ! Espace pour continuer", False, "WHITE")
user_left_used = False
mouse_exist = False
mouse = None
user_space = False
user_space_used = False
end = False


def show_tuto(window):
    global running, story_text, scroll, mouse_exist, mouse, user_space_used, end
    bg_images, bg_width = window.load_bg()
    screen = window.screen
    while running:
        if not window.tuto_text:
            window.screen.fill((0, 0, 0))
            user_choice = typing(story_text, window)
            if not user_choice:
                return False
            window.tuto_text = True
        else:
            # Affichage du background et défilement.
            window.draw_bg(bg_images, bg_width, scroll)

            # auto scroll
            scroll += 1

            if scroll > 100 and not mouse_exist:
                mouse, mouse_exist = show_mouse(window)
                mouse.right_down = True

            if mouse:
                if mouse.jump_count == 4:
                    end = show_space(window, text_tuto_end)
                    if end:
                        return True
                mouse.display(screen)

            if scroll > 300 and mouse and not user_space_used:
                user_space_used = show_space(window, user_space_text)
                mouse.space_down = True
                mouse.right_down = False
                mouse.right_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if mouse:
                        mouse.right_down = True
                if event.key == pygame.K_LEFT:
                    if mouse:
                        mouse.left_down = True
                if event.key == pygame.K_SPACE:
                    if mouse and user_space_used:
                        window.jumping_sound_fx.play()
                        mouse.space_down = True
                        mouse.jump_count += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    if mouse:
                        mouse.right_down = False
                if event.key == pygame.K_LEFT:
                    if mouse:
                        mouse.left_down = False
        window.update()
