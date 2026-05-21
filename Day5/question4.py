x,y,z = map(int, input().split())
myList =[]
for i in range(x):
    a= int(input())
    myList.append(a)

for j in myList:
    if j>y and j<=z:
        print(j, end=" ")