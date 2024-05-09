# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:51:33 2023

@author: Asmaa Youssry
"""

import tkinter as tk #library for gui

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.entries = [] #an empty list to store el entries el hadakhalha lel suduko
        self._create_board()
        self._create_solve_button()

    def _create_board(self): #creates a 9x9 Sudoku board using tk.Entry widgets.
    #It iterates over the rows and columns and creates an entry widget for each cell on the board.
    #The entry widgets are then added to the GUI window using the grid() method,
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.window, width=3)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            self.entries.append(row_entries) #ben store el entries fel list bta3etna

    def _create_solve_button(self):
        solve_button = tk.Button(self.window, text="Solve", command=self._solve)
        solve_button.grid(row=9, columnspan=9) #The button is added to the GUI window using the grid() method

    def _solve(self): #lama nedos 3al solve el function dy bteshtaghal
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = self.entries[i][j] #btakhod el entries widgets w te3mel bihom suduko
                if entry.get().isdigit():
                    row.append(int(entry.get()))
                else:
                    row.append(0)
            board.append(row)

# creates an instance of the SudokuSolver class, passing the Sudoku board to it. 
        solver = SudokuSolver(board)
        solution = solver.solve() #el solve method is called 3shan nehel el suduko

        if solution:
            for i in range(9):
                for j in range(9):
                    entry = self.entries[i][j]
                    entry.config(state='normal')
                    entry.delete(0, tk.END)
                    entry.insert(0, str(solution[i][j]))
                    entry.config(state='disabled')
        else:
            tk.messagebox.showinfo("No Solution")

    def run(self):
        self.window.mainloop()


class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        if self._solve_helper():
            return self.board
        else:
            return None

    def _solve_helper(self):
        next_cell = self._find_empty_cell()
        if not next_cell:
            return True

        row, col = next_cell
        for num in range(1, 10):
            if self._is_valid(num, row, col):
                self.board[row][col] = num

                if self._solve_helper():
                    return True

                self.board[row][col] = 0

        return False

    def _find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def _is_valid(self, num, row, col):
        # Check row
        for j in range(9):
            if self.board[row][j] == num:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True


def main():
    gui = SudokuGUI()
    gui.run()


if __name__ == "__main__":
    main()