# Input 
arr = list(map(int, input("Enter array elements: 
").split())) 
 
n = len(arr) 
 
result = [1] * n 
 
left = 1 
 
# Left product 
for i in range(n): 
 
    result[i] = left 
    left *= arr[i] 
 
right = 1 
 
# Right product 
for i in range(n - 1, -1, -1): 
 
    result[i] *= right 
    right *= arr[i] 
 
# Output 
print("Product array:", result) 