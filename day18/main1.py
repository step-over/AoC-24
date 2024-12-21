from queue import Queue

N = 71
END = 1024
INF = float('inf')

corrupted = []
directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

def save_input():
    file = open('input.txt', 'r')
    lines = file.readlines()[0:END]

    for row in lines:
        numbers = row.split(',')
        corrupted.append( (int(numbers[1]), int(numbers[0])) )

    file.close()

def bfs():
    x, y = 0, 0

    distances = [[ INF for _ in range(N)] for _ in range(N)]
    distances[x][y] = 0

    queue = Queue()
    queue.put((x,y))

    while not queue.empty():
        (x,y) = queue.get()

        for (adj_x, adj_y) in adjacents_of(x, y):
            if distances[adj_x][adj_y] == INF:
                queue.put((adj_x, adj_y)) 
                distances[adj_x][adj_y] = distances[x][y]+1
    
    return distances

def adjacents_of(x, y):
    return [ (x+dx, y+dy) for (dx, dy) in directions
            if x+dx in range(N) and y+dy in range(N) and (x+dx, y+dy) not in corrupted ]

def main():
    save_input()
    distances = bfs()
    print(distances[N-1][N-1])

main()