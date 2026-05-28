Code: 
arr = [1, 2, 3, 4, 5] 
k = 2 
  
first = arr[0] 
  
temp = arr[1:] 
  
k = k % len(temp) 
  
temp = temp[-k:] + temp[:-k] 
  
result = [first] + temp 
  
print(result)