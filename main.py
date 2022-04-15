import numpy as np
import tkinter as tk

from solver import solve
from generate_grid import generate_grid

# ------- #
#   GUI   #
# ------- #

gui = tk.Tk()
gui.title('Sudoku Solver')

# buttons
buttons = tk.Frame(gui, padx=5, pady=5)
tk.Button(buttons, text='Empty🗑️', command=lambda: empty()).grid(row=0, column=0)
tk.Button(buttons, text='New grid 🔢', command=lambda: set_grid(generate_grid())).grid(row=0, column=1)
tk.Button(buttons, text='Solve ⚙️', command=lambda: show_solution()).grid(row=0, column=2)
# tk.Button(buttons, text='Print entries', command=lambda: print(entries)).grid(row=1, column=0) # DEBUG
# tk.Button(buttons, text='Print grid', command=lambda: print(get_grid())).grid(row=1, column=1) # DEBUG
buttons.pack() # anchor buttons to the center

# create grid
frame = tk.LabelFrame(gui, text='Sudoku', padx=5, pady=5)
entries = np.array([None]*9*9, dtype=tk.Entry).reshape((9, 9))
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(frame, width=4, justify=tk.CENTER)
        entries[i][j].grid(row=i, column=j)
        
        # Make sure the input can only be a digit between 0 and 9 or nothing
        reg = gui.register(lambda n: (n.isdigit() and 1<=int(n)<=9) or n == '')
        entries[i][j].config(validate='key', validatecommand=(reg, '%P'))
        
frame.pack()

"""Get the content of the GUI grid"""
def get_grid():
    grid = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            grid[i,j] = entries[i][j].get() or 0
    return grid
            
"""Fill the GUI grid with a given grid"""
def set_grid(grid):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END) # clear entry
            entries[i][j].insert(0, grid[i,j] if grid[i,j] != 0 else '')

"""Replace empty cells with the/a solution"""
def show_solution():
    sol = solve(get_grid())
    
    if sol is None:
        window = tk.Toplevel()

        label = tk.Label(window, text="This Sudoku grid has no solution !")
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(window, text="Close", command=window.destroy)
        button_close.pack(fill='x')
    
    set_grid(sol)

"""Empty grid"""
def empty():
    set_grid(np.zeros((9, 9)))

gui.mainloop()
