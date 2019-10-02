# Program to find the greatest common divisor of 2 integers using Euclid's Algorithm

larger_number = int(input("Enter the larger number: "))
smaller_number = int(input("Enter the smaller number: "))

while(smaller_number != 0):
    print("\nStep 1: Since smaller number is not zero, we are calculating the remainder by dividing " + str(larger_number) + " by " + str(smaller_number))
    remainder = larger_number % smaller_number
    print("Remainder is: " + str(remainder))
    print("Step 2: Replacing larger number with smaller number") 
    larger_number = smaller_number
    print("Larger number is now: " + str(smaller_number))
    print("Step 3: Replacing smaller number with remainder")
    smaller_number = remainder
    print("Smaller number is now: " + str(remainder))
    
print("\nSince, smaller number is now zero, the greatest common divisor of the entered values is the latest larger number which is: " + str(larger_number))

