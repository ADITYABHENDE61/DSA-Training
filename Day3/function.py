# def hello(): #function declaration
#     print("Hello World")
    
# hello() #function calling
# hello() #function calling
# hello()  #function calling

# =================================================================

# def arithmectic():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     sum = a +b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return sum, sub, mul, div

# # print(arithmectic())
# result = arithmectic()
# print("arithmectic is: ", result)
# print("multiply is: ", result[2])

# ==============================================================================================

# def arithmectic(a,b):

#     sum = a +b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return sum, sub, mul, div

# result = arithmectic(5,5)
# print("arithmectic is: ", result)

# ================================================================================

# def credential (username, password):
#     if username == password:
#         print("Login Successfully")
#     else:
#         print("Invalid username or password")
        
# credential(username= "admin",password= "admin")

# ===================================================================================

# def cityName(city= "poona"):
#     print(city)

# cityName("Delhi")
# cityName("Mumbai")
# cityName("Nagpur")
# cityName()

# ====================================================================================

def cityName(*city):
    print(city)
    
cityName("Delhi","Mumbai","Nagpur","poona")

# ======================================================================================

