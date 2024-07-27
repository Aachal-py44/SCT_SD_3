import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()
        
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(self.root, width=2, font=('Arial', 18), borderwidth=2, relief="solid")
                self.cells[row][col].grid(row=row, column=col, padx=5, pady=5)
    
    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=4, columnspan=2)
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        clear_button.grid(row=9, column=2, columnspan=2)
    
    def get_grid(self):
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.cells[row][col].get()
                if value == '':
                    current_row.append(0)
                else:
                    current_row.append(int(value))
            grid.append(current_row)
        return grid
    
    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    self.cells[row][col].delete(0, tk.END)
                else:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, grid[row][col])
    
    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
    
    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists")
    
    def solve_sudoku(self, grid):
        empty = self.find_empty_location(grid)
        if not empty:
            return True
        row, col = empty
        
        for num in range(1, 10):
            if self.is_safe(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return True
                grid[row][col] = 0
        return False
    
    def find_empty_location(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None
    
    def is_safe(self, grid, row, col, num):
        return (self.not_in_row(grid, row, num) and
                self.not_in_col(grid, col, num) and
                self.not_in_box(grid, row - row % 3, col - col % 3, num))
    
    def not_in_row(self, grid, row, num):
        return num not in grid[row]
    
    def not_in_col(self, grid, col, num):
        for i in range(9):
            if grid[i][col] == num:
                return False
        return True
    
    def not_in_box(self, grid, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if grid[i + box_start_row][j + box_start_col] == num:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()