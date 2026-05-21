def productOfArray(arr):#[1,2,3,4]
    if len(arr) == 0:#4
        return 1
    return arr[0] * productOfArray(arr[1:])
        
print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))