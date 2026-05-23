# Regular Expression

# import re 
# count = 0
# pattern = re.compile("Function")
# # print(pattern)
# matcher = pattern.finditer("A function is a python is define by a def statement. python The general syntax looks like this: def function_name(parameters): function-name(Parameter list): statement, i.e the function body . The parameter python list consists of none or more parameters. ")
# for match in matcher:
#     print(match.group())
#     count += 1
#     print(i.start(),".........",i.end(),"..........",i.group())
# print("The number of occurences : ",count)


# import re 
# count = 0
# # pattern = re.compile("Function")
# # print(pattern)
# matcher = re.finditer("Hi","HiHiHiHiHi")
# for i in matcher:  #loop 5 times execute HiHiHiHiHi
#     print(i.group())
#     count += 1
#     print(i.start(),".........",i.end(),"..........",i.group())
# print("The number of occurences : ",count)

# import re 
# obj = input("Enter any charecter : ")
# objmatch = re.finditer(obj,"ab @k9z")
# for match in objmatch:
#     print(match.start(),".........",match.end(),"..........",match.group()) 

# ------------------------------------------------------------------------------------------

#match() Function
# import re 
# a = input("Enter any charecter : ")
# match = re.match(a,"python is a programming language")
# print(match)    
# if match!=None:
#     print("Match found at beginning level")
#     print(match.start(), " " ,match.end())
# else:
#     print("Match not found at beginning level")

# ------------------------------------------------------------------------------------------

#Fullmatch() Function

# import re
# a = input("Enter any string to perform full match : ")
# match = re.fullmatch(a,"pythonisvery")
# print(match)    
# if match!=None:
#     print("Match found ")
#     print(match.start(), " " ,match.end())
# else:
#     print("Full Match not found")

#gmail validation by using fullmatch() function

# import re
# a = input("Enter Email Id : ")
# # match = re.fullmatch("[a-zA-Z0-9]+@[a-z]+.com",a)
# match = re.fullmatch("[a-zA-Z0-9]+@[a-z]+.in",a)
# if match!=None:
#     print("Valid Email id ")
# else:
#     print(" InValid Email id")


# WAP to check Valid mobile number by using fullmatch() function

# import re
# a = input("Enter Mobile Number : ")
# match = re.fullmatch("[6-9][0-9]{9}",a)
# if match!=None:
#     print("Valid Mobile Number ")
# else:
#     print(" InValid Mobile Number")


#-----------------------------------------------------------------------------------------------

#Search() Function

# import re
# a = input("Enter any string to perform search : ")
# match = re.search("python is a dynamic programming language ",a)
# print(match)
# if match!=None:
#     print(match.start(), " " ,match.end()," ", match.group())
# else:
#     print("There is no match found anywhere")

#------------------------------------------------------------------------------------------------

#findall() function

# import re
# # match = re.findall("['0-9a-z']","abcdh3dh5bhkZGIO$&*")
# match = re.findall("['A-Z']","abcdh3dh5bhkZGIO$&*")

# print(match)

#------------------------------------------------------------------------------------------------

#sub() function
# this function perform the substitution and replacement 

# import re
# obj = re.sub("['a-zA-Z']","X","2576 ADIT GAUD Yanj")
# print(obj)

#------------------------------------------------------------------------------------------------

#split() function

# import re
# obj = re.split("['a-z']","2576 ADIT GAUD Yanj")
# print(obj)
#------------------------------------------------------------------------------------------------\

#subn() function

# import re
# obj = re.subn("['0-7']","X","2576 ADIT GAUD Yanj")
# print(obj)
# print("The string is = ",obj[0])
# print("The number of replacement is = ",obj[1])

#------------------------------------------------------------------------------------------------

# import re
# f1 = open("inputtext.txt",'r')
# f2 = open("outputtext.txt",'w')

# for line in f1: 
#     obj = re.sub("['A-Z']","X",line)
#     f2.write(obj)
# f1.close()
# f2.close()

#------------------------------------------------------------------------------------------------

class Graph:
    def __init__(self,vertices):
        # Total no of vertices
        self.V = vertices

        # Create adjacency matrix with all 0s
        self.matrix = [[0 for column in range(vertices)]
                       for row in range(vertices)]
    
    def display(self):
        for row in self.matrix:
            print(row)

    def addEdge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
    
    def removeEdge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0


# create a graph with 4 vertices
g = Graph(4)
# g.display()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.removeEdge(1, 3)
g.display()