import tkinter as tk
from tkinter import simpledialog, messagebox


class ScoreTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Score Tracker")

        # Step 1: Prompt for total rounds and player count
        self.total_rounds = simpledialog.askinteger("Total Rounds", "Enter total number of rounds:")
        self.player_count = simpledialog.askinteger("Player Count", "Enter number of players:")

        if not self.total_rounds or not self.player_count:
            messagebox.showerror("Input Error", "Both rounds and player count are required!")
            self.root.destroy()
            return

        # Step 2: Prompt for player names
        self.player_names = []
        for i in range(self.player_count):
            name = simpledialog.askstring("Player Name", f"Enter name for Player {i + 1}:")
            if name:
                self.player_names.append(name)
            else:
                self.player_names.append(f"Player {i + 1}")

        # Step 3: Create score table
        self.create_score_table()

    def create_score_table(self):
        # Create table headers
        tk.Label(self.root, text="Round", borderwidth=1, relief="solid", width=10).grid(row=0, column=0)
        for col, name in enumerate(self.player_names, start=1):
            tk.Label(self.root, text=name, borderwidth=1, relief="solid", width=10).grid(row=0, column=col)

        # Create table cells
        self.entries = {}
        for round_ in range(1, self.total_rounds + 1):
            tk.Label(self.root, text=f"Round {round_}", borderwidth=1, relief="solid", width=10).grid(row=round_,
                                                                                                      column=0)
            for col in range(1, self.player_count + 1):
                entry = tk.Entry(self.root, width=10, justify='center')
                entry.grid(row=round_, column=col)
                self.entries[(round_, col)] = entry

        # Add a "Calculate Scores" button
        tk.Button(self.root, text="Calculate Scores", command=self.calculate_scores).grid(
            row=self.total_rounds + 1, column=0, columnspan=self.player_count + 1, pady=10
        )

    def calculate_scores(self):
        try:
            scores = {name: 0 for name in self.player_names}
            round_scores = {name: [] for name in self.player_names}  # To track scores by round

            for (round_, col), entry in self.entries.items():
                value = entry.get()
                if value.isdigit():
                    value = int(value)
                    player_name = self.player_names[col - 1]
                    scores[player_name] += value
                    round_scores[player_name].append(value)
                elif value.strip():
                    raise ValueError(f"Invalid score input in Round {round_}, Player {self.player_names[col - 1]}")

            # Prepare total scores and lowest scores
            results = []
            for name in self.player_names:
                total = scores[name]
                lowest = min(round_scores[name]) if round_scores[name] else "N/A"
                results.append(f"{name}: Total = {total}, Game Record = {lowest}")

            # Display total scores and lowest scores
            messagebox.showinfo("Total Scores", "\n".join(results))
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ScoreTrackerApp(root)
    root.mainloop()
