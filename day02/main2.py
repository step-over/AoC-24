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

    if safe_ascending_problem_dampener(report) or safe_descending_problem_dampener(report):
        sum += 1

def safe_ascending_problem_dampener(l):
    pass 

def safe_descending_problem_dampener(l):
    bad_level_ascending = (
        x for x, y in zip(l, l[1:]) if x-y <= 0 or x-y > 3
    )

    next(bad_level_ascending(l), None)

def differ_ascending(l):
    return all(y-x > 0 and y-x < 4 for x, y in zip(l, l[1:]))

def main():
    process_input()
    print(sum)

main()