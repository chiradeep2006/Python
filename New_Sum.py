# Input 
arr1 = list(map(int, input("Enter first number array: 
").split())) 
arr2 = list(map(int, input("Enter second number 
array: ").split())) 
 
i = len(arr1) - 1 
j = len(arr2) - 1 
 
carry = 0 
result = [] 
 
# Process 
while i >= 0 or j >= 0 or carry: 
 
    x = arr1[i] if i >= 0 else 0 
    y = arr2[j] if j >= 0 else 0 
 
    total = x + y + carry 
 
    result.append(total % 10) 
 
    carry = total // 10 
 
    i -= 1 
    j -= 1 
 
result.reverse() 
# Output 
print("Sum array:", result)