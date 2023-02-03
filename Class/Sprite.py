from pygame import sprite, image, transform


class Sprite(sprite.Sprite):
    def __init__(self, color, w, h, x, y):
        super().__init__()
        self.images = list()
        if color == "bleu":
            for i in range(1, 6):
                img = image.load(f"assets/Enemies/bleu/bleu{i}.png")
                img_scaled = transform.scale(img, (w, h))
                self.images.append(img_scaled)
        self.x = int(x)
        self.y = int(y)
        self.rect = self.images[0].get_rect(center=(x, y))
        self.index = 0
        self.explosions = list()
        for i in range(1, 5):
            img = image.load(f"assets/Enemies/explosion/explosion{i}.png")
            img_scaled = transform.scale(img, (w, h))
            self.explosions.append(img_scaled)

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
        if self.index > 3:
            self.index = 0
