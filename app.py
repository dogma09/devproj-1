import os

# Skip pygame and GUI if running inside Jenkins CI
if os.environ.get("JENKINS_HOME"):
    print("Running in Jenkins CI - skipping GUI.")
else:
    import pygame
    import time
    import random

    # Initialize pygame
    pygame.init()

    # Colors
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Screen size
    width = 600
    height = 400

    # Snake block size & speed
    block_size = 10
    snake_speed = 15

    # Fonts
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 20)

    # Display
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    def score_display(score):
        value = score_font.render(f"Score: {score}", True, yellow)
        win.blit(value, [0, 0])

    def draw_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        win.blit(mesg, [width / 6, height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

        while not game_over:

            while game_close:
                win.fill(blue)
                message("Game Over! Press Q-Quit or C-Play Again", red)
                score_display(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -block_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = block_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -block_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = block_size
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            win.fill(blue)
            pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(block_size, snake_list)
            score_display(length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
                foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()
