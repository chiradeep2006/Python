def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


# Example
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if isRotation(s1, s2):
    print("True")
else:
    print("False")