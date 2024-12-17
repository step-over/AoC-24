data = []

def save_input():
    global data

    file = open('input.txt', 'r')
    for row in file:
        data.append(row)

    file.close()

def find_xmas():
    sum = 0

    n = len(data)
    m = len(data[0])-1
    directions = [(0,1), (0,-1), (1,0), (-1,0), (-1,1), (-1,-1), (1,-1), (1,1)]

    for i in range(n):
        for j in range(m):
            if data[i][j] == 'X':
                sum += [next_four(i,di,j,dj,n,m) == "XMAS" for (di,dj) in directions].count(True)
    
    return sum

def next_four(i, si, j, sj, n, m):
    letters = [data[i + si*d][j + sj*d] for d in range(4) 
               if i + si*d in range(n) and j + sj*d in range(m)]
    return ''.join(letters)

def main():
    save_input()
    sum = find_xmas()
    print(sum)

main()