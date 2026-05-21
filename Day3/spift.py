name = "Saurabh*is*awesome"
newname="" # for alphabets
val=""
for i in name:
    if i != "*":
        newname += i
    else:
        val += i
print(newname)
print(str(val+newname))
        