import pygame


class Mouse(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.imgs = list()
        for i in range(1, 3):
            img = pygame.image.load(f"assets/Mouse/mouse{i}.png")
            img_flip = pygame.transform.flip(img, True, False)
            self.imgs.append(pygame.transform.scale(img_flip, (w, h)))
        self.rect = self.imgs[0].get_rect()
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 1
        self.velocity = 20
        self.jump_h = 20
        self.gravity = 0.6

    def update(self, win):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            for y in self.imgs:
                self.imgs = []
                img = pygame.transform.flip(y, True, False)
                win.screen.blit(img, (self.x, self.y))
                self.imgs.append(img)
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            for y in self.imgs:
                self.imgs = []
                img = pygame.transform.flip(y, True, False)
                win.screen.blit(img, (self.x, self.y))
                self.imgs.append(img)

        if self.up_pressed:
            x = self.x
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jump_h:
                self.up_pressed = False
                self.velocity = self.jump_h
                self.y = 550

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)
        win.screen.blit(self.imgs[0], (self.x, self.y))
        win.update()
