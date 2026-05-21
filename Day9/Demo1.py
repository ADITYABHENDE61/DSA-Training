class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next
    
    

            

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)



