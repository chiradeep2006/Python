def isPalindrome(s):
    return s == s[::-1]

s = input("Enter string: ")

if isPalindrome(s):
    print("true")
else:
    print("false")