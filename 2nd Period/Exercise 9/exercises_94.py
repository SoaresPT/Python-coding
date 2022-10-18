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

if __name__ == "__main__":
    car_list = []
    # append 10 car objects to a list with random max speed
    for i in range(10):
        car_list.append(Car(f"ABC-{i+1}", random.randint(100, 200)))
    
    # Print reg. number + max_speed (debugging purposes only)
    #for car in car_list:
        #print(f"{car.registration_number} {car.maximum_speed}")

    #print()
    # Randomize speeds and print them
    race = True
    while race:
        for car in car_list:
            if car.travelled_distance >= 10000:
                print(f"{car.registration_number} has reached 10,000 Km. Travelled actually {car.travelled_distance}")
                race = False
                break                 
            else:
                car.accerelate(random.randint(-10, 15))
                print(f"{car.registration_number} Current speed: {car.current_speed}")
                car.drive(1)
                print(f"{car.registration_number} Distance travelled so far: {car.travelled_distance}")
                print("Still racing...\n")
    print("\n")
    print(f"Reg. Number | Max. Speed | Current Speed | Travelled Distance")
    for car in car_list:
        print("{:^12}|{:^12}|{:^15}|{:^12}".format(car.registration_number,car.maximum_speed,car.current_speed,car.travelled_distance))