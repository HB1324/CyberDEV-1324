import tkinter as tk
from tkinter import messagebox
from typing import List, Optional


class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # 9x9 Entry Grid
        self.entries = [[tk.Entry(root, width=3, font=('Arial', 18), justify='center') for _ in range(9)] for _ in
                        range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Solver
        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

    def get_puzzle(self) -> List[List[int]]:
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            puzzle.append(row)
        return puzzle

    def set_puzzle(self, solution: List[List[int]]):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(solution[i][j]))

    def solve(self):
        puzzle = self.get_puzzle()
        solution = solve_sudoku(puzzle)

        if solution:
            self.set_puzzle(solution)
            messagebox.showinfo("Sudoku Solver", "Puzzle solved!")
        else:
            messagebox.showwarning("Sudoku Solver", "No solution exists for the given puzzle.")


def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board: List[List[int]]) -> Optional[List[List[int]]]:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return board
                        board[row][col] = 0
                return None
    return board


# GUI APP
root = tk.Tk()
app = SudokuSolverApp(root)
root.mainloop()