# to convert an octal representation of integers to decimal

octal = input("Enter the octal number: ")
decimal = 0
exponent = len(octal) - 1

for digit in octal:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent -= 1

print("\nThe integer value is " + str(decimal))