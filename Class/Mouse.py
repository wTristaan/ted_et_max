import pygame.transform
from pygame import image, Surface, transform, sprite, Rect


class Mouse(sprite.Sprite):

    def __init__(self, x, y, w, h):
        super().__init__()
        self.images_left = list()
        for i in range(1, 3):
            img = image.load(f"assets/Mouse/mouse{i}.png")
            img_scaled = transform.scale(img, (w, h))
            self.images_left.append(img_scaled)
        self.images_right = list()
        for i in range(1, 3):
            img = image.load(f"assets/Mouse/mouse{i}.png")
            img_scaled = transform.scale(img, (w, h))
            img_flip = transform.flip(img_scaled, True, False)
            self.images_right.append(img_flip)
        self.x = int(x)
        self.y = int(y)
        self.right_down = False
        self.left_down = False
        self.index = 0
        self.speed = 1
        self.last_pos = "right"
        self.space_down = False
        self.velocity = 20
        self.gravity = 0.6
        self.jump_h = 20
        self.floor = y
        self.jump_count = 0
        self.rect = self.images_right[0].get_rect(center=(x, y))
        self.health = 1
        self.death = pygame.transform.flip(self.images_left[0], False, True)

    def display(self, screen):
        if self.space_down:
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jump_h:
                self.velocity = self.jump_h
                self.y = 460
                self.space_down = False

            if self.last_pos == "right":
                screen.blit(self.images_right[1], (self.x, self.y))
                self.rect = self.images_right[1].get_rect(topleft=(self.x, self.y))
            if self.last_pos == "left":
                screen.blit(self.images_left[1], (self.x, self.y))
                self.rect = self.images_left[1].get_rect(topleft=(self.x, self.y))

        if self.right_down:
            self.x += self.speed
            screen.blit(self.images_right[self.index], (self.x, self.y))
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.last_pos = "right"
        elif self.left_down:
            self.x -= self.speed
            screen.blit(self.images_left[self.index], (self.x, self.y))
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.last_pos = "left"
        else:
            if self.last_pos == "right":
                screen.blit(self.images_right[0], (self.x, self.y))
            if self.last_pos == "left":
                screen.blit(self.images_left[0], (self.x, self.y))

    def flip(self, screen):
        screen.blit(self.death, (self.x, self.y))
