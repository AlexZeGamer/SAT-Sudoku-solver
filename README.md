# SAT Sudoku solver
A SAT-based Sudoku solver made in the context of a small project in the "Logic Problem Solving" class in the first year at the Polytech Paris-Saclay engineering school

## Requirements
`pip install -r requirements.txt`
* Solver made using [pycosat](https://pypi.org/project/pycosat/) and a bit of [numpy](https://pypi.org/project/numpy/)
* GUI made using [tkinter](https://docs.python.org/3/library/tkinter.html)

## Run tests
Download the [1 million Sudoku games dataset](https://www.kaggle.com/datasets/bryanpark/sudoku) by [@Kyubyong](https://github.com/Kyubyong) (`sudoku.csv`)

Run `solver.py` to run the tests

## GUI
Run `main.py` to enter any soduku puzzle and solve it

![image](https://user-images.githubusercontent.com/54336210/163556329-536ebea2-ed9f-495d-b3dd-bd56274e337e.png)
![image](https://user-images.githubusercontent.com/54336210/163556372-1e81b11a-fc9d-4622-9931-6d8f3f625ff9.png)

## Credits
Co-developed by:
* [Alexandre Malfreyt](https://github.com/AlexZeGamer)
* [Esteban Bruneau](https://github.com/Esteboss)

## TODO
- [x] Coding every constraints from sudoku rules (see [here](https://www.sudokuwiki.org/Sudoku_rules)) into a CNF formula
  - [x] Solving sudoku using pycosat
- [x] Testing using a sudoku dataset
  - [x] Timing the `solve()` function
- [x] GUI using tkinter
  - [x] Make sure we can only enter numbers 1-9 in the GUI
  - [x] Show a popup if the sudoku grid has no solution
  - [ ] Separate every 3x3 sub-grid
- [x] Generate sudoku grids
  - [ ] Generate sudoku grids using a CNF
- [ ] Count the number of solutions
- [ ] Working with n^2 * n^2 sudoku grids
