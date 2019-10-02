#Game of Lucky Sevens
import random

amount_money = int(input("Enter the initial pot: "))
count = 0
total_pot = amount_money
maximum_pot = total_pot

while (total_pot != 0):
    
    count += 1
    dice1 = random.randint(1,6)
    print("\nDice Roll 1 is: " + str(dice1))
    dice2 = random.randint(1,6)
    print("Dice Roll 2 is: " + str(dice2))
    
    if(dice1 + dice2 == 7):
        total_pot += 4
        print("Pot after winning this turn is: " + str(total_pot))
    else:
        total_pot -= 1 
        print("Pot after losing this turn is: " + str(total_pot))
        
    if(total_pot > maximum_pot):
       maximum_pot = total_pot
    
print("\nNumber of turns to break the player were: " + str(count))
print("\nThe maximum amount of money in the pot was: " + str(maximum_pot))