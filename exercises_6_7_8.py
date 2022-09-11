# 6.1
import random

def dice_roll():
    return random.randint(1, 6)

rolled_number = dice_roll()
while True:
    rolled_number = dice_roll()
    if rolled_number == 6:
        print(f"The rolled number is: {rolled_number}")
        break
    print(f"The rolled number is: {rolled_number}")
   
# 6.2
import random

def dice_roll(sides: int):
    return random.randint(1, sides)

max_number = int(input("What is the maximum number the dice can roll? "))
while True:
    rolled_number = dice_roll(max_number)
    if rolled_number == max_number:
        print(f"The rolled number is: {rolled_number}")
        break
    print(f"The rolled number is: {rolled_number}")
