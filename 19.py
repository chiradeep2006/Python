numbers = [10, 15, 22, 31, 40, 55, 68]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)