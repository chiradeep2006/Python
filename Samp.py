from collections import defaultdict 
 
# Input 
arr = input("Enter strings: ").split() 
 
groups = defaultdict(list) 
 
# Process 
for word in arr: 
 
    key = ''.join(sorted(word)) 
 
    groups[key].append(word) 
 
# Output 
print(list(groups.values()))