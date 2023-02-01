from pygame import display, time


class Window(object):
    def __init__(self, width, height, flags):
        self.__clock = time.Clock
        self.screen = display.set_mode((width, height), flags)
        display.set_caption("Ted & Max")

    @staticmethod
    def update():
        display.update()

    def get_screen(self):
        return self.screen

    def get_screen_size(self):
        width, height = self.screen.get_size()
        return [width, height]
