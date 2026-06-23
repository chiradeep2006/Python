words = input().split()
L = int(input())

line = []
length = 0

for word in words:
    if length + len(word) + len(line) > L:
        print(" ".join(line))
        line = []
        length = 0

    line.append(word)
    length += len(word)

if line:
    print(" ".join(line))