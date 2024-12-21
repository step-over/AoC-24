import re

ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = 0, 1, 2, 3, 4, 5, 6, 7

def save_input():
    global regA, regB, regC, program, n

    file = open('input.txt', 'r')
    lines = file.readlines()

    regA = int(re.search(r'Register A: (\d+)', lines[0]).group(1))
    regB = int(re.search(r'Register B: (\d+)', lines[1]).group(1))
    regC = int(re.search(r'Register C: (\d+)', lines[2]).group(1))
 
    program = [ int(number) for number in lines[4].replace('Program: ', '').split(',') ]
    n = len(program)

    file.close

def run_program():
    output = ''
    ip = 0

    while ip in range(n-1): 
        inst, op = program[ip], program[ip+1]

        out_new, ip = execute_instuction(inst, op, ip)
        output += out_new

    return output

def execute_instuction(inst, op, ip):
    global regA, regB, regC

    output = ''
    ip += 2

    if inst == ADV:
        regA //= 2**combo(op)

    elif inst == BXL:
        regB = regB ^ op 

    elif inst == BST:
        regB = combo(op) % 8

    elif inst == JNZ and regA != 0:
        ip = op

    elif inst == BXC:
        regB = regB ^ regC

    elif inst == OUT:
        output = str(combo(op) % 8)

    elif inst == BDV:
        regB = regA // 2**combo(op)

    elif inst == CDV:
        regC = regA // 2**combo(op)

    return output, ip

def combo(op):
    if op in range(4):
        return op
    elif op == 4:
        return regA 
    elif op == 5:
        return regB
    elif op == 6:
        return regC

def main():
    save_input()
    output = run_program()
    print(','.join(output))

main()