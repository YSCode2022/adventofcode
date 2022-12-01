

# advent of code
elf_calorie = {}
elf = 0
def parse_input(line):
    global elf_calorie, elf
    if line.strip() == "":
        elf += 1
    else:
        calorie = elf_calorie.get(elf, 0) + int(line.strip())
        elf_calorie[elf] = calorie


if __name__ == "__main__":
    for line in open("puzzle.txt"):
        parse_input(line)

    #print(max(elf_calorie.values()))
    print(sum(sorted(elf_calorie.values(), reverse=True)[:3]))
