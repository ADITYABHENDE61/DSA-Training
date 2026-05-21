def LinearSearch(Array, Target):
    for i in range(1,len(Array)):
        if(Array[i] == Target):
           return i 
    return -1
Array = [3,8,5,7,6,9,5,65]
Target = 7
result = (LinearSearch(Array, Target))
if result == -1:
    print("Element not found")
else:
    print("Element found at index",result)