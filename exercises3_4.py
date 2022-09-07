import random
import math

# 3.1

zander_size = int(input("What is the length of the zander? "))
if zander_size < 42:
    print(f"Please release it back to the lake. The zander is {42-zander_size} cm too small.")

# 3.2

cabin_class = input("Type the cabin class: ")
if cabin_class.upper() == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class.upper() == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class.upper() == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class.upper() == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

# 3.3
gender = input("What is your gender? ")
hemoglobin = int(input("What is your hemoglobin value (g/l)? "))
if gender.upper() == "M" or gender.upper() == "MALE":
    if hemoglobin < 134:
        print("Your hemoglobin value is low")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender.upper() == "F" or gender.upper() == "FEMALE":
    if hemoglobin < 117:
        print("Your hemoglobin value is low")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Error: Can't calculate. Invalid gender typed.")

# 3.4
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This is a leap year!")
else:
    print("This is not a leap year!")


# 4.1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

# 4.2
while True:
    inches = float(input("Type the amount of inches: "))
    if inches < 0:
        print("Negative number detected. Stopping.")
        break
    print(f"{inches} inches is the equivalent of {inches*2.54:.2f} cm")

# 4.3


smallest_no = None
highest_no = None
while True:
    input_no = input("Input a number: ")
    if input_no == "":
        print(f"The smallest number was {smallest_no} and the biggest number was {highest_no}")
        break
    # In case the user never types a number at the beginning we're going to exit out. Otherwise, set them to the vars
    if smallest_no is None and highest_no is None:
        smallest_no = float(input_no)
        highest_no = float(input_no)

    if smallest_no > float(input_no):
        smallest_no = float(input_no)
    if highest_no < float(input_no):
        highest_no = float(input_no)

# 4.4

rng = random.randint(1, 10)
while True:
    user_guess = int(input("Guess the number [1-10]: "))
    if user_guess < rng:
        print("Too low")
    elif user_guess > rng:
        print("Too high")
    else:
        print("Correct")
        break

# 4.5
username = "python"
password = "rules"
no_guesses = 0

while no_guesses < 5:
    user_login = input("Type the username: ")
    user_pass = input("Type the password: ")
    if user_login != username or user_pass != password:
        no_guesses += 1
        if no_guesses == 5:
            print("Access Denied")
            break
    else:
        print("Welcome")
        break

# 4.6

N = int(input("Type the amount of random points you want to generate: "))
n = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1
pi = 4*n/N
print(n)
print(N)
print(f"Approx value of Pi is:  {pi}")