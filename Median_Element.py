import heapq 
 
# Input 
arr = list(map(int, input("Enter stream elements: 
").split())) 
 
small = [] 
large = [] 
 
result = [] 
 
# Process 
for num in arr: 
 
    heapq.heappush(small, -num) 
 
    heapq.heappush(large, -heapq.heappop(small)) 
 
    if len(large) > len(small): 
        heapq.heappush(small, -heapq.heappop(large)) 
 
    if len(small) > len(large): 
        median = float(-small[0]) 
 
    else: 
        median = (-small[0] + large[0]) / 2 
 
result.append(median) 
# Output 
print("Medians:", result)