# rstrip() = to remove space from right side
# lstrip() = to remove space from left side
# strip() = to remove space both right side


city = input("Enter a city name: ")
scity = city.strip()
if scity == "New York":
    print("You live in the Big Apple!")
elif scity == "Los Angeles":
    print("You live in the City of Angels!")
elif scity == "Chicago":
    print("You live in the Windy City!")
else:
    print("I don't know where you live!")