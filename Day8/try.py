import logging
logging.basicConfig(filename="newfile.log", level = logging.DEBUG)
try:
    a = int (input("Enter the number : "))
    b = int (input("Enter the number : "))
    print (a/b)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
    logging.exception(msg)  
print("Logging Level is set up. Check 'newfile.log' for details.")