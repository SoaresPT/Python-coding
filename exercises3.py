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
