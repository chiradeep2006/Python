Code: 
arr = [1, 2, 3, 4, 5] 
d = 2 
  
n = len(arr) 
  
d = d % n 
  
arr[:] = arr[d:] + arr[:d] 
  
print(arr)