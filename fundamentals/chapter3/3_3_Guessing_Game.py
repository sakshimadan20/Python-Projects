import random
import math

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
user_number = int(input("Enter a number between "+ str(lower_bound)+ " and "+ str(upper_bound) + ": "))

max_times = int(math.log((upper_bound - lower_bound + 1), 2))
if (max_times == 0):
    # in case both upper & lower bounds were same
    max_times = 1

computer_guess = random.randint(lower_bound,upper_bound)
count = 1

print("The computer guessed: " + str(computer_guess))

while((computer_guess != user_number) and (count < int(max_times))):
        if(computer_guess > user_number):
            user_output = input("Enter user comment: ")
            while(user_output != "Too Large!"):
                user_output = input("Misleading Comment!! Enter user comment again: ")
            upper_bound = computer_guess - 1
            computer_guess = random.randint(lower_bound, upper_bound)
            count +=1
            print("The computer guessed " + str(computer_guess)) 
        elif(computer_guess < user_number):
            user_output = input("Enter user comment: ")
            while(user_output != "Too Small!"):
                user_output = input("Misleading Comment!! Enter user comment again: ")
            lower_bound = computer_guess + 1
            computer_guess = random.randint(lower_bound, upper_bound)
            count +=1 
            print("The computer guessed " + str(computer_guess))

if(computer_guess == user_number):
    print("Computer guessed it right in "+ str(count) + " time(s), which is within " + str(max_times) + " tries.")
else:
    print("Computer could not guess it right within "+ str(count) + " time(s).")
            
        