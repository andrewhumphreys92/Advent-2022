import sys

if len(sys.argv) != 2:
    sys.exit("you forgot the file!")

allcaloriefoods = []
x = 0
totalcaloriesperelf = 0
calorieintlist = []

with open(sys.argv[1], "r") as f:
    reader = f.readlines()
    for line in reader:
        if line != "\n":
            line = int(line)
            calorieintlist.append(line)
        if line == "\n":
            calorieintlist.append(line)

for foodcalories in calorieintlist:
    if foodcalories == "\n":
        allcaloriefoods.append(totalcaloriesperelf)
        x += 1
        totalcaloriesperelf = 0
    if foodcalories != "\n":
        totalcaloriesperelf = totalcaloriesperelf + foodcalories

print(max(allcaloriefoods))