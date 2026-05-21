# s = "Python are high level programing language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# name = "Saurabh"
# sal = 5000
# age = 28
# print("{} sal is {} age is {}".format(name,sal,age))

# name = "racecar"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")     


# #check for anagram 
# vowel = "a,e,i,o,u"
# name = "hello"
# vow = 0
# con = 0
# for i in name:
#     if i in vowel:
#         vow +=1
#     else:
#         con +=1   
# print("vowel =", vow)
# print("consonent =", con)

# s = "the is sentence"
# count = 1
# for i in s:
#     if i == " ":
#         count +=1
# print("Count :",count)


# r = "gasgg54@#vscsd!s'"
# special = 0
# for i in r:
#     if i.isalnum():
#         continue
#     # elif i.isdigit():
#     #     continue
#     else:
#         special +=1
# print("special character :",special)

# print('Saurabh'.isalnum())
# print('Saurabh'.isalpha())
# print('777f'.isdigit()) # only 0 to 9
# print('Saurabh'.islower())
# print('SAURABH'.isupper())
# print('½'.isnumeric()) # everything just like 2/3
# print(' '.isspace())


# ================================================================
# print("Saurabh".find("r"))
# print("Saurabrh".index("r"))

#===============================================================
# n = int(input("Enter the number of row :"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
        
#     print()
# ==============================================================


# for Alphabet print 
# n = int(input("Enter the number of row"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print() 

# =============================================================

# n = int(input("Enter the number of row"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
    
# ==========================================================
# import time
# n = int(input("Enter the number of row"))
# for i in range(1,n+1):
#     print(" "*(n-1),end=" ")
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()
    

# ===========================================================   

# n = [1,2,3,4]
# for i in n:
#     print(i)

# ======================================================

# mytuple = (1,2,3,4,"saurabh","sharma")

# print(mytuple)
# print(type(mytuple))

# mytuple[2] ="sunil"
# print(mytuple)

# ===============================================
# init_tuple =()
# print(init_tuple.__len__())

# a = 'a', 'b'
# b = ('a', 'b')
# print(a == b)

# a = '1','2'
# b = ('3','4')
# print(a+b)


# a = ("saurabh",) *3
# print(type(a))

# a = ((1,2),)*7 
# print(len(a[3:8]))

# ======================================================================================

# mydict = {"rollno":"101","name":"saurabh","age":22,"city":"delhi","101":"Saurabh"}
# print(mydict)
# print(mydict["name"])
# print(mydict["age"])
# print(mydict["city"])
# a = mydict["101"]
# print(a)

# mydict[101]="Motya"
# print(mydict)

# ===========================================================================
# for x in mydict:
#     print(x)

# print()
# for x in mydict.values():
#     print(x)
    
# =======================================================================

# for x , y in mydict.items():
#     print(x,y)

# mydict["mobile"] = "1234567890"
# print(mydict)

# ========================================================

# mydict.pop(101)
# print(mydict)

# ===================================================================

# a = {(1,2):1,(2,3):2}
# print(a[2,3])

# a = {'a':1,'b':2,'c':3}    # this is error 
# print(a['a','b'])

# =================================================================

# mydict = {}
# mydict[(1,2,3)] = 8
# mydict[(4,2,1)]= 10
# mydict[(1,2)]= 12
# sum = 0
# for x in mydict:
#     sum += mydict[x]
# print(sum)
# print(mydict)

# =====================================================================
# box = {}
# jars = {}
# crates = {}
# box['biscult'] = 1
# box ['cake'] =3
# jars ['jam']  = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box']))

# # ===================================================================
# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])
    
# =================================================================

# dict = {'B':97,'A':96,'C':98}
# largest_key = max(dict, key=dict.get)
# print(largest_key)
# =============================================================

# num = 123
# a = num % 10 
# num = num//10
# b  = num%10
# c = num//10
# rev = a*100 + b*10 + c*1
# print(rev)
# ================================================================
Amount = int(input("Enter the withdraw amount: "))
print("100 notes =",Amount//100)
print("50 notes =",(Amount%100)//50)
print("20 notes =",((Amount%100)%50)//20)
print("10 notes =",(((Amount%100)%50)%20)//10)
print("5 notes =",((((Amount%100)%50)%20)%10)//5)
      