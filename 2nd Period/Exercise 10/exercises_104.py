# 10.4
import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    
    def accerelate(self, km_h: int):
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

class Race:
    def __init__(self, name: str, km: int, car_list: Car):
        self.name = name
        self.km = km
        self.car_list = car_list
    
    def hour_passes(self):
        pass

    def print_status(self):
        pass

    def race_finished(self):
        pass

if __name__ == "__main__":
    # append 10 car objects to a list with random max speed
    car_list = []
    for i in range(10):
        car_list.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    # Create the race
    race = Race("Grand Demolition Derby", 8000, car_list)