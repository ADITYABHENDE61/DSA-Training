# username = "admin"
# password = "admin"
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin":
        print("Login Successful")
        break
    else:
        print("Invalid username or password")