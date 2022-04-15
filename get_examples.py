import numpy as np

# 1 million sudoku games dataset by BryanPark
# https://www.kaggle.com/datasets/bryanpark/sudoku

"""Get the examples from the sudoku.csv file"""
def get_examples(nb = 100):
    # We create empty arrays to store nb grids
    quizzes = np.zeros((nb, 81), dtype=np.int32)
    solutions = np.zeros((nb, 81), dtype=np.int32)
    
    # We fetch the grids from the dataset
    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:nb+1]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    
    # Reshape the arrays into an array of nb 9x9 2D decimal grids
    quizzes = quizzes.reshape((nb, 9, 9))
    solutions = solutions.reshape((nb, 9, 9))
    
    return quizzes, solutions