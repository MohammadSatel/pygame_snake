import pygame
import random

pygame.init()

# Set up display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Snake initial position and velocity
snake_position = [100, 50]
snake_body = [[200, 100], [190, 100], [180, 100]]
velocity = [5, 0]

# Food position
food_position = [random.randrange(1, (width//100)) * 100,
                 random.randrange(1, (height//100)) * 100]
food_spawn = True

# Clock to control the frame rate
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Change direction based on arrow keys
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                velocity = [-10, 0]
            if keys[pygame.K_RIGHT]:
                velocity = [10, 0]
            if keys[pygame.K_UP]:
                velocity = [0, -10]
            if keys[pygame.K_DOWN]:
                velocity = [0, 10]

    # Move the snake
    snake_position[0] += velocity[0]
    snake_position[1] += velocity[1]

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (width//100)) * 100,
                         random.randrange(1, (height//100)) * 100]
    food_spawn = True

    # Draw Snake and Food
    display.fill(black)
    for pos in snake_body:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(display, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    pygame.display.update()
    clock.tick(15)

pygame.quit()
