# arr = [0,0,1,2,0,3,0,0,4]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] == 0:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)



# input = [3,4,-1,1]
# for i in range (len(input)):
#     if input[i] <=0 :
#         print(i)


# Permutation

# class Solution(object):
#     input = [1,2,3]
#     def permute(self, nums):
#         result = []
#         self.backtrack(nums,[],result)
#         return result
#     def backtrack(self,nums,path,result):
#         if not nums:
#             result.append(path)  
#         for i in range(len(nums)):
#             self.backtrack(nums[:i]+nums[i+1:],path+[nums[i]],result)

    
# s = Solution()
# print(s.permute(s.input))   




# try: 
#     a = int (input("Enter the number : "))
#     b = int (input("Enter the number : "))
#     print (a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input, please enter a number")
# # except :
# #     print("An error occurred")
# finally:
#     print("This block will always execute")
# else:
#     print ("Everything is ok")


# except(ZeroDivisionError, ValueError) as msg:  # multiple exception handling in single except block
    # print(msg)


# import csv
# f = open("employee.csv",'a')
# a = csv.writer(f)
# # a.writerow(["EmpID","EmpName","EmpAge"])
# print("file created successfully")
# empid = int(input("Enter Employee ID : "))
# empname = input("Enter Employee Name : ")
# empage = int(input("Enter Employee Age : "))
# a.writerow([empid,empname,empage])
# print("Data written successfully")

import csv
a= open("student.csv",'a')
r = csv.writer(a)
# r.writerow(["stuID","stuName","physics","chemistry","maths","total","percentage","result"])
print("file created successfully")
stuID = int(input("Enter Student ID : "))
stuName = input("Enter Student Name : ")    
physics = int(input("Enter marks in Physics : "))
chemistry = int(input("Enter marks in Chemistry : "))
maths = int(input("Enter marks in Maths : "))
total = physics + chemistry + maths
percentage = total/3
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"
r.writerow([stuID,stuName,physics,chemistry,maths,total,percentage,result])
print("Data written successfully")