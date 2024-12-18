map , antinodes = [] , []
n , m = 0 , 0

def save_map():
    global n, m

    file = open('input.txt', 'r')

    for line in file:
        map.append([cell for cell in line.strip()])
        antinodes.append([cell for cell in line.strip()])
    
    n = len(map)
    m = len(map[0])
    
    file.close()
    
def mark_antinodes():
    antennas = antennas_pos()

    for i1, (x1, y1) in enumerate(antennas):
        for (x2, y2) in antennas[i1+1:]:
             if (map[x1][y1] == map[x2][y2]):
                (dx, dy) = (x1-x2, y1-y2)
                
                (ant1x, ant1y) = (x1+dx, y1+dy)
                (ant2x, ant2y) = (x2-dx, y2-dy)
                
                if in_range(ant1x, ant1y):
                    antinodes[ant1x][ant1y] = '#'

                if in_range(ant2x, ant2y):
                    antinodes[ant2x][ant2y] = '#'

def antennas_pos():
    list = []

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if (cell != '.'):
                list.append((x,y))
    
    return list

def in_range(x,y):
    return x in range(n) and y in range(m)

def calculate_antinodes():
    num = 0

    for row in antinodes:
        num += row.count('#')

    return num

def main():
    save_map()
    mark_antinodes()
    num = calculate_antinodes()
    print(num)

main()