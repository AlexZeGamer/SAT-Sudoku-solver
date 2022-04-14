import numpy as np
from solver import solve
import tkinter as tk

gui = tk.Tk()
gui.title('Sudoku Solver')

# show buttons
buttons = tk.Frame(gui, padx=5, pady=5)
tk.Button(buttons, text='Empty 🗑️', command=lambda: empty()).grid(row=0, column=0)
tk.Button(buttons, text='Solve ⚙️', command=lambda: show_solution()).grid(row=0, column=1)
# tk.Button(buttons, text='Print entries', command=lambda: print(entries)).pack() # DEBUG
# tk.Button(buttons, text='Print grid', command=lambda: print(get_grid())).pack() # DEBUG
buttons.pack(anchor='e') # anchor buttons to the right

# create grid
frame = tk.LabelFrame(gui, text='Sudoku', padx=5, pady=5)
entries = np.array([None]*9*9, dtype=tk.Entry).reshape((9, 9))
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(frame, width=4, justify=tk.CENTER, validatecommand=lambda n: (n.isdigit() or n == '') and len(n) == 1)
        entries[i][j].grid(row=i, column=j)
frame.pack()

"""Get the content of the GUI grid"""
def get_grid():
    grid = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            grid[i,j] = entries[i][j].get() or 0
    return grid

"""Replace empty cells with the/a solution"""
def show_solution():
    sol = solve(get_grid())
    
    if sol is None:
        return
    
    for i in range(9):
        for j in range(9):
            entries[i][j].fg = 'black'
            entries[i][j].delete(0, tk.END) # clear entry
            entries[i][j].insert(0, sol[i,j])

"""Empty grid"""
def empty():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END) # clear entry
            entries[i][j].insert(0, '')

gui.mainloop()
