# def func(value, values):
#     var = 1 
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t, v[0])


# def f(i, values = []):  #[1][1,2][1,2,3]
#     values.append(i)
#     print(values)
#     #return values
# f(1)# calling function
# f(2)
# f(3)


# fruit = {}   #{'Apple':1,'banana':1,'apple':1}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone("Apple")
# addone("banana")
# addone("apple")
# print(len(fruit))


# Q.write a proogram to accept student name and marks from the kyboard and creates a dictionary. also display student marks by taking student name.

# n = int(input("Enter the number of students : "))
# d={}
# for i in range(n):
#     name = input("Enter the name of student : ")
#     marks = int(input("Enter the marks of student : "))
#     d[name] = marks  # add Key:value
# while True:
#     name = input("Enter the name of student to get marks : ")
#     marks = d.get(name, -1)
#     if marks == -1:
#         print("Student not found")
#     else:
#         print(f"{name} has scored {marks} marks")
#     options = input("Do you want to continue (y/n) : ")
#     if options ==  "n":
#         break
# print("Thank you for using the program")    
    

# Q. write a program to access each character of a string in forward and backward direction. by using while loop.
    # i/p = "learning python is very easy "

# s = "learning python is very easy "
# i = 0
# while i < len(s):
#     print(s[i], end=" ")
#     i += 1
# print("Forward direction")
# i = len(s) - 1
# while i >= 0:
#     print(s[i], end=" ")
#     i -= 1
# print("Backward direction")



# v = ['a','e','i','o','u']
# w = input("Enter any word where we will search for vowels : ")
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print("Vowels found in the word are : ", found)
# print("Unique vowels ", len(found),"from the given word=",w)


# x,y,z = map(int, input().split())
# mylist =[]
# for i in range(x):
#     a = int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
#         print(j, end=" ")


# import datetime
# date = datetime.datetime.now()
# print("It's Now :{:%d-%m-%Y %H:%M:%S}".format(date))


# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(x == y) 
# print(x == z)
# print(x != z)


# s = [1,4,9,16,25,36,49,64,81,100]
# val = [2**i for i in range(1,6)]
# print(val)


# s=[ i*i for i in range(1,11)]
# print(s) 


#dictionary comprehension
# squares = {i: i*i for i in range(1,6)}
# print(squares)

# doubles = {i: i*2 for i in range(1,6)}
# print(doubles)


# how to read multiple values from the keyboard in a single line .

# a,b = [int(x) for x in input("Enter two numbers : ").split()]
# print("The Product of two numbers is : ", a*b)


# a,b,c = [float(x) for x in input("Enter three float numbers : ").split()]
# print("The sum of three numbers is : ", a+b+c)

# from ast import While


# mycart = [10,20,800,60,70]
# for item in mycart:
#     if item > 500:
#         print("This item is not in my budget")
#         continue
#     print("Item added to cart : ", item)
# else:
#     print("All items have been processed")      
    
# ===============================================================

# username = "admin"
# password = "admin"
# while True:
#     u = input("Enter username : ")
#     p = input("Enter password : ")
#     if u == username and p == password:
#         print("Login successful")
#         break
#     else:
#         print("Invalid username or password")



# Tower of hanoi

import time
class Tower:
    def __init__(self):
        print("Wellcome to Tower of Hanoi Game")
        print()
        print("Given problem A = [3,2,1] B = [] C = []")
        print()
        print("Expectation : A = [] B = [] C = [3,2,1]")
        self.A = []
        self.B = []
        self.C = []

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass one Completed=======================\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 2 Completed=======================\n")

    def pass3(self):
        self.temp = self.A.pop(2)
        self.B.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 3 Completed=======================\n")

    def pass4(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 4 Completed====================\n")

    def pass5(self):
        self.temp = self.B.pop(2)
        self.A.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 5 Completed====================\n")

    def pass6(self):
        self.temp = self.C.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 6 Completed====================\n")

    def pass7(self):
        self.temp = self.C.pop(0)
        self.A.append(self.temp)
        time.sleep(3)
        print("A= ", self.A  ,"  ", "B= ", self.B,"  ", "C= ", self.C)
        print("Pass 7 Completed====================\n")
obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()