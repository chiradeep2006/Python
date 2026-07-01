def backtrack(num, seq):
    if len(num) == 0:
        return len(seq) >= 3

    for i in range(1, len(num)+1):
        if num[0] == '0' and i > 1:
            break

        curr = int(num[:i])

        if curr > 2**31 - 1:
            break

        if len(seq) >= 2:
            s = seq[-1] + seq[-2]

            if curr < s:
                continue

            if curr > s:
                break

        seq.append(curr)

        if backtrack(num[i:], seq):
            return True

        seq.pop()

    return False

s = input()
print("YES" if backtrack(s, []) else "NO")