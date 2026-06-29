s = input()

total_close = s.count(')')
open_count = 0
close_right = total_close

for i in range(len(s)):
    if s[i] == ')':
        close_right -= 1

    if open_count == close_right:
        print(i)
        break

    if s[i] == '(':
        open_count += 1
else:
    print(-1)