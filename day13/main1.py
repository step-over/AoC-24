import re
import math 

inf = math.inf

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
    res = inf

    # Brute force solution
    for a in range(1, 100):  
        for b in range(1, 100):
            if buttonA_x * a + buttonB_x * b == end_x and buttonA_y * a + buttonB_y * b == end_y:
                res = min(res, 3*a +b)
    
    if res == inf: 
        return 0
    else: 
        return res

def main():
    total = process_input()
    print(total)

main()