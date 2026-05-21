v = ['a','e','i','o','u']
w = input("Enter a word: ")
# w = saurabhkha
found = []
for i in w:
    if i in v:
        found.append(i)
print("Vowels in the word are: ",found)
print("unique vowel",len(found), 'from the give word =',w)