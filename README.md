# SAT Sudoku solver
A SAT-based Sudoku solver made in the context of a small project in the "Logic Problem Solving" class in the first year at the Polytech Paris-Saclay engineering school

## Requirements
`pip install -r requirements.txt`
* Solver made using [pycosat](https://pypi.org/project/pycosat/) and a bit of [numpy](https://pypi.org/project/numpy/)
* GUI made using [tkinter](https://docs.python.org/3/library/tkinter.html)

## Run tests
Download the [1 million Sudoku games dataset](https://www.kaggle.com/datasets/bryanpark/sudoku) by [@Kyubyong](https://github.com/Kyubyong) (`sudoku.csv`)

Run `solver.py` to run the tests

## Run GUI
Run `main.py` to enter any soduku puzzle and solve it

![image](https://user-images.githubusercontent.com/54336210/163411198-36622de7-1215-409f-bd8e-4028b0f8818d.png)
![image](https://user-images.githubusercontent.com/54336210/163411170-9e2c8fbd-5c0e-4150-a991-7447a91a62f5.png)

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
- [ ] Generate sudoku grids
- [ ] Count the number of solutions
- [ ] Working with n^2 * n^2 sudoku grids
