arr = [1, 2, 3, 2, 1, 4] 
  
unique = [] 
  
for i in arr: 
    if arr.count(i) == 1: 
        unique.append(i) 
  
unique.sort() 
  
print(unique)