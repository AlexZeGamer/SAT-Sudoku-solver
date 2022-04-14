import itertools as it
import pycosat as sat
import numpy as np
from utils import *

n = 3*3
A = np.arange(1, 9**3+1).reshape((9, 9, 9))

# ------------------------ #
#  ADDING CNF CONSTRAINTS  #
# ------------------------ #

"""Adds the statement grid constraints to the CNF"""
def set_initial_grid(quiz):
    cnf = []
    for digit in range(1,9+1):
        for i in range(9):
            for j in range(9):
                if quiz[i,j] == digit:
                    cnf += [[int(A[i,j,digit-1])]]
                elif quiz[i,j] != 0:
                    cnf += [[-int(A[i,j,digit-1])]]
    return cnf

"""Adds the constraint that a digit is the only one in its row or column"""
def check_row_or_column(digit: int):
    cnf = []
    for i in range(9):
        for j in range(9):
            cnf += exactly_one(A[i,:,digit-1].tolist())
            cnf += exactly_one(A[:,j,digit-1].tolist())
    return cnf

"""Adds the constraint that a digit is the only one in its 3x3 square"""
def check_3x3_squares(digit: int):
    cnf = []
    for sq_i in range(3):
        for sq_j in range(3):
            cnf += exactly_one(A[sq_i*3:sq_i*3+3, sq_j*3:sq_j*3+3, digit-1].flatten().tolist())
    return cnf

"""Adds the constraint that there is at least one digit in each box"""
def check_digit():
    cnf = []
    for i in range(9):
        for j in range(9):
            cnf += exactly_one(A[i,j].flatten().tolist())
    return cnf

# -------

"""build the cnf corresponding to sudoku rules"""
def build_cnf(quiz):
    quiz = np.array(quiz)
    
    # create cnf by adding every constraint
    cnf = []
    cnf += set_initial_grid(quiz)
    for digit in range(1,9+1):
        cnf += check_row_or_column(digit)
        cnf += check_3x3_squares(digit)
    cnf += check_digit()
    return cnf

"""9x9x9 3D binary grid > 9x9 2D decimal grid"""
def bin_to_dec_grid(grid):
    grid = np.array(grid).reshape((9, 9, 9))
    
    grid = np.array([
        # digit that belongs in sol[i,j]
        # (ie. index of first positive value in sol[i,j] + 1)
        int(np.where(grid[i, j] > 0)[0]) + 1
        for i, j in it.product(range(9), range(9))
    ])
    
    grid = grid.reshape((9, 9))
    return grid

"""
Solve a sudoku grid
quiz : 9x9 2D decimal grid (np.array)
"""
def solve(quiz):
    cnf = build_cnf(quiz)
    
    sol = sat.solve(cnf)
    if sol == 'UNSAT':
        return None
    
    return bin_to_dec_grid(sol)

"""
Give n solution to a sudoku grid
/!\ This function can be very slow (should not be used for a high n value)
quiz : 9x9 2D decimal grid (np.array)
"""
def solve_n(quiz, n):
    cnf = build_cnf(quiz)
    
    sols = list(it.islice(sat.itersolve(cnf), n))
    if sols == 'UNSAT':
        return None

    return [
        bin_to_dec_grid(sol)
        for sol in sols
    ]

"""
Give every solution to a sudoku grid
/!\ This function is very slow (should not be used)
quiz : 9x9 2D decimal grid (np.array)
"""
def solve_all(quiz):
    cnf = build_cnf(quiz)
    
    sols = sat.itersolve(cnf)
    if sols == 'UNSAT':
        return None

    return [
        bin_to_dec_grid(sol)
        for sol in sols
    ]



# testing
if __name__ == '__main__':
    from get_examples import get_examples
    import random
    from time import time
    
    nb = 100 # number of tests to run
    times = [] # list of times to run each test
    quizzes, solutions = get_examples(nb)
    
    for i in range(nb):
        grid_nb = random.randint(0, len(quizzes)-1) # random grid
        print(f'Test #{i+1}', end='\r')
        
        start = time()
        cnf = solve(quizzes[grid_nb])
        times += [time() - start]
        
        assert(solve(quizzes[grid_nb]).all() == solutions[grid_nb].all())
        
    print(f'All {nb} tests passed ! 🎉')
    print(f'Minimum time : {min(times)}')
    print(f'Maximum time : {max(times)}')
    print(f'Average time : {sum(times)/len(times)}')
