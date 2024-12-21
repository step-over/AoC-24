from heapq import heapify, heappop, heappush

map = []

movements = { 'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0) }

inf = float('inf')

def save_map():
    file = open('input.txt', 'r')

    for row in file:
        map.append(row.strip())

    file.close()

def dijkstra():
    x, y = find_in_map('S')

    distances = [[ inf for _ in row] for row in map]
    prior_queue = [(0, x, y, 'E')]
    heapify(prior_queue)

    while prior_queue:
        (dist, x, y, facing) = heappop(prior_queue)

        for (x_adj, y_adj, weight, facing_adj) in adjacents_of(x, y, facing):
            if distances[x_adj][y_adj] > dist + weight:      # update shortests paths
                distances[x_adj][y_adj] = dist + weight
                heappush(prior_queue, (distances[x_adj][y_adj], x_adj, y_adj, facing_adj))

    return distances

def adjacents_of(x, y, facing):
    return [ (x+dx, y+dy, weight_moving_from_to(facing, direction), direction) 
            for direction, (dx, dy) in movements.items() if map[x+dx][y+dy] != '#' ]

# not efficient to rotate and not move, so I always consider one forward movement
def weight_moving_from_to(source, end):  
    if source == end:     # no need to rotate
        return 1         
    elif set([source, end]) == set(['E', 'W']) or set([source, end]) == set(['N', 'S']):  # need to rotate 180 degrees
        return 1000*2+1  
    else:                 # need to rotate 90 degrees
        return 1000+1    

def find_in_map(desired_cell):
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == desired_cell:
                return x, y

def main():
    save_map()
    dist = dijkstra()
    x_e, y_e = find_in_map('E')
    print(dist[x_e][y_e])

main()