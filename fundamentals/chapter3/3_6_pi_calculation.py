#To find out the value of (pi/4) based on approximations

import math
number_of_iterations = int(input("Enter the number of iterations: "))
i=0
sum = 1

while(i <  number_of_iterations):
    i += 1
    fraction = 1.0 / (1 + 2 * i)
    if(i % 2 != 0):
        sum = sum - fraction
    else:
        sum = sum + fraction

print("The value of pi/4 after " + str(number_of_iterations) + " is " + str(sum) + " as compared to " + str(math.pi / 4))

