from pygame import display, time, image, transform


class Window(object):
    def __init__(self, width, height, flags):
        self.__clock = time.Clock
        self.screen = display.set_mode((width, height), flags)
        self.tuto_text = False
        self.tuto_right = False
        self.tuto_jump = False
        display.set_caption("Ted & Max")

    @staticmethod
    def update():
        display.update()

    def get_screen(self):
        return self.screen

    def get_screen_size(self):
        width, height = self.screen.get_size()
        return [width, height]

    def load_bg(self):
        bg_images = list()
        w, h = self.get_screen_size()
        for i in range(1, 6):
            bg_image = image.load(f"assets/Menu/PARALLAX/layer{i}.png").convert_alpha()
            bg_image_scaled = transform.scale(bg_image, (w, h))
            bg_images.append(bg_image_scaled)
        bg_width = bg_images[0].get_width()
        return [bg_images, bg_width]

    def draw_bg(self, bg_images, bg_width, scroll):
        for x in range(5):
            speed = 1
            for i in bg_images:
                self.screen.blit(i, ((x * bg_width) - scroll * speed, 0))
                speed += 0.2
