# 9.4
import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    
    def accerelate(self, km_h):
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
"""
Now we will program a car race. 
The travelled distance of a new car is initialized as zero. 
At the beginning of the main program, create a list that consists of 10 car objects created using a loop. 
The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: 
"ABC-1", "ABC-2" and so on. 
Now the race begins. 
One per every hour of the race, the following operations are performed:
    The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
    Each car is made to drive for one hour. This is done with the drive method.

The race continues until one of the cars has advanced at least 10,000 kilometers. 
Finally, the properties of each car are printed out formatted into a clear table.
"""
if __name__ == "__main__":
    car_list = []
    # append 10 car objects to a list with random max speed
    for i in range(10):
        car_list.append(Car(f"ABC-{i+1}", random.randint(100, 200)))
    
    # Print reg. number + max_speed (debugging purposes only)
    for car in car_list:
        print(f"{car.registration_number} {car.maximum_speed}")

    print()
    # Randomize speeds and print them
    race = True
    while race:
        for car in car_list:
            if car.travelled_distance >= 1000:
                print(f"{car.registration_number} has reached 10,000 Km {car.travelled_distance}")
                race = False
            else:
                car.accerelate(random.randint(-10, 15))
                print(f"{car.registration_number} Current speed: {car.current_speed}")
                car.drive(1)
                print(f"{car.registration_number} Distance travelled so far: {car.travelled_distance}")
                print("Still racing...\n")