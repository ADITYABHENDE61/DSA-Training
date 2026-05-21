arr = [[100,198,300],[122,232,111],[223,565,764]]
newList = []

for i in range(3):
    j = 0
    max = arr[i][j]
    for j in range(3):
        if arr[i][j] > max:
            max = arr[i][j]
    newList.append(max)

print(newList)