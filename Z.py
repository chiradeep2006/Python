Code: 
arr = [1,2,5,7,-1,-2,-5,-7] 
  
  
found = False 
  
for i in range(len(arr)): 
    for j in range(i + 1, len(arr)): 
        if arr[i] + arr[j] == 0: 
            print("Target found:", arr[i], arr[j]) 
            found = True 
  
if found == False: 
    print("Target not found" 