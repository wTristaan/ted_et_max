import pygame
from Class.Window import Window
from Class.Sprite import Sprite

pygame.init()

window = Window(900,700,pygame.RESIZABLE)
window.get_screen()
window.get_screen_size()

clock = pygame.time.Clock()
FPS = 60
scroll = 0


bg_images = []
for i in range(1, 6):
  bg_image = pygame.image.load(f"assets/Menu/PARALLAX/layer{i}.png").convert_alpha()
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
        window.get_screen().blit(i, ((x * bg_width) - scroll * speed, 0))
        speed += 0.2
    




# boucle pour que sa tourne indéfiniment
while True:
    draw_bg()

    # auto scroll
    scroll += 1
    if scroll > bg_width:
        scroll = 0
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.update()



        


        