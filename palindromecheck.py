def isPalindrome(s):
    return s == s[::-1]


# Example
s = input("Enter a string: ")

if isPalindrome(s):
    print("True")
else:
    print("False")