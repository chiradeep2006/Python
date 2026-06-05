Code: 
# Input 
arr = list(map(int, input("Enter array elements: 
").split())) 
k = int(input("Enter k value: ")) 
 
# Process 
arr.sort() 
 
# Output 
print("Kth smallest element is:", arr[k - 1])