#Game of Lucky Sevens
import random

amount_money = int(input("Enter the initial pot: "))
count = 0
total_pot = amount_money
maximum_pot = total_pot
win = "No"

while (total_pot != 0):
    if(total_pot > maximum_pot):
       maximum_pot = total_pot
    
    count += 1
    dice1_roll = random.randint(1,6)
    print("\nDice Roll 1 is: " + str(dice1_roll))
    dice2_roll = random.randint(1,6)
    print("Dice Roll 2 is: " + str(dice2_roll))
    
    for roll in range(1,7):
        if((dice1_roll == int(roll)) & (dice2_roll == int(7 - roll))):
            win = "Yes"
            total_pot += 4
            print("Pot after winning this turn is: " + str(total_pot))
            break
        else:
            continue
            
    if(win != "Yes"):
       total_pot -= 1 
       print("Pot after losing this turn is: " + str(total_pot))
    
print("\nNumber of turns to break the player were: " + str(count))
print("\nThe maximum amount of money in the pot was: " + str(maximum_pot))

                 
