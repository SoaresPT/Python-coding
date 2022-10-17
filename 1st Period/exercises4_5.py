import random

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

import random

N = int(input("Type the amount of random points you want to generate: "))
n = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1
pi = 4*n/N
print(f"Approx value of Pi is:  {pi}")

# 5.1
total = 0

roll = int(input("How many dices do you want to roll: "))
for i in range(roll):
    rng = random.randint(1, 6)
    #print(f"Dice #{i+1} rolled {rng}")
    total += rng
print(f"The sum is {total}")

# 5.2

l = []
while True:
    n = input("Input some numbers: ")
    if n != "":
        l.append(int(n))
    else:
        break
l.sort(reverse=True)
print(f"The five greatest numbers are : {l[:5]}")

# 5.3
number = int(input("Write a number: "))
prime = True

if number <= 1:
    print("Prime numbers must be greater than 1.")
else:
    for i in range(2, number):
        if (number % i) == 0:
            prime = False
            break
    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# 5.4
cities = []
for i in range(5):
    cities.append(input("Type a city name: "))
print("The cities you typed were: ")
for i in range(len(cities)):
    print(cities[i])
