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
def dice_roll(sides: int):
    return random.randint(1, sides)

max_number = int(input("What is the maximum number the dice can roll? "))
while True:
    rolled_number = dice_roll(max_number)
    if rolled_number == max_number:
        print(f"The rolled number is: {rolled_number}")
        break
    print(f"The rolled number is: {rolled_number}")
    
# 6.3
def gallon_to_liters(amount: float):
    return amount*3.78541178

while True:
    gallon_input = float(input("How many gallons do you wish to convert to liters: "))
    if gallon_input < 0:
        print("Negative number typed. Exiting...")
        break
    else:
        print(f"{gallon_input} gallons = {gallon_to_liters(gallon_input):.2f} liters")
