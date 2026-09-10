sentence = input("Enter sentence: ")

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print(reversed_sentence)