text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

max_char = max(frequency, key=frequency.get)

print("Most frequent character:", max_char)
print("Frequency:", frequency[max_char])