arr = [5,7,8,3,7,8,9,2,3]
count = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[j] == arr[i]:
            count+=1
        
        
print(count)