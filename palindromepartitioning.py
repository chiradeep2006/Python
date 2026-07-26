def isPalindrome(s):
    return s == s[::-1]

def partition(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            if isPalindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


# Example
s = input("Enter string: ")

for p in partition(s):
    print(p)