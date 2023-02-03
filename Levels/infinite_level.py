import pygame
import random

from Class.Mouse import Mouse
from Class.Sprite import Sprite

font = pygame.font.SysFont(None, 35)


def ended_game(window, score, enemie):
    window.boom_fx.play()
    pygame.mixer.music.stop()
    running = True
    player_message = font.render("Vous êtes mort votre score est de " + str(round(score, 1)), True, "white")
    while running:
        enemie.explode(window.screen)
        window.screen.blit(player_message, (250, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

        window.update()


def lock_player(window):
    running = True
    player_message = font.render("Espace pour commencer", True, "white")
    while running:
        window.screen.blit(player_message, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        window.update()


def infinite_level(window):
    cheese_count = 0
    cheese = None
    cheese_timer = 0
    cheese_cooldown = 7000
    cheese_spawn = False
    speed = 1.7
    colors = ["bleu", "red", "green"]
    game_over = False
    mouse_hurt = False
    locked = False
    full_life = pygame.image.load("assets/Mouse/heart.png").convert_alpha()
    full_life_scaled = pygame.transform.scale(full_life, (25, 25))
    player_score = 0
    new_enemie = None
    obstacle_timer = 0
    obstacle_spawn = False
    obstacle_cooldown = 2500
    mouse = Mouse(x=10, y=460, w=50, h=50)

    running = True
    screen = window.get_screen()
    w, h = window.get_screen_size()

    bg_orange = pygame.image.load("assets/Menu/PARALLAX/layer1.png").convert_alpha()
    bg_orange_x = 0

    bg_cloud = pygame.image.load("assets/Menu/PARALLAX/layer2.png").convert_alpha()
    bg_cloud_x = 0

    bg_mountain = pygame.image.load("assets/Menu/PARALLAX/layer3.png").convert_alpha()
    bg_mountain_x = 0

    bg_tree = pygame.image.load("assets/Menu/PARALLAX/layer4.png").convert_alpha()
    bg_tree_x = 0

    floor = pygame.image.load("assets/Menu/PARALLAX/layer5.png").convert_alpha()
    floor_x = 0

    bg_orange_scaled = pygame.transform.scale(bg_orange, (w, h))
    bg_orange_x2 = w

    bg_cloud_scaled = pygame.transform.scale(bg_cloud, (w, h))
    bg_cloud_x2 = w

    bg_mountain_scaled = pygame.transform.scale(bg_mountain, (w, h))
    bg_mountain_x2 = w

    bg_tree_scaled = pygame.transform.scale(bg_tree, (w, h))
    bg_tree_x2 = w

    floor_scaled = pygame.transform.scale(floor, (w, h))
    floor_x2 = w

    while running:
        speed = speed * 1.00005
        if not locked:
            locked = lock_player(window)
            mouse.space_down = True
        screen.blit(bg_orange_scaled, (bg_orange_x, 0))
        screen.blit(bg_orange_scaled, (bg_orange_x2, 0))

        screen.blit(bg_cloud_scaled, (bg_cloud_x, 0))
        screen.blit(bg_cloud_scaled, (bg_cloud_x2, 0))

        screen.blit(bg_mountain_scaled, (bg_mountain_x, 0))
        screen.blit(bg_mountain_scaled, (bg_mountain_x2, 0))

        screen.blit(bg_tree_scaled, (bg_tree_x, 0))
        screen.blit(bg_tree_scaled, (bg_tree_x2, 0))

        screen.blit(floor_scaled, (floor_x, 0))
        screen.blit(floor_scaled, (floor_x2, 0))

        bg_orange_x -= 1 / speed
        bg_orange_x2 -= 1 / speed
        bg_cloud_x -= 2 / speed
        bg_cloud_x2 -= 2 / speed
        bg_mountain_x -= 3 / speed
        bg_mountain_x2 -= 3 / speed
        bg_tree_x -= 4 / speed
        bg_tree_x2 -= 4 / speed
        floor_x -= 5 / speed
        floor_x2 -= 5 / speed

        if bg_orange_x < -w:
            bg_orange_x = w
        if bg_orange_x2 < -w:
            bg_orange_x2 = w
        if bg_cloud_x < -w:
            bg_cloud_x = w
        if bg_cloud_x2 < -w:
            bg_cloud_x2 = w
        if bg_mountain_x < -w:
            bg_mountain_x = w
        if bg_mountain_x2 < -w:
            bg_mountain_x2 = w
        if bg_tree_x < -w:
            bg_tree_x = w
        if bg_tree_x2 < -w:
            bg_tree_x2 = w
        if floor_x < -w:
            floor_x = w
        if floor_x2 < -w:
            floor_x2 = w

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window.jumping_sound_fx.play()
                    mouse.space_down = True

        if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
            obstacle_spawn = True

        if pygame.time.get_ticks() - cheese_timer >= cheese_cooldown:
            cheese_spawn = True

        if cheese_spawn:
            y = random.randint(420, 465)
            cheese = Sprite(color=None, w=50, h=50, x=w + 100, y=y, img="assets/Mouse/camembert.png")
            cheese_timer = pygame.time.get_ticks()
            cheese_spawn = False

        if obstacle_spawn:
            color = random.choice(colors)
            new_enemie = Sprite(color=color, w=50, h=50, x=w + 10, y=465)
            obstacle_timer = pygame.time.get_ticks()
            obstacle_spawn = False

        if cheese:
            cheese.solo_update(screen, speed)
            if cheese.rect.collidepoint(mouse.rect.x, mouse.rect.y):
                window.jumping_sound_fx.play()
                cheese = None
                cheese_count += 1
                mouse.health += 1

        if new_enemie:
            new_enemie.jump(screen)
            new_enemie.update(screen, 5 / speed)

            if new_enemie.rect.collidepoint(mouse.rect.x, mouse.rect.y):
                window.hurt_fx.play()
                if mouse.health == 0:
                    game_over = True
                else:
                    mouse.space_down = True
                    new_enemie = None
                    mouse_hurt = True

        if mouse_hurt:
            mouse.health -= 1
            mouse_hurt = False

        if round(player_score, 1) % 100 == 0 and int(player_score) > 0:
            window.scoring_sound_fx.play()

        player_score += 0.1
        player_score_text = font.render(str(int(player_score)), True, "black")
        player_cheese_text = font.render("Fromage récupéré(s) " + str(int(cheese_count)), True, "black")
        # Affiche le score du joueur
        screen.blit(player_score_text, (800, 10))
        screen.blit(player_cheese_text, (200, 10))

        x = 30
        for i in range(mouse.health):
            screen.blit(full_life_scaled, (x, 10))
            x += 50

        if not game_over:
            mouse.right_down = True
            mouse.x = 10
            mouse.display(screen)
        else:
            mouse.flip(screen)
            return ended_game(window, player_score, new_enemie)
        window.update()