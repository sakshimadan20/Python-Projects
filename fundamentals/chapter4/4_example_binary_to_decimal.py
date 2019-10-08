#Convert Binary to Decimal
   
binary = input("Enter the binary number: ")
decimal = 0
length = len(binary) - 1

for char in range(length, -1, -1):
    decimal = decimal + (int(binary[length - char]) * (2 ** char))
    
print("The integer value is: ",decimal)
