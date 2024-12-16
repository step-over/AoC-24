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

def calculate_similarity_score():
    global sum
    for number in left_list:
        sum += number * right_list.count(number)

def main():
    save_input()
    calculate_similarity_score()
    print(sum)

main()