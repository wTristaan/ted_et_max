from pygame import sprite, image, transform, Surface


class Sprite(sprite.Sprite):
    def __init__(self, img, w, h):
        super().__init__()
        img = image.load(img)
        img_scaled = transform.scale(img, (w, h))
        self.image = img_scaled
        self.sprite = Surface([w, h])
        self.rect = self.sprite.get_rect()
        self.x = 0
        self.y = 0

    def set_image_size(self, width, height):
        self.image = transform.scale(self.image, (width, height))

    def resize_image(self, width, height):
        self.image = transform.scale(self.image, (width, height))

    def update(self, screen, x, y):
        screen.blit(self.image, (x, y))
        sprite.Sprite.update(self)