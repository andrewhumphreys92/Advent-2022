import sys

if len(sys.argv) != 2:
    sys.exit("Don't forget your input!")

file = open(sys.argv[1], "r")

pairs = [[]]
sublist = []
list = []
total = 0

x = 0

for line in file:
    line = line.strip()
    d = line.split(',')

    e = d[0].split('-')
    f = d[1].split('-')
    for number in range(len(e)):
        e[number] = int(e[number])
    for number in range(len(f)):
        f[number] = int(f[number])
    pairs[x].append(e)
    pairs[x].append(f)
    x += 1
    pairs.append([])

for pair in pairs:
    for duplet in pair:
        for i in range(duplet[0], duplet[1] + 1):
            sublist.append(i)
        list.append(sublist)
        sublist = []

for i in range(0, len(list), 2):
    if len(list[i]) > len(list[i + 1]):
        result = all(elem in list[i] for elem in list[i + 1])
        if result:
            total += 1
    else:
        result = all(elem in list[i + 1] for elem in list[i])
        if result:
            total += 1

print(total)