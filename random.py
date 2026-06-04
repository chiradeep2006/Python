Code: 
r, c = map(int, input().split()) 
  
matrix = [] 
  
for i in range(r): 
    row = list(map(int, input().split())) 
    matrix.append(row) 
  
x, y = map(int, input().split()) 
  
for i in range(0, r, x): 
    for j in range(0, c, y): 
  
        if i + x <= r and j + y <= c: 
  
            total = 0 
  
            for a in range(i, i + x): 
                for b in range(j, j + y): 
                    total += matrix[a][b] 
  
            print(total, end=" ")