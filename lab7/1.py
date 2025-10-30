import pygame
import datetime 
import time

pygame.init()
background = pygame.image.load("/Users/zansaa/Documents/pp2/lab7/image/base_micky.jpg")
minute_hand = pygame.image.load("/Users/zansaa/Documents/pp2/lab7/image/minute.png")
second_hand = pygame.image.load("/Users/zansaa/Documents/pp2/lab7/image/second.png")

WIDTH , HEIGHT = 1100,900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CENTER_X,CENTER_Y= WIDTH//2 , HEIGHT//2

background = pygame.transform.smoothscale(background, (WIDTH + 100, HEIGHT))


def rotation(image,angle,pivot):
    rotate_image= pygame.transform.rotate(image,-angle)
    rotate_rect= rotate_image.get_rect(center=pivot)
    return rotate_image,rotate_rect

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255,255,255))
    screen.blit(background, (-50, 0))
    
    now=datetime.datetime.now()
    minutes= now.minute + now.second / 60
    seconds = now.second + now.microsecond / 1e6

    minute_angle = (minutes / 60.0) * 360.0
    second_angle = (seconds / 60.0) * 360.0

    rotate_minute_hand, minute_rect = rotation(minute_hand, minute_angle, (CENTER_X, CENTER_Y))
    rotate_second_hand, second_rect = rotation(second_hand, second_angle, (CENTER_X, CENTER_Y))
    
    screen.blit(rotate_minute_hand, minute_rect)
    screen.blit(rotate_second_hand, second_rect)

    pygame.display.flip()

    time.sleep(1/60) 
pygame.quit()

