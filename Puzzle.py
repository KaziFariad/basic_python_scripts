import random
import numpy as np
print("========================= THE PUZZLE =========================")

solved_puzzle = []
puzzle = []
numbers = []
square = int(input("Which level (2 -) do you want to play: "))


def solved():
    for i in range(square**2):
        numbers.append(i+1)
    numbers[square**2 - 1] = "-"
    solved_puzzle = np.array(numbers).reshape(-1, square)
    for x in solved_puzzle:
        print(x)


def randomize():
    for i in range(square):
        col = []
        for j in range(square):
            r = random.choice(numbers)
            col.append(r)
            numbers.remove(r)
        puzzle.append(col)


score = 0


def show_puzzle(p=puzzle):
    print("=========" * (square))
    for i in range(size):
        for j in range(size):
            print(" |", str(p[i][j]).ljust(4), end=" ")
            if(j == size-1):
                print(end="| ")
        print("")
    print("========="*(square))


def position_of_x(x="-"):
    for i in range(size):
        for j in range(size):
            if(puzzle[i][j] == x):
                return i, j


def side_queries(x="-"):
    x, y = position_of_x()
    global l
    l = []
    if(x > 0):
        l.append(puzzle[x-1][y])
    if(x < size-1):
        l.append(puzzle[x+1][y])
    if(y > 0):
        l.append(puzzle[x][y-1])
    if(y < size-1):
        l.append(puzzle[x][y+1])
    for i in l:
        print(i, end=" | ")


def swap(a):
    x1, y1 = position_of_x()
    x2, y2 = position_of_x(a)
    puzzle[x1][y1], puzzle[x2][y2] = a, "-"


def is_solved():
    order = 1
    for i in range(size):
        for j in range(size):
            if(puzzle[i][j] == order or order == size*size):
                order += 1
            else:
                return False
    return True


print("Make the following:")
solved()
print("From this one: ")
randomize()
size = len(puzzle)
show_puzzle()
while(not is_solved()):
    print("Pick one from these to move:")
    side_queries()
    inp = int(input("Enter your choice: "))
    while(inp not in l):
        inp = int(input("Enter a valid choice: "))
    swap(inp)
    show_puzzle()
    score += 1

print("You solved in", score, "steps")
