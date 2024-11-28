import tkinter as tk
from tkinter import simpledialog
import random


class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")

        # Game constants
        self.canvas_width = 1280
        self.canvas_height = 720
        self.paddle_width = 15
        self.paddle_height = 150
        self.paddle_speed = 10
        self.ball_size = 30
        self.min_ball_speed = 5
        self.max_ball_speed = 20
        self.game_active = False

        # Paddle movement states
        self.paddle1_direction = 0
        self.paddle2_direction = 0

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Create placeholder score label (updated later)
        self.score_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 20),
            bg="black",
            fg="white"
        )
        self.score_label.pack()

        # Bind keys for paddle movement and other actions
        self.root.bind("<w>", lambda event: self.set_paddle_direction(1, -1))
        self.root.bind("<s>", lambda event: self.set_paddle_direction(1, 1))
        self.root.bind("<Up>", lambda event: self.set_paddle_direction(2, -1))
        self.root.bind("<Down>", lambda event: self.set_paddle_direction(2, 1))
        self.root.bind("<KeyRelease-w>", lambda event: self.set_paddle_direction(1, 0))
        self.root.bind("<KeyRelease-s>", lambda event: self.set_paddle_direction(1, 0))
        self.root.bind("<KeyRelease-Up>", lambda event: self.set_paddle_direction(2, 0))
        self.root.bind("<KeyRelease-Down>", lambda event: self.set_paddle_direction(2, 0))
        self.root.bind("<space>", self.start_game)
        self.root.bind("<x>", self.reset_game)
        self.root.bind("<r>", self.reset_to_config)

        # Delay configuration until event loop starts
        self.root.after(100, self.configure_game)

    def configure_game(self):
        """Prompt the user for game settings."""
        # Player names
        self.player1_name = simpledialog.askstring("Player 1 Name", "Enter Player 1's name:", initialvalue="Player 1")
        self.player2_name = simpledialog.askstring("Player 2 Name", "Enter Player 2's name:", initialvalue="Player 2")

        # Player colors
        self.player1_color = simpledialog.askstring(
            "Player 1 Color", "Enter Player 1's paddle color (e.g., red, blue):", initialvalue="red"
        )
        self.player2_color = simpledialog.askstring(
            "Player 2 Color", "Enter Player 2's paddle color (e.g., green, yellow):", initialvalue="blue"
        )

        # Ball color
        self.ball_color = simpledialog.askstring(
            "Ball Color", f"Enter the ball's color (e.g., mix of {self.player1_color} and {self.player2_color}):",
            initialvalue="purple"
        )

        # Ball speed
        self.ball_speed = simpledialog.askinteger(
            "Ball Speed", "Enter ball speed (5-20):", minvalue=5, maxvalue=20, initialvalue=7
        )

        # Paddle speed
        self.paddle_speed = simpledialog.askinteger(
            "Paddle Speed", "Enter paddle speed (1-20):", minvalue=1, maxvalue=20, initialvalue=10
        )

        # Ball size
        self.ball_size = simpledialog.askinteger(
            "Ball Size", "Enter ball size (10-100):", minvalue=10, maxvalue=100, initialvalue=30
        )

        # Background choice
        self.background_choice = simpledialog.askstring(
            "Background Choice", "Choose the background layout: \n1. Pong\n2. Air Hockey\n3. Basketball\n4. Football",
            initialvalue="Pong"
        )

        # Initialize the game
        self.initialize_game()

    def initialize_game(self):
        """Set up the game components."""
        # Initialize scores
        self.score1 = 0
        self.score2 = 0

        # Set background
        self.set_game_background()

        # Create paddles
        self.paddle1 = self.canvas.create_rectangle(
            40, (self.canvas_height - self.paddle_height) // 2,
            40 + self.paddle_width, (self.canvas_height + self.paddle_height) // 2,
            fill=self.player1_color
        )
        self.paddle2 = self.canvas.create_rectangle(
            self.canvas_width - 40 - self.paddle_width, (self.canvas_height - self.paddle_height) // 2,
            self.canvas_width - 40, (self.canvas_height + self.paddle_height) // 2,
            fill=self.player2_color
        )

        # Create ball
        self.ball = self.canvas.create_oval(
            (self.canvas_width - self.ball_size) // 2,
            (self.canvas_height - self.ball_size) // 2,
            (self.canvas_width + self.ball_size) // 2,
            (self.canvas_height + self.ball_size) // 2,
            fill=self.ball_color
        )

        # Update scoreboard
        self.update_scoreboard()

        # Initialize ball movement
        self.ball_dx = 0
        self.ball_dy = 0

        # Start paddle movement loop
        self.update_paddles()

    def set_game_background(self):
        """Set the background based on user selection."""
        self.canvas.delete("all")

        if self.background_choice.lower() == "pong":
            self.canvas.create_line(self.canvas_width // 2, 0, self.canvas_width // 2, self.canvas_height, fill="white")
        elif self.background_choice.lower() == "air hockey":
            self.canvas.create_oval(
                self.canvas_width // 2 - 50, self.canvas_height // 2 - 50,
                self.canvas_width // 2 + 50, self.canvas_height // 2 + 50,
                outline="white", width=2
            )
        elif self.background_choice.lower() == "basketball":
            self.canvas.create_oval(
                self.canvas_width // 2 - 100, self.canvas_height // 2 - 100,
                self.canvas_width // 2 + 100, self.canvas_height // 2 + 100,
                outline="white", width=2
            )
        elif self.background_choice.lower() == "football":
            for i in range(0, self.canvas_height, 40):
                self.canvas.create_line(0, i, self.canvas_width, i, fill="white")
        else:
            self.background_choice = "Pong"
            self.set_game_background()

    def start_game(self, event=None):
        """Start the game."""
        if not self.game_active:
            self.game_active = True
            self.ball_dx = random.choice([-1, 1]) * self.ball_speed
            self.ball_dy = random.choice([-1, 1]) * self.ball_speed
            self.update_game()

    def update_game(self):
        """Update the game state."""
        if self.game_active:
            self.move_ball()
            self.update_paddles()
            self.root.after(10, self.update_game)

    def move_ball(self):
        """Move the ball and handle collisions."""
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        if ball_coords[1] <= 0 or ball_coords[3] >= self.canvas_height:
            self.ball_dy = -self.ball_dy

        if self.check_ball_collision(self.paddle1, ball_coords) or self.check_ball_collision(self.paddle2, ball_coords):
            self.ball_dx = -self.ball_dx

        if ball_coords[0] <= 0:
            self.score2 += 1
            self.update_scoreboard()
            self.reset_ball()
        elif ball_coords[2] >= self.canvas_width:
            self.score1 += 1
            self.update_scoreboard()
            self.reset_ball()

    def check_ball_collision(self, paddle, ball_coords):
        """Check for ball-paddle collision."""
        paddle_coords = self.canvas.coords(paddle)
        return (
            ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]
            and ball_coords[3] >= paddle_coords[1] and ball_coords[1] <= paddle_coords[3]
        )

    def reset_ball(self):
        """Reset the ball to the center of the canvas."""
        self.canvas.coords(
            self.ball,
            (self.canvas_width - self.ball_size) // 2, (self.canvas_height - self.ball_size) // 2,
            (self.canvas_width + self.ball_size) // 2, (self.canvas_height + self.ball_size) // 2
        )
        self.ball_dx = random.choice([-1, 1]) * self.ball_speed
        self.ball_dy = random.choice([-1, 1]) * self.ball_speed

    def update_scoreboard(self):
        """Update the scoreboard."""
        self.score_label.config(
            text=f"{self.player1_name}: {self.score1}   {self.player2_name}: {self.score2}"
        )

    def set_paddle_direction(self, player, direction):
        """Set paddle direction."""
        if player == 1:
            self.paddle1_direction = direction
        elif player == 2:
            self.paddle2_direction = direction

    def update_paddles(self):
        """Move paddles based on direction."""
        self.move_paddle(self.paddle1, self.paddle1_direction)
        self.move_paddle(self.paddle2, self.paddle2_direction)
        self.root.after(10, self.update_paddles)

    def move_paddle(self, paddle, direction):
        """Move a paddle vertically."""
        if direction != 0:
            self.canvas.move(paddle, 0, direction * self.paddle_speed)
            paddle_coords = self.canvas.coords(paddle)

            if paddle_coords[1] < 0:
                self.canvas.move(paddle, 0, -paddle_coords[1])
            elif paddle_coords[3] > self.canvas_height:
                self.canvas.move(paddle, 0, self.canvas_height - paddle_coords[3])

    def reset_game(self, event=None):
        """Reset the game while keeping settings."""
        self.game_active = False
        self.initialize_game()

    def reset_to_config(self, event=None):
        """Reset the game and reconfigure settings."""
        self.game_active = False
        self.configure_game()
        self.initialize_game()


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
