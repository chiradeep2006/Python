A = input().split('.')
B = input().split('.')

n = max(len(A), len(B))

A += ['0'] * (n - len(A))
B += ['0'] * (n - len(B))

for i in range(n):
    x = int(A[i])
    y = int(B[i])

    if x > y:
        print(1)
        break
    elif x < y:
        print(-1)
        break
else:
    print(0)