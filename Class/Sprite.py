from pygame import sprite, image, transform


class Sprite(sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def set_image_size(self, width, height):
        self.image = transform.scale(self.image, (width, height))