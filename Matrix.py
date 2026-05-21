

arr = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
] 
  
x1, y1 = 1, 1 
x2, y2 = 2, 2 
  
total = 0 
  
for i in range(x1 - 1, x2): 
    for j in range(y1 - 1, y2): 
        total += arr[i][j] 
  
print("Sum of submatrix:", total)