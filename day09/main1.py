disk_map = []
file_pos = {}

def save_disk_map():
    global disk_map

    file = open('input.txt', 'r')
    line = file.readline()

    disk_map = [(id // 2, int(number)) for id,number in enumerate(line) ]

    file.close()

def compact_disk():
    init_pos = 0
    (idx_end, (id_end, num_end)) = list(enumerate(disk_map))[-1]

    for x, (id, num) in enumerate(disk_map):

        if is_file_block(x):
            update_file_pos(init_pos, id, num)
            init_pos += num

        else:
            # fill empty block
            # only empty blocks from start

            while num > 0 and idx_end > x:
                filled = min(num_end, num)

                update_file_pos(id_end, init_pos, filled)

                num -= filled
                num_end -= filled

                # update disk map
                disk_map[idx_end] = (id_end, num_end)

                # update file_block to move if necessary
                if num_end == 0 and idx_end > 1:
                    idx_end -= 2
                    (id_end, num_end) = disk_map[idx_end]
                
                init_pos += filled

def update_file_pos(id, init_pos, length):
    if id not in file_pos:
        file_pos[id] = 0
            
    file_pos[id] += sum(range(init_pos, init_pos + length))

def is_file_block(x):
    return x % 2 == 0

def filesystem_checksum():
    sum = 0

    for id in file_pos:
        sum += file_pos[id] * id

    return sum

def main():
    save_disk_map()
    compact_disk()
    sum = filesystem_checksum()
    print(sum)

main()