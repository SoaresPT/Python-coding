import math
import random

# Phase 1

name = input("What is your name? ")
print(f"Hello {name}!")

# Phase 2

radius = float(input("Give me the radius? "))
print(f"The area is {math.pi*radius**2:.2f}")

# Phase 3

rect_length = int(input("Please input the desired rectangle length: "))
rect_width = int(input("Please input the desired rectangle width: "))
print(f"The perimeter is {rect_width*2+rect_length*2} and the area is {rect_width*rect_length}")

# Phase 4

number1 = int(input("Input the first integer number: "))
number2 = int(input("Input the second integer number: "))
number3 = int(input("Input the third integer number: "))
print(f"The sum is {number1 + number2 + number3}, the product is {number1*number2*number3} and the average is {(number1+number2+number3)/3}")

# Phase 5

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talent_kg = talents * 8.512
pounds_kg = pounds * 0.4256
lots_kg = lots * 0.0133
kg = int(talent_kg + pounds_kg + lots_kg)
g = (talent_kg + pounds_kg + lots_kg - kg) * 1000
print(f"The weight in modern units: {kg} kilograms and {g:.2f} grams.")


# Phase 6

print(f"Combination lock of 3-digit: {random.randint(0,9)} - {random.randint(0,9)} - {random.randint(0,9)}")
print(f"Combination lock of 4-digit: {random.randint(0,6)} - {random.randint(0,6)} - {random.randint(0,6)} - {random.randint(0,6)}")
