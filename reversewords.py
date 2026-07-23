def reverseWords(s):
    words = [word for word in s.split('.') if word]
    words.reverse()
    return '.'.join(words)


# Example
s = input("Enter string: ")
print(reverseWords(s))