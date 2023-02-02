import pygame
import time

from Class.Mouse import Mouse
from Class.Sprite import Sprite

pygame.init()
font = pygame.font.SysFont(None, 24)
text = "C'est l'aventure d’un chat maladroit" \
        " et d’une petite souris futée. " \
        "Le chat, qui tente à tout prix d’attraper la souris, " \
       "n'hésite pas à se défendre en lui faisant mal. " \
        "Malheureusement pour Max, il ne parviendra jamais à attraper son pire ennemi."
text = [*text]


def typing(text, window):
    spacing = 50
    line = 50
    text_end = False
    index = 0
    while not text_end:
        if index < len(text):
            screen_x, y = window.screen.get_size()
            text_img = font.render(text[index], True, "WHITE")
            text_width = text_img.get_width()
            if spacing >= screen_x - 50:
                line += 20
                spacing = 50
            window.screen.blit(text_img, (spacing, line))
            index += 1
            spacing += text_width
            window.update()
            time.sleep(0.01)
        else:
            text_img = font.render("Espace pour continuer", False, "WHITE")
            window.screen.blit(text_img, (50, 350))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        text_end = True
            window.update()


def show_ted(window):
    mouse = Mouse(x=10, y=550, w=50, h=50)
    right = False
    while not right:
        window.screen.blit(mouse.imgs[0], (mouse.x, mouse.y))
        text_img = font.render("--> pour avancer", True, "WHITE")
        window.screen.blit(text_img, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
        window.update()
    return mouse


mouse = None
scroll = 0


def show_text(window):
    text_img = font.render("Espace pour sauter", True, "WHITE")
    running = True
    while running:
        window.screen.blit(text_img, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        window.update()
    return enemis


enemis = False


def tutorial(window, bg_images, bg_width):
    global mouse, scroll, enemis
    running = True
    while running:
        if not window.tuto_text:
            window.screen.fill((0, 0, 0))
            typing(text, window)
            window.tuto_text = True

        window.draw_bg(bg_images, bg_width, scroll)

        if scroll > 150 and not window.tuto_right:
            mouse = show_ted(window)
            window.tuto_right = True
            scroll = 0

        if not mouse:
            scroll += 1
        else:
            scroll += 1
            mouse.update(window)
            if mouse.x > 150 and not window.tuto_jump:
                mouse.right_pressed = False
                mouse.left_pressed = False
                show_text(window)
                window.tuto_jump = True

            if mouse.x > 500:
                break

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mouse.right_pressed = True
                if event.key == pygame.K_SPACE:
                    mouse.up_pressed = True
                if event.key == pygame.K_LEFT:
                    mouse.left_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    mouse.right_pressed = False
                if event.key == pygame.K_LEFT:
                    mouse.left_pressed = False
        window.update()



