m = int(input()) 
a1 = list(map(int, input().split())) 
  
n = int(input()) 
a2 = list(map(int, input().split())) 
  
longest = [] 
  
for i in range(m): 
    for j in range(n): 
  
        temp = [] 
        x = i 
        y = j 
  
        while x < m and y < n and a1[x] == a2[y]: 
            temp.append(a1[x]) 
            x += 1 
            y += 1 
  
        if len(temp) > len(longest): 
            longest = temp 
  
for i in longest: 
    print(i, end=" ") 
