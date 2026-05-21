# def recursiveRange(num):  #6 , 5, 4, 3, 2, 1
#     if num <= 0:
#         return 0
    
#     return num + recursiveRange(num-1)
#     #6+5+4+3+2+1

# print(recursiveRange(6))


# someRecursive  Solution

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
print(someRecursive([1,2,3,4], isOdd))
print(someRecursive([4,6,8,9], isOdd))  
print(someRecursive([4,6,8], isOdd))
    
    