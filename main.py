import pygame
from Class.Window import Window
from Class.Sprite import Sprite
from Class.Button import Button

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
    
# button
play_button = pygame.image.load("assets/Menu/button1.png")
play_button = pygame.transform.scale(play_button, (550, 200))
play_button_rect = play_button.get_rect()

play_button2 = pygame.image.load("assets/Menu/button2.png")
play_button2 = pygame.transform.scale(play_button2, (550, 200))
play_button2_rect = play_button2.get_rect()

play_button3 = pygame.image.load("assets/Menu/button3.png")
play_button3 = pygame.transform.scale(play_button3, (550, 200))
play_button3_rect = play_button3.get_rect()


aventure = False
option = False
exit = False




# boucle pour que sa tourne indéfiniment
while True:
    draw_bg()

    # auto scroll
    scroll += 1
    if scroll > bg_width:
        scroll = 0
    clock.tick(FPS)

    # affichage des trois boutons
    window.get_screen().blit(play_button, (window.get_screen_size()[0] / 2 - play_button.get_width() / 2, window.get_screen_size()[1] / 2 - play_button.get_height() / 2 - 200))
    window.get_screen().blit(play_button2, (window.get_screen_size()[0] / 2 - play_button2.get_width() / 2, window.get_screen_size()[1] / 2 - play_button2.get_height() / 2 + 0))
    window.get_screen().blit(play_button3, (window.get_screen_size()[0] / 2 - play_button3.get_width() / 2, window.get_screen_size()[1] / 2 - play_button3.get_height() / 2 + 200))

    if aventure:
        print("Aventure")
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      # faire lancer le jeu 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: # aventure
          aventure = True
        if event.key == pygame.K_LEFT: # option
          option = True
        if event.key == pygame.K_DOWN: # fermeture
          pygame.quit()
          exit()




    window.update()



        


        