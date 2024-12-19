import re
from sympy import symbols, Eq, solve

def process_input():
    total = 0

    file = open('input.txt', 'r')
    lines = file.readlines()

    for i in range(0, len(lines), 4):
        lineA_matches = re.search(r'Button A: X\+(\d+), Y\+(\d+)', lines[i]).groups()
        buttonA_x , buttonA_y = int(lineA_matches[0]) , int(lineA_matches[1])

        lineB_matches = re.search(r'Button B: X\+(\d+), Y\+(\d+)', lines[i+1]).groups()
        buttonB_x , buttonB_y = int(lineB_matches[0]) , int(lineB_matches[1])

        prize_matches = re.search(r'Prize: X=(\d+), Y=(\d+)', lines[i+2]).groups()
        end_x , end_y = int(prize_matches[0]) , int(prize_matches[1])

        total += minimize_solver(buttonA_x, buttonA_y, buttonB_x, buttonB_y, end_x, end_y)

    file.close()

    return total

def minimize_solver(buttonA_x, buttonA_y, buttonB_x, buttonB_y, end_x, end_y):
    # This solver doesnt minimize, only solves the linear equations. I dont know why it works 

    # Define symbolic variables
    a, b = symbols('a b', integer=True)

    # Define the equations
    eq1 = Eq(a * buttonA_x + b * buttonB_x, end_x)
    eq2 = Eq(a * buttonA_y + b * buttonB_y, end_y)

    # Solve the system of equations
    solution = solve([eq1, eq2], (a, b))

    if len(solution) > 0: 
        return solution[a]*3 + solution[b]
    else:   # Not possible solution
        return 0

def main():
    total = process_input()
    print(total)

main()