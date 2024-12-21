desired_designs = []

def save_input():
    global towel_patterns

    file = open('input.txt', 'r')
    lines = file.readlines()

    towel_patterns = lines[0].strip().split(', ')

    for design in lines[2:]:
        desired_designs.append(design.strip())
    
    file.close()

def possible_designs():
    global memo 
    memo = {} # memorization because checks repeat for the same design

    amount = 0

    for design in desired_designs:
        amount += is_possible(design)

    return amount

def is_possible(design):  
    if design in memo:
        return memo[design]

    # not saved in memory
    if design == '': 
        return True
    
    possible = False

    for pattern in towel_patterns:
        if design.startswith(pattern):
            possible |= is_possible(design.removeprefix(pattern))

    memo[design] = possible
    return possible

def main():
    save_input()
    amount = possible_designs()
    print(amount)

main()