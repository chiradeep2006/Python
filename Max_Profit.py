# Input 
arr = list(map(int, input("Enter stock prices: 
").split())) 
 
profit = 0 
 
# Process 
for i in range(1, len(arr)): 
 
    if arr[i] > arr[i - 1]: 
        profit += arr[i] - arr[i - 1] 
 
# Output 
print("Maximum Profit:", profit