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
    m = len(data[0])

    for i in range(n):
        for j in range(m):
            if data[i][j] == 'X':
                sum += is_horizontal_xmas(i,j,m)
                sum += is_vertical_xmas(i,j,n)
                sum += is_diagonal_xmas(i,j,n,m)
    
    return sum
                    
def is_horizontal_xmas(i, j, m):
    res = (j + 3 < m and data[i][j:j+3] == "XMAS")
    res += (j > 3 and data[i][j-3:j] == "XMAS")

    return res

def is_vertical_xmas(i, j, n):
    print(i)
    print(j)
    print(n)
    print(data)

    res = (i + 3 < n and data[i:i+1][j] == "XMAS")
    res += (i > 3 and data[i-3:i][j] == "XMAS")

    return res

def is_diagonal_xmas(i, j, n, m):
    res = (i > 3 and j + 3 < m) and [data[i-d][j+d] for d in range(3)] == "XMAS"
    res += (i > 3 and j > 3) and [data[i-d][j-d] for d in range(3)] == "XMAS"
    res += (i + 3 < n and j > 3) and [data[i+d][j-d] for d in range(3)] == "XMAS"
    res += (i + 3 < n and j + 3 < m) and [data[i+d][j+d] for d in range(3)] == "XMAS"

    return res

def main():
    save_input()
    sum = find_xmas()
    print(sum)

main()