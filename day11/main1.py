stones = []

def save_stones():
    global stones

    file = open('input.txt', 'r')
    line = file.readline()

    stones = line.split(' ')

def blink():
    global stones
    evolution = []

    for stone in stones:
        if stone == '0':
            evolution.append('1')

        elif len(stone) % 2 == 0: 
            half = len(stone)//2

            evolution.append(str(int(stone[:half])))
            evolution.append(str(int(stone[half:])))

        else: 
            evolution.append(str(int(stone) * 2024)) 

    stones = evolution

def main():
    save_stones()
    for _ in range(75): blink()
    print(len(stones))

main()

        