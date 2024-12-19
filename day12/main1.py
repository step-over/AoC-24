from collections import deque

map, fenced = [], []
directions = [(0,1), (0,-1), (1,0), (-1,0)]
n, m = 0, 0

def save_map():
    global n, m

    file = open('input.txt', 'r')

    for lines in file:
        map.append(lines.strip())
    
    file.close()

    n = len(map)
    m = len(map[0])


def fencing_regions_price():
    global fenced
    fenced = [[False for _ in row] for row in map ]

    total = 0

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if not fenced[x][y]:
                total += fence_price_for(x, y, cell)
    
    return total

def fence_price_for(r, c, cell):
    area, perimeter = 0, 0

    stack = deque()
    stack.append((r,c))

    while len(stack) > 0: # dfs
        (x,y) = stack.pop()
        fenced[x][y] = True
                     
        shared_sides = shared_sides_number(cell, x, y) 
        perimeter += 4 - shared_sides*2
        area += 1

        adjacents = adjacents_of(cell, x, y)
                        
        for (adj_x, adj_y) in adjacents:
            if (not fenced[adj_x][adj_y] and (adj_x, adj_y) not in stack):
                stack.append((adj_x, adj_y))

    return area * perimeter

def adjacents_of(cell, x, y):
    return [ (x+dx, y+dy) for (dx,dy) in directions if x + dx in range(n) and y + dy in range(m) and map[x+dx][y+dy] == cell ]

def shared_sides_number(cell, x, y):
    return [ map[x+dx][y+dy] == cell and fenced[x+dx][y+dy] for (dx,dy) in directions if x + dx in range(n) and y + dy in range(m)].count(True)

def main():
    save_map()
    total = fencing_regions_price()
    print(total)

main()