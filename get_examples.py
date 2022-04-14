import numpy as np

# 1 million sudoku games dataset by BryanPark
# https://www.kaggle.com/datasets/bryanpark/sudoku

"""Get the examples from the file sudoku.csv"""
def get_examples(nb = 100):
    quizzes = np.zeros((nb, 81), np.int32)
    solutions = np.zeros((nb, 81), np.int32)
    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:nb+1]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))
    
    return quizzes, solutions