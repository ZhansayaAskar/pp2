import pygame
import time

pygame.init()
screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

pos_x = 250
pos_y = 250
radius = 25
step = 20

running = True
while running:
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, "red", (pos_x, pos_y), radius)

    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False  

      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            pos_y = min(pos_y + step, 500 - radius)
         elif event.key == pygame.K_UP:
            pos_y = max(pos_y - step, radius)
         elif event.key == pygame.K_LEFT:
            pos_x = max(pos_x - step, radius)
         elif event.key == pygame.K_RIGHT:
            pos_x = min(pos_x + step, 500 - radius)

    time.sleep(1/200)

pygame.quit()