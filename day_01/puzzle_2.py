#!/usr/bin/env python 

def main():
    file = open('input.txt','r')

    elves_count = []
    current_elf_count = 0
    for line in file.readlines():
        current_text = line.strip()
        if current_text:
            current_elf_count += int(current_text)
        else:
            elves_count.append(current_elf_count)
            current_elf_count = 0

    if current_elf_count != 0:
        elves_count.append(current_elf_count)

    best_3_elves = sorted(elves_count)[-3:]
    print('best_3_elves = {}'.format(best_3_elves))
    print('Answer = {}'.format(sum(best_3_elves)))

    file.close()


if __name__ == '__main__':
    main()
