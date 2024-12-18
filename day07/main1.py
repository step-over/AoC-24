equation = []

def proccess_input():
    file = open('input.txt', 'r')
    sum = 0

    for line in file:
        equation = [int(n.strip(':')) for n in line.split(' ')]
        
        if is_possible_to_sum(equation[0], equation[1], 2, equation):
            sum += equation[0]
    
    file.close()
    return sum

def is_possible_to_sum(total, partial, idx, eq):
    if idx == len(eq):
        return total == partial
    elif partial > total: 
        return False 
    else:
        return is_possible_to_sum(total, partial + eq[idx], idx+1, eq) or is_possible_to_sum(total, partial * eq[idx], idx+1, eq)

def main():
    sum = proccess_input()
    print(sum)

main()