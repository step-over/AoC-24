import re

sum = 0

def find_mul():
    global sum

    file = open('input.txt', 'r')
    lines = file.readlines()

    for line in lines:
        pattern = r"mul\(([\d]{1,3})\,([\d]{1,3})\)"
        mul = re.findall(pattern, line)

        for (x,y) in mul:
            sum += int(x)*int(y)

def main():
    find_mul()
    print(sum)

main()