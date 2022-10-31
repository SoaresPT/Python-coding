# 11.2
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

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.battery_capacity = battery_capacity
        self.type = "Electric"

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_capacity, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.tank_capacity = tank_capacity
        self.type = "Gasoline"

class Race:
    def __init__(self, name: str, km: int, car_list: Car):
        self.name = name
        self.km = km
        self.car_list = car_list
        self.total_hours = 0

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Reg. Number | Max. Speed | Current Speed | Travelled Distance")
        for car in car_list:
            print("{:^12}|{:^12}|{:^15}|{:^12}".format(car.registration_number, car.maximum_speed, car.current_speed,
                                                       car.travelled_distance))
        print("\n")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.km:
                return True
        return False


if __name__ == "__main__":
    car_list = []

    # Create and Add the electric and gasoline car to the list
    tesla = ElectricCar("ABC-15", 180, 52.5)
    car_list.append(tesla)

    volkswagen = GasolineCar("ACD-123", 165, 32.3)
    car_list.append(volkswagen)

    # Make the cars race at random speeds just like previous exercises but with some tweaked values to make it more interesting
    for hour in range(3):
        for car in car_list:
            car.accelerate(random.randint(1, car.maximum_speed / 2.5))
            car.drive(1)
    
    print(f"Reg. Number | Max. Speed | Current Speed | Travelled Distance | Car Type")
    for car in car_list:
        print("{:^12}|{:^12}|{:^15}|{:^20}|{:^10}".format(car.registration_number,  car.maximum_speed, car.current_speed,
                                                       car.travelled_distance, car.type))