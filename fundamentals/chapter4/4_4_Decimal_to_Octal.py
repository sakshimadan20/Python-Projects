# to convert a decimal representation of integers to octal

decimal = int(input("Enter a decimal integer: "))

print("\n%10s%10s%12s" % ("Quotient", "Remainder", "Octal"))
octal = ""

while decimal > 0:
    remainder = decimal % 8
    decimal = decimal // 8
    octal = str(remainder) + octal
    print("%10d%10d%12s" % (decimal, remainder, octal))

print("\nThe octal representation is " + octal)
