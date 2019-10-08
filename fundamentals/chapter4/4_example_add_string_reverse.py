#add a string to an empty string in reverse order

myString = "Sakshi"
reversedString = ""

for i in range(1,len(myString) + 1):
    reversedString += myString[-i]
    
print(reversedString)
