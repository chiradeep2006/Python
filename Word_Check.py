def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return 1 if dp[n] else 0


wordDict = ["i", "like", "sam", "sung", "samsung",
            "mobile", "ice", "cream", "icecream",
            "man", "go", "mango"]

print(wordBreak("ilike", wordDict))
print(wordBreak("ilikesamsung", wordDict))