import time
import turtle
import random

TURTLE_SIZE = 20
screen = turtle.Screen()
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p1.speed(0)
p1.penup()
p2.penup()
p3.penup()
p1.goto(-300, 300)
p2.speed(0)
p1.hideturtle()
p3.hideturtle()
p2.hideturtle()
p3.color('Black')
p3.pensize(10)
x_axis=-80.77569
y_axis=268.96651-10*50
p3.goto(x_axis, y_axis)
p3.write("Generated sudoku grid", font='bold', align='center')

#create sudoku grid
def box_ui(p1):
    x_axis = -300
    y_axis = 300
    p1.pendown()
    p1.pensize(3)
    while y_axis != -200:
        p1.forward(450)
        p1.penup()
        y_axis = y_axis - 50
        if (y_axis % 3 == 0):
            p1.pensize(3)
        else:
            p1.pensize(1)
        p1.goto(x_axis, y_axis)
        p1.pendown()

    p1.penup()
    p1.pensize(3)
    p1.goto(-300, 300)
    p1.pendown()
    y_axis = -150
    while x_axis != 200:
        p1.goto(x_axis, y_axis)
        p1.penup()
        x_axis = x_axis + 50
        if (x_axis % 3 == 0):
            p1.pensize(3)
        else:
            p1.pensize(1)
        p1.goto(x_axis, 300)
        p1.pendown()
    p1.penup()


box_ui(p1)

# create 2d array
rows = 9
cols = 9
grid = []

# append array into another array to create 2d array
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    grid.append(col)

# print ui grid
def print_grid_ui(grid):
    y_axis = 272.83388
    p2.goto(-273.73412, 272.83388)
    p2.color('Red')
    for i in range(0, 9):
        for j in range(0, 9):
            p2.write(grid[i][j])
            p2.forward(50.3)
        y_axis = y_axis - 50.3
        p2.goto(-273.73410, y_axis)

# print the 2d array
def print_grid(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            print(grid[i][j], end=" ")
        print("")

p2.pensize(3)


# remove elements from UI and write the number on that place
def remove_ui_element(row, col, num):
    x_axis = -273.77569+col*49
    y_axis = 268.96651-row*50
    p2.goto(x_axis, y_axis)
    p2.color('white')
    p2.begin_fill()
    p2.goto(x_axis, y_axis-2)
    p2.backward(5)
    for v in range(0, 4):
        p2.forward(23)
        p2.left(90)
    p2.end_fill()
    p2.getscreen().update()
    if num == 0:
        p2.color('Red')
    else:
        p2.color('Green')
    p2.write(num,font='bold')

#fill the diagonal elements first
def fill_diagonal(grid, inc1, inc2, y_axis, x_axis):
    pl1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 3):
        p2.goto(x_axis, y_axis)
        y_axis = y_axis - 51.5
        for j in range(0, 3):
            a = random.choice(pl1)
            pl1.remove(a)
            grid[i + inc1][j + inc2] = a
            p2.getscreen().update()
            p2.color('white')
            p2.begin_fill()
            p2.backward(1)
            for v in range(0, 4):
                p2.forward(20)
                p2.left(90)
            p2.end_fill()
            p2.getscreen().update()
            p2.color('Green')
            p2.write(a, font='bold', align='center')
            p2.forward(50.6)
        p2.getscreen().update()

# ----------------------------------------
# find empty location to fill in the value
def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return row, col
    return False

def check_location_is_safe(grid, row, col, num):
    #check in row
    for i in range(0,9):
        if grid[row][i] == num:
            return False
    #check in column
    for i in range(0,9):
        if grid[i][col] == num:
            return False
    #check in 3*3 matrix
    for i in range(3):
        for j in range(3):
            if grid[i + (row - row % 3)][j + (col - col % 3)] == num:
                return False
    return True

def valid_sudoku(grid):
    l = [0, 0]
    if find_empty_location(grid, l) == False:
        return True #sudoku done i.e no more null value

    row = l[0]
    col = l[1]
    #num generates number from 1 to 9 and check for safety
    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num)==True:
            grid[row][col] = num
            #print("row: ", row, " Col : ",col, " num : ",num)
            remove_ui_element(row,col,num)
            if valid_sudoku(grid):
                return True
            #on failure return element to 0
            grid[row][col] = 0
    return False #this will trigger backtracking

#remove random element and make it 0
def generate_sudoku(grid):
    r1 = random.randint(1, 81)
    for i in range(0, r1):
        r2 = random.randint(0, 8)
        r3 = random.randint(0, 8)
        if grid[r2][r3] != 0:
            grid[r2][r3] = 0
            remove_ui_element(r2,r3,0)
        else:
            i = i - 1
#solve the sudoku using backtracking
def solve_sudoku(grid):
    l = [0, 0]
    if (find_empty_location(grid, l) == False):
        return True

    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num)==True:
            grid[row][col] = num
            remove_ui_element(row,col,num)
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

#define button structure in ui
def btn_ui(x_axis,y_axis):
    p2.penup()
    p2.goto(x_axis,y_axis)
    p2.pendown()
    p2.goto(x_axis+190,y_axis)
    p2.goto(x_axis+190,y_axis-40)
    p2.goto(x_axis,y_axis-40)
    p2.goto(x_axis,y_axis)
    p2.penup()
    p2.goto(x_axis+95,y_axis-30)

#creates the button in the ui
for i in range(0,5):
    x_axis=-275.77569+9*50
    if i ==0:
        y_axis=273.46651
        btn_ui(x_axis,y_axis)
        p2.write("Initial Sudoku", align='center', font='bold')
    elif i ==1:
        y_axis=273.46651-50
        btn_ui(x_axis,y_axis)
        p2.write("Valid Sudoku", align='center', font='bold')
    elif i==2:
        y_axis=273.46651-100
        btn_ui(x_axis,y_axis)
        p2.write("Generated Sudoku", align='center', font='bold')
    elif i==3:
        y_axis=273.46651-150
        btn_ui(x_axis,y_axis)
        p2.write("Solved Sudoku", align='center', font='bold')
    elif i==4:
        y_axis=273.46651-200
        btn_ui(x_axis,y_axis)
        p2.write("Exit", align='center', font='bold')

#button action on click
def btn_click(x,y):
    global grid
    if -275.77569+9*50 <=x <= -275.77569+9*50+190:
        if 273.46651-40 <=y <= 273.46651:
            x_axis=-80.77569
            y_axis=268.96651-10*50
            p3.goto(x_axis, y_axis)
            p3.color('black')
            p3.clear()
            p3.write("Initial sudoku",font=('bold'),align=('center'))
            for i in range(0, 3):
                if i == 0:
                    axis = (-271.83412, 268.63388)
                    y_axis = axis[1]
                    x_axis = axis[0]
                    inc1 = 0
                    inc2 = 0
                elif i == 1:
                    axis = (-124.71823, 115.87484)
                    x_axis = axis[0]
                    y_axis = axis[1]
                    inc1 = 3
                    inc2 = 3
                else:
                    axis = (26.18394, -35.08419)
                    x_axis = axis[0]
                    y_axis = axis[1]
                    inc1 = 6
                    inc2 = 6

                fill_diagonal(grid, inc1, inc2, y_axis, x_axis)
            print("-----------------\nInitial sudoku:")
            print_grid(grid)
        elif 273.46651-50-40<=y<=273.46651-50:
            x_axis=-80.77569
            y_axis=268.96651-10*50
            p3.goto(x_axis, y_axis)
            p3.write("valid sudoku",font=('bold'),align=('center'))
            valid_sudoku(grid)
            print("-----------------\nvalid sudoku:")
            print_grid(grid)
        elif 273.46651-100-40<=y<=273.46651-100:
            x_axis=-80.77569
            y_axis=268.96651-10*50
            p3.goto(x_axis, y_axis)
            p3.write("generated sudoku",font=('bold'),align=('center'))
            generate_sudoku(grid)
            print("-----------------\ngenerated sudoku:")
            print_grid(grid)
        elif 273.46651-150-40<=y<=273.46651-150:
            x_axis=-80.77569
            y_axis=268.96651-10*50
            p3.goto(x_axis, y_axis)
            p3.write("solved sudoku",font=('bold'),align=('center'))
            solve_sudoku(grid)
            print("-----------------\nsolved sudoku:")
            print_grid(grid)
        elif 273.46651-200-40<=y<=273.46651-200:
            x_axis=-20
            y_axis=75
            p3.goto(x_axis, y_axis)
            p3.clear()
            p2.clear()
            p1.clear()
            p3.write("Thank You!",font=('bold',30),align=('center'))
            time.sleep(3)
            exit(0)
    p3.clear()

print_grid_ui(grid)

screen.onclick(btn_click)

turtle.done()
