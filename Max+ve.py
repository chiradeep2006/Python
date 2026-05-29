arr = [1, 10, 5, 2, 7] 
  
max_diff = -1 
  
for i in range(len(arr)): 
    for j in range(i + 1, len(arr)): 
        if arr[i] < arr[j]: 
            if j - i > max_diff: 
                max_diff = j - i 
  
print(max_diff)