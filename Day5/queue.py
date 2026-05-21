import sys

class queue:
    def __init__(self, size):
        self.myqueue = []
        self.queuesize = size
        
    def isfull(self):
        if len(self.myqueue) == self.queuesize:
            return True
        else:
            return False
    
    def enqeue(self, value):
        if self.isfull():
            print("Queue is full")
        else:
            self.myqueue.append(value)
            
    def isempty(self):
        if self.myqueue == []:
            return True
        else:
            return False
        
    def qequeue(self):
        if self.isempty():
            print("queue is empty")
        else:
            self.myqueue.pop(0)
            
    def peek(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.myqueue[0])
            
    def deletequeue(self):
        self.myqueue = []
            
    def display(self):
        print(self.myqueue)

size = int(input("Enter the size of the queue: "))
obj = queue(size)
print("Queue is created of size ")
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Peek operation")
    print("5. delete")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the element to be added: "))
        obj.enqeue(value)
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        obj.display()
    elif choice == 5:
        obj.peek()
    elif choice == 5:
        obj.deletequeue()
    elif choice == 6:
        sys.exit()
        
    else:
        print("Invalid choice")