map, moves = [], []

direction = { '^' : (-1, 0) , 'v': (1, 0) , '>': (0, 1) , '<': (0, -1) }

def save_input():
    global moves

    file = open('input.txt', 'r')
    lines = file.readlines()

    for row in lines:
        if '#' in row:
            map.append([cell for cell in row.strip()])
        else:
            moves += row.strip()

    file.close()

def move_robot():
    x_robot, y_robot = find_robot()

    for move in moves:
        x_robot, y_robot = move_according_to(x_robot, y_robot, move)

def find_robot():
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == '@':
                return x, y

def move_according_to(x, y, move):
    (dx, dy) = direction[move]

    #hit an object. move recursively
    if map[x+dx][y+dy] == 'O':  
        move_according_to(x+dx, y+dy, move) 

    # check if is possible to move
    if map[x+dx][y+dy] == '.':
        map[x+dx][y+dy], map[x][y] = map[x][y], map[x+dx][y+dy]
        return x+dx, y+dy
    
    return x, y
        
def boxes_gps_coordinates():
    sum = 0

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == 'O':
                sum += 100*x + y
    
    return sum

def main():
    save_input()
    move_robot()
    sum = boxes_gps_coordinates()
    print(sum)

main()