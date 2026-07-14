def compareVersion(v1, v2):
    a = list(map(int, v1.split(".")))
    b = list(map(int, v2.split(".")))

    n = max(len(a), len(b))

    while len(a) < n:
        a.append(0)

    while len(b) < n:
        b.append(0)

    for i in range(n):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1

    return 0


# Example
v1 = input("Enter first version: ")
v2 = input("Enter second version: ")

print(compareVersion(v1, v2))