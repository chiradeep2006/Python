def strStr(pattern, text):
    return text.find(pattern)


# Example
pattern = input("Enter pattern: ")
text = input("Enter text: ")

print(strStr(pattern, text))