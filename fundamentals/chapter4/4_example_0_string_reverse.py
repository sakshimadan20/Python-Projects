#to print the string in reverse order

myString = "Programming"
#print(len(myString))

for count in range(1, len(myString)+1):
    print(myString[-count], end="")
    