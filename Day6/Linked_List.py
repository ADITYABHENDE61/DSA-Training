# class Node :
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList :
#     def __init__(self):
#         self.head = None
    
# linkedllist = LinkedList()
# linkedllist.head = Node(5)
# second =           Node(10)
# third =            Node(15)
# forth =            Node(20)

# #connecting the nodes
# linkedllist.head.next = second
# second.next = third
# third.next = forth

# #displaying the data of the nodes
# while linkedllist.head != None:
#     print(linkedllist.head.data," - "  , end =" ")
#     linkedllist.head = linkedllist.head.next


class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        self.node = Node(data)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else :
            self.tail.next = self.node
            self.tail = self.node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else :
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    def addNodeInBeginning(self, data):
        self.node = Node(data)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else :
            self.node.next = self.head
            self.head = self.node
    
    def addNodeInBetween(self, data, position):
        self.node = Node(data)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else :
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            self.node.next = temp.next
            temp.next = self.node

    def addNodeInEnd(self, data):
        self.node = Node(data)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else :
            self.tail.next = self.node
            self.tail = self.node


if __name__ == "__main__":
    object = LinkedList()   # LinkedList object created
    # Menu Driven options
    while True:
        print("\n1. Add Node Linked List :")
        print("2. Add Node in the beginning :")
        print("3. Add Node in the Between :")
        print("4. Add Node in the end :")
        print("5. Display the Linked List :")
        print("6. Exit")
        ch = int(input("Enter your choice :"))
        if ch == 1 :
            value = int(input("Enter the value of the node :"))
            object.addNode(value)
            print("Node added successfully at the singly linked list :")
        
        elif ch == 2 :
            value = int(input("Enter the value of the node :"))
            object.addNodeInBeginning(value)
            print("Node added successfully at the beginning of the linked list :")

        elif ch == 5 :
            print("The elements in the linked list are :")
            object.display()

        elif ch == 3 :
            value = int(input("Enter the value of the node :"))
            position = int(input("Enter the position of the node :"))
            object.addNodeInBetween(value, position)
            print("Node added successfully at the between of the linked list :")
        

