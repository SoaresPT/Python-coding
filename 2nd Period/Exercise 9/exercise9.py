# Exercise 9
import random


class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, km_h):
        if km_h < 0:
            if self.current_speed - km_h <= 0:
                self.current_speed += km_h
            else:
                self.current_speed = 0
        if km_h > 0:
            if self.current_speed + km_h <= self.maximum_speed:
                self.current_speed += km_h
            else:
                self.current_speed = self.maximum_speed

    def drive(self, hours_driven):
        self.travelled_distance += hours_driven * self.current_speed


# Phase 1

new_car = Car("ABC-123", 142)
print(f"Registration Number : {new_car.registration_number}")
print(f"Maximum Speed : {new_car.maximum_speed}")
print(f"Current Speed : {new_car.current_speed}")
print(f"Travelled Distance : {new_car.travelled_distance}")

print("\n")
# Phase 2
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"Current Speed: {new_car.current_speed}")
new_car.accelerate(-200)
print(f"Final Speed: {new_car.current_speed}")

print("\n")
# Phase 3
# Set the car travelled distance to 2000 to match the example of exercise 9.3
new_car.travelled_distance = 2000
new_car.accelerate(60)
new_car.drive(1.5)
print(f"Now the travelled distance is : {new_car.travelled_distance}")

print("\n")
# Phase 4

car_list = []
# append 10 car objects to a list with random max speed
for i in range(10):
    car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

# Race begins
print("Starting the race...")
race = True
while race:
    for car in car_list:
        if car.travelled_distance >= 10000:
            print(
                f"{car.registration_number} has reached 10,000 Km. It actually travelled: {car.travelled_distance} Km.")
            race = False
            break
        else:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

print("\n\t\t\t\t\tFinal Race statistics:")
# Print list in a nice format
print(f"Reg. Number | Max. Speed | Current Speed | Travelled Distance")
for car in car_list:
    print("{:^12}|{:^12}|{:^15}|{:^12}".format(car.registration_number, car.maximum_speed, car.current_speed,
                                               car.travelled_distance))
