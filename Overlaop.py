r, c = map(int, input().split()) 
  
matrix = [] 
  
for i in range(r): 
    row = list(map(int, input().split())) 
    matrix.append(row) 
  
size = 1 
  
while size <= min(r, c): 
  
    for i in range(0, r, size): 
        for j in range(0, c, size): 
  
            if i + size <= r and j + size <= c: 
  
                print("Submatrix of size", size) 
  
                for x in range(i, i + size): 
                    for y in range(j, j + size): 
                        print(matrix[x][y], end=" ") 
                    print() 
  
                print() 
  
    size += 1