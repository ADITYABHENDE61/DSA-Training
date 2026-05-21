chr = ord(input("Enter any character :"))
if chr >=65 and chr <=90:
    print("upper casse")
elif chr >=97 and chr <=122:
    print("Lower case")
    
elif chr >= 48 and chr <=57:
    print("digit")
else:
    print("Special character")