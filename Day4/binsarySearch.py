def binarySearch(arr, target):
    # pass
    
    low = 0
    high = len(ar) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if ar[mid]== target:
            return mid
            break
        elif ar[mid]>= target:
            high = mid -1
        else:
            low = mid + 1
            
    return -1
ar = [1,3,4,5,6,7,8,9,10]
target = 7
# binarySearch(ar,target)
result = binarySearch(ar,target)
if result != -1:
    print("Element is present at index",result)
else:
    print("Element is not present in array")
    
