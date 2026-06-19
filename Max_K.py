from collections import deque 
 
# Input 
arr = list(map(int, input("Enter array elements: 
").split())) 
k = int(input("Enter window size: ")) 
 
dq = deque() 
result = [] 
 
# Process 
for i in range(len(arr)): 
 
    while dq and dq[0] <= i - k: 
        dq.popleft() 
 
    while dq and arr[dq[-1]] < arr[i]: 
        dq.pop() 
 
    dq.append(i) 
 
    if i >= k - 1: 
        result.append(arr[dq[0]]) 
 
# Output 
print(result) 
