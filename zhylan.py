import pygame
import sys
from random import randint  
from bd import user,save_score

pygame.init()

WINDOW = 500
TILE_SIZE = 25

score = 0
level = 1
snake = pygame.Rect(250, 250, TILE_SIZE, TILE_SIZE)
snake_body = []
snake_length = 1
snake_direction = (0, 0)
paused = False

foodtime = 0
foodlife = 500  

food = pygame.Rect(100, 100, TILE_SIZE, TILE_SIZE)

food_weight = [1, 5, 10]
food_value = food_weight[randint(0, len(food_weight)-1)]

obstacles = []
screen = pygame.display.set_mode([WINDOW, WINDOW])
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

counter = 0
speed = 10
username = input("Enter your username: ")
user_id, last_score = user(username)
if last_score:
    print(f"Welcome back, {username}! Last score: {last_score[0]}, level: {last_score[1]}")

def obstacle(level):
    obs_list = []
    for i in range(level):  
        x = randint(0, WINDOW - TILE_SIZE)
        y = randint(0, WINDOW - TILE_SIZE)
        obs_list.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
    return obs_list

def spawn_food():
    global food, food_value, foodtime
    food.x = randint(0, (WINDOW // TILE_SIZE) - 1) * TILE_SIZE
    food.y = randint(0, (WINDOW // TILE_SIZE) - 1) * TILE_SIZE
    food_value = food_weight[randint(0, len(food_weight)-1)]
    foodtime = 0

spawn_food() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                snake_direction = (0, -TILE_SIZE)
            if event.key == pygame.K_DOWN: 
                snake_direction = (0, TILE_SIZE)
            if event.key == pygame.K_LEFT: 
                snake_direction = (-TILE_SIZE, 0)
            if event.key == pygame.K_RIGHT: 
                snake_direction = (TILE_SIZE, 0)
            if event.key == pygame.K_p:  
                save_score(user_id, score, level)
                paused = not paused
    if paused:
        continue
    screen.fill((175, 215, 70))
    
    # Collision with the wall
    hit_wall = snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW
    
    # Collision with yourself
    hit_self = False
    if snake_direction != (0, 0):
        for segment in snake_body[:-1]:
            if snake.x == segment.x and snake.y == segment.y:
                hit_self = True
                break

    # Collision with obstacles
    hit_obstacle = False
    for obs in obstacles:
        if snake.colliderect(obs):
            hit_obstacle = True
            break
    
    if hit_wall or hit_self or hit_obstacle:
        snake.x = 250
        snake.y = 250
        snake_body = []
        snake_length = 1
        snake_direction = (0, 0)
        score = 0
        level = 1
        speed = 10
        obstacles = []  

    # Eating food
    if snake.x == food.x and snake.y == food.y:
        snake_length += 1
        score += food_value  
        spawn_food()  
        if score >= level * 30:
            level += 1
            speed = speed - 2
            if speed < 3:
                speed = 3
            obstacles.extend(obstacle(level))
    
    foodtime += 1
    if foodtime >= foodlife:
        spawn_food()

    # moving snake
    counter += 1
    if counter >= speed:
        counter = 0
        if snake_direction != (0, 0):
            snake.x += snake_direction[0]
            snake.y += snake_direction[1]
            snake_body.append(pygame.Rect(snake.x, snake.y, TILE_SIZE, TILE_SIZE))
            if len(snake_body) > snake_length:
                del snake_body[0]
    
    pygame.draw.rect(screen, "red", food)
    
    for segment in snake_body:
        pygame.draw.rect(screen, "blue", segment)
    
    for obs in obstacles:
        pygame.draw.rect(screen, "grey", obs)
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))
    
    pygame.display.flip()
    clock.tick(60)