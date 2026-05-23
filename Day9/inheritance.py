# Single Inheritance
# class College:
#     def college_name(self):
#         print("College : RBU")

# class Student(College):
#     def student_info(self):
#         print("Name : Aditya Bhende")
#         print("Branch : MCA")

# obj = Student()
# obj.college_name()
# obj.student_info()

# Multilevel Inheritance
# class College:
#     def college_name(self):
#         print("College : RBU")

# class Student(College):
#     def student_info(self):
#         print("Name : Aditya Bhende")
#         print("Branch : MCA")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : Python")
#         print("Subject1 : java")
#         print("Subject1 : C")


# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# Multiple Inheritance

class College:
    def college_name(self):
        print("College : RBU")

class Student:
    def student_info(self):
        print("Name : Aditya Bhende")
        print("Branch : MCA")

class Exam(College,Student):
    def subject(self):
        print("Subject1 : Python")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()

