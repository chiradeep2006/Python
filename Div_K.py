# Input 
arr = list(map(int, input("Enter array elements: 
").split())) 
k = int(input("Enter k value: ")) 
 
# Process 
if len(arr) % 2 != 0: 
    print(False) 
 
else: 
 
    rem = Counter() 
 
    for num in arr: 
        rem[num % k] += 1 
 
    possible = True 
 
    for r in rem: 
 
        if r == 0: 
            if rem[r] % 2 != 0: 
                possible = False 
 
        elif 2 * r == k: 
if rem[r] % 2 != 0: 
possible = False 
else: 
if rem[r] != rem[k - r]: 
possible = False 
print(possible)