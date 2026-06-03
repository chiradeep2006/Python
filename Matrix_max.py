n = int(input()) 
  
weights = list(map(int, input().split())) 
values = list(map(int, input().split())) 
  
capacity = int(input()) 
  
dp = [0] * (capacity + 1) 
  
for i in range(n): 
    for j in range(capacity, weights[i] - 1, -1): 
  
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i]) 
  
print("Maximum Value:", dp[capacity])