e: 
# Input 
rows = int(input("Enter rows: ")) 
cols = int(input("Enter columns: ")) 
 
mat = [] 
 
print("Enter matrix:") 
 
for _ in range(rows): 
    mat.append(list(map(int, input().split()))) 
 
x = int(input("Enter element to search: ")) 
 
i = 0 
j = cols - 1 
 
found = False 
 
# Process 
while i < rows and j >= 0: 
 
    if mat[i][j] == x: 
        found = True 
        break 
 
elif mat[i][j] > x: 
j -= 1 
else: 
i += 1 
# Output 
print(found)