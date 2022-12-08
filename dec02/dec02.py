
"""
Rock: A,X: beats sizzors
Paper: B, Y
Sizzors: C, Z


A Y //draw
B X //lose
C Z //win

"""

draw = {
    "A":"X",
    "B":"Y",
    "C":"Z"
}
loss = {
    "A": "Z", # rock beats sizzors
    "B": "X", # paper beats rock
    "C":"Y" # sizzors beats paper
}

win = {
    "A": "Y", # rock loses to  paper
    "B": "Z", # paper loses to sizzors
    "C": "X" # sizzors loses to  rock
}

draw = {
    "A":"X",
    "B":"Y",
    "C":"Z"
}
starting_points = {
    "X":1,
    "Y":2,
    "Z":3
}
starting_points2 = {
    "A":1,
    "B":2,
    "C":3
}


final_result = {
    "X":0,
    "Y":3,
    "Z":6
}


def parse_input_2(line):
    opponent, result = line.split()
    if result == "Y": # draw
        #choose same token
        myself = draw.get(opponent)
    elif result == "X": #lose
        myself = loss.get(opponent)
    else:
        myself = win.get(opponent)
    total = starting_points.get(myself)
    total += final_result.get(result)
    return total



def parse_input(line):
    opponent, myself = line.split()
    total = starting_points.get(myself)
    if draw.get(opponent) == myself:
        total += 3
    elif loss.get(opponent) == myself:
        total  += 0
    else:
        total += 6
        
    return total

if __name__ == "__main__":
    total_count = 0
    for line in open("puzzle.txt"):
        total_count+= parse_input_2(line)

    print(total_count)

    #print(max(elf_calorie.values()))
    #print(sum(sorted(elf_calorie.values(), reverse=True)[:3]))



