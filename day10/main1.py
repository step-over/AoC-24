from queue import LifoQueue

map = []
n, m = 0, 0

def save_map():
    global n, m

    file = open('input.txt', 'r')

    for line in file:
        map.append([int(x) for x in line.strip()])

    n = len(map)
    m = len(map[0])

def calculate_scores_trailheads():
    sum = 0
    trailheads = get_trailheads()
    
    for begin in trailheads:
        sum += calculates_scores_from(begin)
    
    return sum 

def get_trailheads():
    trailheads = []

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == 0:
                trailheads.append((x,y))

    return trailheads

def calculates_scores_from(begin):
    scores = 0

    visited = [[False for _ in row] for row in map ]

    stack = LifoQueue()
    stack.put(begin)

    while not stack.empty(): # dfs
        (x,y) = stack.get()
        
        visited[x][y] = True

        if (map[x][y] == 9): # trailhead
            scores += 1

        adjacents = adjacents_of(x, y)
            
        for (adj_x, adj_y) in adjacents:
            if (not visited[adj_x][adj_y]):
                stack.put((adj_x, adj_y))

    return scores

def adjacents_of(x, y):
    return [ (x+dx , y+dy) for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)] 
            if x+dx in range(n) and y+dy in range(m) and map[x][y] + 1 == map[x+dx][y+dy] ]

def main():
    save_map()
    sum = calculate_scores_trailheads()
    print(sum)

main()    