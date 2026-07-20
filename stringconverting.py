def canConvert(A, B, k):
    if len(A) != len(B):
        return "No"

    changes = 0

    for i in range(len(A)):
        if A[i] != B[i]:
            changes += 1

    return "Yes" if changes <= k else "No"


# Example
k = int(input("Enter K: "))
A = input("Enter string A: ")
B = input("Enter string B: ")

print(canConvert(A, B, k))