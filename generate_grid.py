from tkinter import Y

from scipy.fftpack import diff
from solver import solve, solve_all, build_cnf, bin_to_dec_grid
import pycosat as sat
import numpy as np
import random


"""Generate a random grid to be solved
/!\ Not efficient at all (we could have used the SAT solver here)

difficulty: percentage of cells to be empty"""
def generate_grid(difficulty = 25, require_unique_sol = True):
    # calculate the number of cells to empty according to the difficulty
    nb_empty_cells = int(81 * ((100-difficulty)/100))
    
    # generate a random solved sudoku grid
    cnf = build_cnf(np.zeros((9, 9)))
    random.shuffle(cnf)
    grid = sat.solve(cnf)
    grid = bin_to_dec_grid(grid)

    # remove random cells
    for i in range(nb_empty_cells):
        x, y = random.randint(0, 8), random.randint(0, 8)
        
        if grid[x,y] == 0: # if the cell is already empty, try again
            i -= 1
            continue
        
        grid[x, y] = 0
    
    # if there is more than one solution, try again
    if require_unique_sol and len(solve_all(grid)) > 1:
        return generate_grid()
    
    return grid
