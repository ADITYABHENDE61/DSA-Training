class Student:
    @staticmethod
    def get_personal_detail(firstname, lastname):
        print("Your personal detail=",firstname,lastname)

    @staticmethod
    def contact_detail(mobail_No,rollno):
        print ("Your Conntact details =",mobail_No,rollno)
    
Student.get_personal_detail("Aditya","Bhende")
Student.contact_detail(7588228798,07)