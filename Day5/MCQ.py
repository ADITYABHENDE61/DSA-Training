# def fun(value, values):
#     var = 1
#     values[0] = 44
# t= 3
# v = [1,2,3]
# fun(t,v)
# print(t,v[0])

# ==============================================

# def i(i, values = []):
#     values.append(i)
#     print(values)
# i(1)
# i(2)
# i(3)
# ============================================
# def add_value(i, values=[]):
#     values.append(i)
#     return values

# x = add_value(1)
# x = add_value(2)
# x = add_value(3)

# print(x)
# ============================================

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone("apple")
# addone("banana")
# addone("Apple")
# addone("apple")
# print(len(fruit))

# ====================================================
# import datetime
# date = datetime.datetime.now()
# print("Its now :{:%d-%m-%Y %H:%M:%S}".format(date))

# ======================================================
# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3]
# print(x == y)
# print(x == z)
# print(x != z)

#======================================================
# val = [2**i for i in range(11)]
# print(val)

#========================================================

# s = [i*i for i in range(11)]
# print(s)
# #==========================================================

# square  ={x:x*x for x in range(1,11)}
# print(square)
# # =========================================

# doubles = {x:x*2 for x in range(1,11)}
# print(doubles)

# =====================================================

# a,b = [int(x) for x in input("Enter two numbers: ").split()]
# print("Product is: ",a*b)

# ==========================================
# a,b,c = [float(x) for x in input("Enter three numbers: ").split()]
# print("Sum is: ",(a+b+c))

# ===============================
# mycart =[10,20,800,60,70]
# for item in mycart:
#     if item > 400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("I have bought all the items")
# ==========================================================