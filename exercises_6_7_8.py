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

# 6.4
def sum_list(sumList: list):
    return sum(sumList)

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"The sum of the list is: {sum_list(lista)}")

# 6.5
def trim_odd_numbers(list_of_numbers: list):
    cut_list = []
    for i in list_of_numbers:
        if i % 2 == 0:
            cut_list.append(i)
    return cut_list

lista = [0,1,2,3,4,5,6,7,8,9,10,11,13,15,16]
print(f"Original List: {lista}")
print(f"Cut-down List: {trim_odd_numbers(lista)}")

