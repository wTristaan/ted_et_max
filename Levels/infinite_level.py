import pygame

from Class.Mouse import Mouse
from Class.Sprite import Sprite


def infinite_level(window):
    obstacle_timer = 0
    obstacle_spawn = False
    obstacle_cooldown = 1000
    mouse = Mouse(x=10, y=460, w=50, h=50)
    mouseGroup = pygame.sprite.GroupSingle()
    mouseGroup.add(mouse)

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

        bg_orange_x -= 1 / 2
        bg_orange_x2 -= 1 / 2
        bg_cloud_x -= 2 / 2
        bg_cloud_x2 -= 2 / 2
        bg_mountain_x -= 3 / 2
        bg_mountain_x2 -= 3 / 2
        bg_tree_x -= 4 / 2
        bg_tree_x2 -= 4 / 2
        floor_x -= 5 / 2
        floor_x2 -= 5 / 2

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
            obstacleSpawn = True

        if obstacleSpawn:
            new_enemis = Sprite(1280, 580)
            obstacleGroup.add(newObstacle)
            obstacleTimer = pygame.time.get_ticks()
            obstacleSpawn = False

        mouse.right_down = True
        mouse.x = 10
        mouse.display(screen)
        window.update()