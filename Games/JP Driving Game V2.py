import pygame
import random
import sys
import math

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 400, 600
FPS = 75

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROAD_COLOR = (169, 169, 169)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")

# Game variables
car_width = 60
car_height = 75
car_speed = 5
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
lane_width = WIDTH // 4
current_lane = 2  # Starts in the middle lane (index 2 for the 4 lanes)

# Obstacle variables
obstacle_width = 40
obstacle_height = 60
obstacle_speed = 5
obstacles = []

# Font for score and other text
font = pygame.font.SysFont("Arial", 30)


# Start screen function
def start_screen():
    # Display the start screen
    screen.fill(WHITE)
    title_text = font.render("Car Dodge Game", True, BLACK)
    start_text = font.render("Press SPACE to Start", True, BLACK)

    # Center the text on the screen
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))

    pygame.display.update()

    # Wait for the spacebar to start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game when space is pressed
                    waiting = False


# Game loop
def game():
    global car_x, current_lane, obstacles, car_y
    score = 0
    clock = pygame.time.Clock()

    # Call the start screen
    start_screen()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key handling for car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and current_lane > 0:
            current_lane -= 0.1  # Move left
        if keys[pygame.K_RIGHT] and current_lane < 3:
            current_lane += 0.1  # Move right

        # Update car position based on lane
        car_x = current_lane * lane_width + (lane_width - car_width) // 2

        # Generate new obstacles
        base_prob = 0.01  # Starting probability
        scaling_factor = 0.001  # Rate of probability increase
        if random.random() < base_prob + scaling_factor * math.log(score + 1):
            new_obstacle_lane = random.randint(0, 3)
            new_obstacle_x = new_obstacle_lane * lane_width + (lane_width - obstacle_width) // 2
            obstacles.append([new_obstacle_x, -obstacle_height])

        # Move obstacles down the screen
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)  # Remove obstacle once it goes off-screen
                score += 1  # Increase score for each passed obstacle

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if (obstacle[0] < car_x + car_width and obstacle[0] + obstacle_width > car_x and
                obstacle[1] < car_y + car_height and obstacle[1] + obstacle_height > car_y):
                game_over(score)

        # Clear the screen
        screen.fill(WHITE)

        # Draw the road
        pygame.draw.rect(screen, ROAD_COLOR, (WIDTH // 4, 0, 2 * lane_width, HEIGHT))

        # Draw the lanes (vertical lines)
        for i in range(1, 4):
            pygame.draw.line(screen, BLACK, (i * lane_width, 0), (i * lane_width, HEIGHT), 5)

        # Draw the car (green rectangle)
        pygame.draw.rect(screen, GREEN, (car_x, car_y, car_width, car_height))

        # Draw obstacles (red rectangles)
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

        # Display the score
        score_text = font.render(f"Score:        {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FPS)


# Game Over screen
def game_over(score):
    game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
    screen.fill(WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    # Wait for "r" to restart or quit the game
    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game on pressing "r"
                    game()  # Restart the game by calling the game function again
                elif event.key == pygame.K_q:  # Quit the game on pressing "q"
                    pygame.quit()
                    sys.exit()


# Run the game
game()
