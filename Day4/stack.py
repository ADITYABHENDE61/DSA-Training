import sys
class Stack:
    def __init__(self, size):
        self.mystack = []
        self.Stacksize = size
        
    def push(self, value):
        if self.isfull():
            print("stack is full")
        else:
            self.mystack.append(value)
            print("value pushed")
        
    def isempty(self):
        if len(self.mystack) == 0   :
            return True
        else:
            return False
        
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(self.mystack.pop())
    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(self.mystack[-1])
    def deletestack(self):
        self.mystack = []
    
    def isfull(self):
        if len(self.mystack) == self.Stacksize:
            return True
        else:
            return False
        
    def display(self):
        print(self.mystack)
size = int(input("Enter the size of stack: "))
obj = Stack(size)
print("stack is created")
while True:
    
    print("1. Push")
    print("2. Display")
    print("3. Pop")
    print("4. Peek")
    print("5. delete stack")
    print("6. Is full")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to push: "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deletestack()
    elif choice == 6:
        obj.isfull()
    else:
        sys.exit()
        