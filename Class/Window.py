from pygame import display, time, image, transform, mixer


class Window(object):
    def __init__(self, width, height, flags):
        self.__clock = time.Clock
        self.screen = display.set_mode((width, height), flags)
        self.tuto_text = False
        self.tuto_right = False
        self.tuto_jump = False
        self.main_music = "assets/Musics/main-music.mp3"
        self.change_menu = "assets/Musics/effects/change_menu.wav"
        self.typing_sound = "assets/Musics/effects/type_sound.mp3"
        self.lock_sound = "assets/Musics/effects/locked.mp3"
        self.jumping_sound = "assets/Musics/effects/jump.wav"

        self.change_menu_fx = mixer.Sound(self.change_menu)
        self.change_menu_fx.set_volume(0.2)

        self.typing_sound_fx = mixer.Sound(self.typing_sound)
        self.typing_sound_fx.set_volume(0.1)

        self.lock_sound_fx = mixer.Sound(self.typing_sound)
        self.lock_sound_fx.set_volume(1)

        self.jumping_sound_fx = mixer.Sound(self.jumping_sound)
        self.jumping_sound_fx.set_volume(0.1)

        display.set_caption("Ted & Max")
        mixer.init()
        mixer.music.load(self.main_music)
        mixer.music.set_volume(0.02)
        mixer.music.play(-1)

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
