number = int(input("Type a number: "))
factorial = number
if number <= 0:
    print("Thanks and bye!")
else:
    for i in range(1, number):
        factorial = factorial * i
        print(f"i is now {i} so Factorial {factorial}")
    print(f"The factorial of {number} is {factorial}")