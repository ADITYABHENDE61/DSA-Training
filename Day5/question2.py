# Write a program to access each character of a string in forward and backward direction (using loop).
# i/p = "learning python is very easy"

str = "learning python is very easy"
print("Forward direction:")
for i in str:
    print(i,end=" ")
print("\nBackward direction:")
for i in range(len(str)-1, -1, -1):
    print(str[i], end=" ")
    