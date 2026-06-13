# Input 
n = int(input("Enter size of first array: ")) 
m = int(input("Enter size of second array: ")) 
 
a = list(map(int, input("Enter first array: ").split())) 
b = list(map(int, input("Enter second array: 
").split())) 
 
dp = [[0] * (m + 1) for _ in range(n + 1)] 
 
# Process 
for i in range(1, n + 1): 
 
    for j in range(1, min(i, m) + 1): 
 
        dp[i][j] = max( 
            dp[i - 1][j], 
            dp[i - 1][j - 1] + a[i - 1] * b[j - 1] 
        ) 
 
# Output 
print("Maximum dot product:", dp[n][m])