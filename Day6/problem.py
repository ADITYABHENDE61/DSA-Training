# reverse a string

# s = "Hello World"
# words = s.split()      # Split string into words
# reversed_words = [word[::-1] for word in words]   # Reverse each word
# result = " ".join(reversed_words)   # Join words back into string

# print(result)


# sort the list in ascending order

# arr = []
# n = int(input("Enter the number of elements in the list :"))
# for i in range(n):
#     element = int(input("Enter an element :"))
#     arr.append(element)

# arr = [5, 2, 9, 1, 5, 6]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)


# Selection Sort Algorithm

# arr = [5, 2, 9, 1, 8, 6]
# for i in range(len(arr)):
#     min = i
#     j = i + 1
#     while j < len(arr):
#         if arr[j] < arr[min]:
#             min = j
#         j += 1
#     arr[i], arr[min] = arr[min], arr[i]
# print(arr)


# find all the duplicates in the list
# arr = [4,3,2,7,8,2,1,5,5]
# duplicates = []               
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in duplicates:
#             duplicates.append(arr[i])
# print("Duplicates in the list are:", duplicates)


# Sort Dictionary by key values
# input = {"C": 3, "A": 1, "B": 2}
# sorted_Ascending = dict(sorted(input.items()))
# sorted_Descending = dict(sorted(input.items(), reverse=True))
# print("Sorted dictionary by key values Ascending order :", sorted_Ascending)
# print("Sorted dictionary by key values in descending order:", sorted_Descending)

# types of variables (instance var)

# class New :
#     def __init__(self):
#         self.a = 10
# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# class New:
#     a = 10
#     def __init__(self):
#         self.name = "Prashant"
# obj1 = New()
# obj2 = New()
# obj3 = New()
# New.a = 50
# print(obj1.a)
# print(obj2.a)   
# print(obj3.a)


class College:
    collegename = "Modern College" 
    def __init__(self):
        self.studentname = "Aditya"
principal = College()
teacher = College()
accountant = College()
print("principal :",principal.collegename,"....",principal.studentname)
print("teacher :",teacher.collegename,"....",teacher.studentname)
print("accountant :",accountant.collegename,"....",accountant.studentname)
College.collegename = "HBD"  #static variable change
principal.studentname = "Tanuj" #instance variable change
print("principal :",principal.collegename,"....",principal.studentname)
print("teacher :",teacher.collegename,"....",teacher.studentname)
print("accountant :",accountant.collegename,"....",accountant.studentname)