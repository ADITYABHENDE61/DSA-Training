import sys
def add():
    a  = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a+b)
    sys.exit()
    
    
def sub():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a-b)
    sys.exit()

def mul():   
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a*b)
    sys.exit()

def div(): 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a/b)
    sys.exit()
    
while True:
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()