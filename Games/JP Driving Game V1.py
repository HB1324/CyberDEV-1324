import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
FPS = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Driving Game")

# Load car image
car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_img.fill(GREEN)

# Define the Car class
class Car:
    def __init__(self):
        self.x = WIDTH // 2 - CAR_WIDTH // 2
        self.y = HEIGHT - CAR_HEIGHT - 10
        self.speed = 5

    def move(self, dx):
        self.x += dx
        # Keep the car inside the screen boundaries
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - CAR_WIDTH:
            self.x = WIDTH - CAR_WIDTH

    def draw(self):
        screen.blit(car_img, (self.x, self.y))

# Define the Obstacle class
class Obstacle:
    def __init__(self):
        self.x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        self.y = -OBSTACLE_HEIGHT
        self.speed = random.randint(4, 8)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Collision detection
def check_collision(car, obstacles):
    for obstacle in obstacles:
        if (car.x < obstacle.x + OBSTACLE_WIDTH and
            car.x + CAR_WIDTH > obstacle.x and
            car.y < obstacle.y + OBSTACLE_HEIGHT and
            car.y + CAR_HEIGHT > obstacle.y):
            return True
    return False

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    car = Car()
    obstacles = []
    score = 0
    running = True

    while running:
        screen.fill(WHITE)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key press to move the car
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move(-car.speed)
        if keys[pygame.K_RIGHT]:
            car.move(car.speed)

        # Generate new obstacles

        # 0-30 Seconds
        if random.random() < 0.01:  # 2% chance to generate a new obstacle each frame
            obstacles.append(Obstacle())

        elif score > 3000:
            if random.random() < 0.025:  # 2% chance to generate a new obstacle each frame
                obstacles.append(Obstacle())

        # Move obstacles
        for obstacle in obstacles:
            obstacle.move()

        # Remove obstacles that have passed the screen
        obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

        # Check for collision
        if check_collision(car, obstacles):
            running = False

        # Draw everything
        car.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # Display the score
        score += 1
        font = pygame.font.SysFont("Arial", 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(FPS)

    # Game over message
    font = pygame.font.SysFont("Arial", 50)
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
    pygame.display.update()
    pygame.time.delay(2000)  # Display Game Over message for 2 seconds

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game_loop()