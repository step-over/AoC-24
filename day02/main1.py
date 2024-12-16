sum = 0

def process_input():
    file = open('input.txt', 'r')
    lines = file.readlines()

    for line in lines:
        report = list(map(int, line.split()))

        calculate_safety(report)

    file.close()

def calculate_safety(report):
    global sum

    if differ_ascending(report) or differ_descending(report):
        sum += 1

def differ_ascending(l):
    return all(y-x > 0 and y-x < 4 for x, y in zip(l, l[1:]))

def differ_descending(l):
    return all(x-y > 0 and x-y < 4 for x, y in zip(l, l[1:]))

def main():
    process_input()
    print(sum)

main()