7.pydef largest_histogram(heights): 
 
    stack = [] 
    max_area = 0 
    heights.append(0) 
 
    for i in range(len(heights)): 
 
        while stack and heights[stack[-1]] > heights[i]: 
 
            h = heights[stack.pop()] 
 
            width = i if not stack else i - stack[-1] - 1 
 
            max_area = max(max_area, h * width) 
 
        stack.append(i) 
 
    heights.pop() 
 
    return max_area 
 
 
# Input 
rows = int(input("Enter number of rows: ")) 
cols = int(input("Enter number of columns: ")) 
 
25 
 
mat = [] 
 
print("Enter matrix:") 
 
for _ in range(rows): 
    mat.append(list(map(int, input().split()))) 
 
heights = [0] * cols 
answer = 0 
 
# Process 
for row in mat: 
 
    for i in range(cols): 
 
        if row[i] == 1: 
            heights[i] += 1 
        else: 
            heights[i] = 0 
 
    answer = max(answer, largest_histogram(heights)) 
 
# Output 
print("Maximum rectangle area:", answer)