inputWord = input()
splitted = inputWord.split()
output =""
firstLetter = ""
for i in splitted:
    if i == "the" or i == "of":
        firstLetter = i[0]
    else:
        firstLetter = i[0].upper()
    output = output + firstLetter

print(output)
