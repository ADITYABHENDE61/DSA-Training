# Hashing is a technique to convert a large chunk of data into a small format
# Hashing is used to store the data in an unordered manner

class HashTable:
    def __init__(self):
        self.size = self.size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)

h = HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()

    