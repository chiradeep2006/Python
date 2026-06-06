de: 
# Input 
arr = list(map(int, input("Enter binary array: 
").split())) 
k = int(input("Enter k value: ")) 
 
left = 0 
zero_count = 0 
max_len = 0 
 
# Process 
for right in range(len(arr)): 
 
    if arr[right] == 0: 
        zero_count += 1 
 
    while zero_count > k: 
 
        if arr[left] == 0: 
            zero_count -= 1 
 
        left += 1 
 
    max_len = max(max_len, right - left + 1) 
 
# Output 
print("Maximum consecutive 1s:", max_len)