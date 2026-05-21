math  = 50
chem = 90
dsa = 66
total = math+ chem+ dsa
percentage = total/3.0
print("total :",total)
print("percentage :", percentage)
if math >= 40 and chem >=40 and dsa >=40:
    print("Pass")
else:
    print("Fail")
    
gender = input("Enter the gender M/F :")
if percentage >= 65 and gender == "male":
    print("eligible of placement")
else:
    print("not eligible for placement")

    
    
    