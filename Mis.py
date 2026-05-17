arr=[1,2,3,5] 
n=len(arr)+1 
expected=0 
for i in range(1,n+1): 
    expected+=i 
actual=0 
for i in arr: 
    actual+=i 
missing=expected-actual 
print("Missing Number:",missing)