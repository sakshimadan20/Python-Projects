#To find the distance travelled by the ball by dropping it from a certain height

import math

height = float(input("Enter the initial height from which the ball is dropped: "))
bounciness_index = float(input("Enter the bounciness index: "))

distance = 0.0
number_bounces = 0

def isEqualFloat(f1, f2):
    return abs(f1 - f2) <= 1e-9

while(isEqualFloat(height, 0.0) != True):
    number_bounces += 1
    distance = distance + height + (bounciness_index * height)
    height = bounciness_index * height
    
print("\nThe distance travelled is: " + str(round(distance,2)) + " ft. in " +  str(number_bounces) + " bounces." )