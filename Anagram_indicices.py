from collections import Counter

text = input()
pat = input()

k = len(pat)

p = Counter(pat)
w = Counter(text[:k])

ans = []

if w == p:
    ans.append(0)

for i in range(k, len(text)):
    w[text[i]] += 1
    w[text[i-k]] -= 1

    if w[text[i-k]] == 0:
        del w[text[i-k]]

    if w == p:
        ans.append(i-k+1)

print(ans)