map = []
n, m = 0, 0

def save_input():
    global n, m

    file = open('input.txt', 'r')
    for row in file:
        map.append([cell for cell in row.strip()])
    
    file.close()

    n = len(map)
    m = len(map[0])

def mark_guard_path():
    (row_g,col_g)= find_guard()

    while True:
        if at_border(row_g, col_g):
            map[row_g][col_g] = 'X'
            break
        elif facing_obstacle(row_g, col_g):
            guard_turn_right(row_g, col_g)
        else: 
            (row_g, col_g) = move_forward(row_g, col_g)
            

def find_guard():
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell in {'^', 'v', '>', '<'}:
                return (x,y)
            
def at_border(f_g, c_g):
    (next_row, next_col) = next_position_guard(f_g, c_g)
    return not in_range(next_row, next_col)

def facing_obstacle(f_g, c_g):
    (next_row, next_col) = next_position_guard(f_g, c_g)
    return map[next_row][next_col] == '#'

def move_forward(f_g, c_g):
    (next_row, next_col) = next_position_guard(f_g, c_g)
    map[next_row][next_col] = map[f_g][c_g]
    map[f_g][c_g] = 'X'
    
    return (next_row, next_col)
    
def guard_turn_right(f_g, c_g):
    match map[f_g][c_g]:
        case '^':
            map[f_g][c_g] = '>'
        case '>':
            map[f_g][c_g] = 'v'
        case 'v':
            map[f_g][c_g] = '<'
        case '<':
            map[f_g][c_g] = '^'

def next_position_guard(f_g, c_g):
    match map[f_g][c_g]:
        case '^':
            return (f_g-1, c_g)
        case '>':
            return (f_g, c_g+1)
        case 'v':
            return (f_g+1, c_g)
        case '<':
            return (f_g, c_g-1)

def in_range(f_g,c_g):
    return f_g in range(n) and c_g in range(m) 

def count_visited_positions():
    res = 0

    for row in map:
        res += row.count('X')

    return res

def main():
    save_input()
    mark_guard_path()
    res = count_visited_positions()
    print(res)

main()