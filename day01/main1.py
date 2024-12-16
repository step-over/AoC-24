import heapq

left_list = []
right_list = []

sum = 0

def save_input():
    file = open('input.txt', 'r')
    lines = file.readlines()

    for line in lines:
        numbers = line.split()

        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    file.close()

def sort_lists():
    heapq.heapify(left_list)
    heapq.heapify(right_list)

def calculate_distances():
    global sum
    while left_list:
        sum += abs(heapq.heappop(left_list) - heapq.heappop(right_list))

def main():
    save_input()
    sort_lists()
    calculate_distances()
    print(sum)

main()