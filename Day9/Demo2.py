class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        value = [str(x) for x in self.LinkedList]
        return ''.join(value)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else :
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None 
                self.LinkedList.tail = None 
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempNode
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else :
            return self.LinkedList.head
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print (custQueue)
print("Display top Value")
print(custQueue.peek())
print ("Delete FIFO")
print(custQueue.dequeue())
print ("Display Queue again !")
print(custQueue)
