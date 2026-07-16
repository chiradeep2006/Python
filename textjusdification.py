def justifyText(words, L):
    result = []
    i = 0

    while i < len(words):
        line = []
        length = 0

        while i < len(words) and length + len(words[i]) + len(line) <= L:
            line.append(words[i])
            length += len(words[i])
            i += 1

        if i == len(words) or len(line) == 1:
            text = " ".join(line)
            text += " " * (L - len(text))
        else:
            spaces = L - length
            gaps = len(line) - 1
            even = spaces // gaps
            extra = spaces % gaps

            text = ""
            for j in range(gaps):
                text += line[j]
                text += " " * (even + (1 if j < extra else 0))
            text += line[-1]

        result.append(text)

    return result


# Example
words = input("Enter words: ").split()
L = int(input("Enter line width: "))

for line in justifyText(words, L):
    print(line)