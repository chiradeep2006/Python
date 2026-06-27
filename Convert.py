k = int(input())
A = input()
B = input()

if len(A) != len(B):
    print("No")
else:
    changes = sum(1 for i in range(len(A)) if A[i] != B[i])

    if changes <= k:
        print("Yes")
    else:
        print("No")