rules = []
updates = []

def save_input():
    global rules
    global updates

    file = open('input.txt', 'r')
    for line in file:
        line = line.strip()
        if '|' in line:
            numbers = line.split('|')
            rules.append([numbers[1], numbers[0]])
        elif ',' in line: 
            page = line.split(',')
            updates.append(page)
        else:
            pass

    file.close()

def sum_middle_ordered_updates():
    sum = 0
    
    for update in updates:
        if order_right(update):
            middle = int(len(update)//2)
            sum += int(update[middle])
    
    return sum

def order_right(l):
    return all([x,y] not in rules for x,y in zip(l, l[1:]))

def main():
    save_input()
    sum = sum_middle_ordered_updates()
    print(sum)

main()