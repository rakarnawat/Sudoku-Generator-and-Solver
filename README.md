# Sudoku-Generator-and-Solver
Python is used to complete the project.

In this project, three libraries were used, and they are as follows:
1. time   : it is used to let the program wait for 3 seconds before exiting.
2. turtle : it is used for building gui.
3. random : it is used to randomly choose number from the list of 1 to 9 and it is  also used to generate sudoku by randomly choosing nuber between 0 to 81 and then randomly choosing the position for that number and then making it zero.

The programme uses large floating point numbers (for eg: -275.77569) because the x, y axis are first plotted on a graph sheet before the sudoku grid is created on the GUI.

In this project, the sudoku puzzle can be generated as many as desired. Even after the sudoku has been solved, the puzzle can be generated by simply clicking on generate sudoku.

Along with the project file, the folder also contains an exe file and a video demonstrating the active project.

Project output from the console:
-----------------
Initial sudoku:
4 6 1 0 0 0 0 0 0 
2 3 9 0 0 0 0 0 0 
8 7 5 0 0 0 0 0 0 
0 0 0 8 7 4 0 0 0 
0 0 0 9 6 3 0 0 0 
0 0 0 2 5 1 0 0 0 
0 0 0 0 0 0 4 9 3 
0 0 0 0 0 0 5 8 7 
0 0 0 0 0 0 2 6 1 
-----------------
valid sudoku:
4 6 1 3 2 5 8 7 9 
2 3 9 1 8 7 6 4 5 
8 7 5 4 9 6 3 1 2 
1 2 3 8 7 4 9 5 6 
5 4 7 9 6 3 1 2 8 
6 9 8 2 5 1 7 3 4 
7 8 6 5 1 2 4 9 3 
3 1 2 6 4 9 5 8 7 
9 5 4 7 3 8 2 6 1 
-----------------
generated sudoku:
0 6 0 3 0 5 0 0 0 
2 3 0 0 0 7 0 4 0 
0 0 5 0 9 0 3 0 0 
1 2 0 8 0 0 0 0 6 
0 4 7 0 0 0 0 2 0 
0 9 0 0 0 0 7 0 4 
0 0 6 5 0 0 0 0 0 
3 0 0 6 0 0 5 0 0 
9 5 4 0 0 0 0 0 0 
-----------------
solved sudoku:
4 6 1 3 2 5 8 7 9 
2 3 9 1 8 7 6 4 5 
7 8 5 4 9 6 3 1 2 
1 2 3 8 7 4 9 5 6 
5 4 7 9 6 3 1 2 8 
6 9 8 2 5 1 7 3 4 
8 1 6 5 3 2 4 9 7 
3 7 2 6 4 9 5 8 1 
9 5 4 7 1 8 2 6 3 