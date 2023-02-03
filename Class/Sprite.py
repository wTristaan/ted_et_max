from pygame import sprite, image, transform
import random


class Sprite(sprite.Sprite):
    def __init__(self, color, w, h, x, y, img=None):
        super().__init__()
        self.images = list()
        if color:
            for i in range(1, 6):
                img = image.load(f"assets/Enemies/{color}/{color}{i}.png")
                img_scaled = transform.scale(img, (w, h))
                self.images.append(img_scaled)
        else:
            img = image.load(img)
            img_scaled = transform.scale(img, (w, h))
            self.images.append(img_scaled)
        self.x = int(x)
        self.y = int(y)
        self.rect = self.images[0].get_rect(center=(x, y))
        self.index = 0
        self.solo_index = 0
        self.explosions = list()
        for i in range(1, 21):
            img = image.load(f"assets/Enemies/explosion/explosion{i}.png")
            img_scaled = transform.scale(img, (w, h))
            self.explosions.append(img_scaled)
        self.velocity = 15
        self.gravity = 0.6
        self.jump_h = 15
        self.floor = y
        self.jumper = random.randint(0, 1)

    def update(self, screen, speed):
        self.x -= speed
        self.rect = self.images[self.index].get_rect(center=(self.x, self.y))
        screen.blit(self.images[self.index],  (self.x, self.y))

        self.index += 1
        if self.index > 4:
            self.index = 0

    def explode(self, screen):
        screen.blit(self.explosions[self.index], (self.x, self.y))

        self.index += 1
        if self.index > 19:
            self.index = 0

    def jump(self, screen):
        if self.jumper:
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jump_h:
                self.velocity = self.jump_h
                self.y = 460

            screen.blit(self.images[1], (self.x, self.y))
            self.rect = self.images [1].get_rect(topleft=(self.x, self.y))

    def solo_update(self, screen, speed):
        self.x -= speed
        self.rect = self.images[self.solo_index].get_rect(center=(self.x, self.y))
        screen.blit(self.images[self.solo_index], (self.x, self.y))
