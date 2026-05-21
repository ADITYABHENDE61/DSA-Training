# class Tree:
#     def __init__(self, data):
#         self.data = data   #Drinks
#         self.child = []

#     def __str__(self , level = 0):
#         ret = "\t"*level + repr(self.data) + "\n"
#         for child in self.child:
#             ret += child.__str__(level+1)
#         return ret
        
    
#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree Node added successfully")

# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold") 
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# NonAlcholic = Tree("Non-Alcoholic")
# Alcoholic = Tree("Alcoholic")

# rootNode.addChild(Hot) #left
# rootNode.addChild(Cold)   #right
# Hot.addChild(tea)         #left
# Hot.addChild(coffee)
# Cold.addChild(NonAlcholic)
# Cold.addChild(Alcoholic)

# print(rootNode)





