n = int(input("Enter the number of students: "))
d = {}
for i in range(n):
    name = input("Enter the name of the student: ")
    marks = float(input("Enter the marks of the student: "))
    d[name] = marks
    
while True:
    name = input("enter student name to get marks")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student not found")
    else:
        print("Marks of the student is: ",marks)
        
    option = input("Do you want to continue? (y/n)")
    if option == 'n':
        break
print("Thank you for using the program")
