# 9.4
import random


class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, km_h):
        self.current_speed += km_h
        if self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed <= 0:
            self.current_speed = 0

    def drive(self, hours_driven):
        self.travelled_distance += hours_driven * self.current_speed


if __name__ == "__main__":
    car_list = []
    # append 10 car objects to a list with random max speed
    for i in range(10):
        car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    # Race begins
    race = True
    while race:
        for car in car_list:
            if car.travelled_distance >= 10000:
                print(f"{car.registration_number} has reached 10,000 Km. It actually travelled: {car.travelled_distance} Km.")
                race = False
                break
            else:
                car.accelerate(random.randint(-10, 15))
                car.drive(1)
    print("\n\t\t\t\t\tFinal Race statistics:")
    print(f"Reg. Number | Max. Speed | Current Speed | Travelled Distance")
    # https://stackoverflow.com/a/44201508
    for car in car_list:
        print("{:^12}|{:^12}|{:^15}|{:^12}".format(car.registration_number, car.maximum_speed, car.current_speed,
                                                   car.travelled_distance))
