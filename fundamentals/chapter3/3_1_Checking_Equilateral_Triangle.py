# Write a program to indicate whether or not the triangle is an equilateral triangle

#input the 3 sides of the traingle
side1 = float(input("Enter the length of side 1 : "))
side2 = float(input("Enter the length of side 2 : "))
side3 = float(input("Enter the length of side 3 : "))

#check if the three sides are equal
if((side1 == side2) and (side2==side3)):
    print("\nThe triangle is an equilateral triangle :")
else:
    print("\nThe triangle is not an equilateral triangle")