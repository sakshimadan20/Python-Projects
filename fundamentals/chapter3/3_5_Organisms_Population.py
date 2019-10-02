# Program to find out the population prediction
import math

#take the 4 inputs
initial_organisms = int(input("Enter the number of initial organisms: "))
rate = float(input("Enter the rate of growth: "))
number_of_hours = float(input("Enter the number of hours it takes to achieve the rate of " + str(rate) + ": "))
final_number_hours = float(input("Enter the number of hours after which the population is to be calculated: "))

#formula for calculating population & printing the result
#final_population = initial_organisms * pow(rate,(final_number_hours/number_of_hours))



print("\nThe final population is: "+ str((final_population)))