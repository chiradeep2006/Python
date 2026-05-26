arr = ["flower", "flow", "flight"] 
  
prefix = arr[0] 
  
for word in arr[1:]: 
    while word[:len(prefix)] != prefix: 
        prefix = prefix[:-1] 
  
        if prefix == "": 
            break 
  
print(prefix)