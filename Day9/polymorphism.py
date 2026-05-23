# Python doesn't support constructor overloading and method overloading
# It only supports Operator Overloading

# class RBI:
#     def home_loan(self):
#         print("RBI Home Loan = 8%")


#     def educational_loan(self):
#         print("Educational Loan = 9%")

# class SBI(RBI):
#     def educational_loan(self):
#         print("Educational Loan = 10%")
#         super().educational_loan()

# obj = SBI()
# obj.educational_loan()


#Constructor Overriding 
class RBI:
    def __init__(self):
        print("Parent Class constructor")

class SBI(RBI):
    def __init__(self):
        print("Child Class constructor")

obj = SBI()