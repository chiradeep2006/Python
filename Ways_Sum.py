# Input 
coins = list(map(int, input("Enter coin values: 
").split())) 
target = int(input("Enter target sum: ")) 
 
# DP array 
dp = [0] * (target + 1) 
dp[0] = 1 
 
# Process 
for coin in coins: 
 
    for i in range(coin, target + 1): 
        dp[i] += dp[i - coin] 
 
# Output 
print("Number of ways:", dp[target])