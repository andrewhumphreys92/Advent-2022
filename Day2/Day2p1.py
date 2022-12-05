import sys

if len(sys.argv) != 2:
    sys.exit("Input?!?!?!")

pairs = []
score = 0
file = open(sys.argv[1], "r")

for line in file:
    pairs.append(line.split())

for pair in pairs:
    if pair[0] == "A":
        pair[0] = "rock"
    if pair[0] == "B":
        pair[0] = "paper"
    if pair[0] == "C":
        pair[0] = "scissors"

    if pair[1] == "X":
        pair[1] = "rock"
    if pair[1] == "Y":
        pair[1] = "paper"
    if pair[1] == "Z":
        pair[1] = "scissors"




for pair in pairs:
    if pair[1] == "rock":
        score += 1
        if pair[0] == "scissors":
            score += 6
        if pair[0] == "rock":
            score += 3

    if pair[1] == "paper":
        score += 2
        if pair[0] == "rock":
            score += 6
        if pair[0] == "paper":
            score += 3

    if pair[1] == "scissors":
        score += 3
        if pair[0] == "paper":
            score += 6
        if pair[0] == "scissors":
            score += 3

print(score)
