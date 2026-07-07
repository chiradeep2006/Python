import string

sentence = input("Enter a sentence: ")

# Convert to lowercase
sentence = sentence.lower()

# Remove punctuation
for char in string.punctuation:
    sentence = sentence.replace(char, "")

# Split into words
words = sentence.split()

# Count frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display in alphabetical order
for word in sorted(frequency):
    print(f"{word}: {frequency[word]}")