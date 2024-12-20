import re
from math import prod

robots = []
n, m = 101, 103

def save_input():
    file = open('input.txt', 'r')
    
    for line in file:
        matches = re.search(r'p=(\d+),(\d+) v=(-*\d+).(-*\d+)', line).groups()
        robots.append(list(map(int, matches)))
    
    file.close()

def move():
    for i, (x, y, vel_x, vel_y) in enumerate(robots):
        robots[i][0] = (x + vel_x) % n
        robots[i][1] = (y + vel_y) % m

def safety_factor():
    quadrant = [0, 0, 0, 0, 0]

    for (x, y, _, _) in robots:
        quadrant[quad(x, y)] += 1
    
    return prod(quadrant[:-1]) # remove last element because quadrant[4] contains robots in the middle

def quad(x, y):
    half_x = n // 2
    half_y = m // 2

    if x == half_x or y == half_y: # robot in the middle
        return 4 
    
    if x < half_x: # left_quadrant
        return 0 if y < half_y else 2
    else:   # right cuadrant
        return 1 if y < half_y else 3

def main():
    save_input()
    for _ in range(100): move()
    total = safety_factor()
    print(total)

main()