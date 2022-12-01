#!/usr/bin/env python 

def main():
    file = open('input.txt','r')

    max_elf_count = 0
    current_elf_count = 0
    for line in file.readlines():
        current_text = line.strip()
        if current_text:
            current_elf_count += int(current_text)
        else:
            max_elf_count = max(max_elf_count, current_elf_count)
            current_elf_count = 0

    if current_elf_count != 0:
        max_elf_count = max(max_elf_count, current_elf_count)

    print('Answer = {}'.format(max_elf_count))

    file.close()


if __name__ == '__main__':
    main()
