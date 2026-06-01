r, c = map(int, input().split()) 
  
m1 = [] 
  
for i in range(r): 
    row = input().split() 
    m1.append(row) 
  
k = int(input()) 
  
m2 = [] 
  
for i in range(k): 
    row = input().split() 
    m2.append(row) 
  
# Find transpose of M2 
transpose = [] 
  
for i in range(k): 
    temp = [] 
    for j in range(k): 
        temp.append(m2[j][i]) 
    transpose.append(temp) 
  
found = False 
  
53 
 
# Check transpose inside M1 
for i in range(r - k + 1): 
    for j in range(c - k + 1): 
  
        match = True 
  
        for x in range(k): 
            for y in range(k): 
  
                if m1[i + x][j + y] != transpose[x][y]: 
                    match = False 
  
        if match: 
            found = True 
  
if found: 
    for row in m2: 
        print(*row) 
else: 
    print(-1)