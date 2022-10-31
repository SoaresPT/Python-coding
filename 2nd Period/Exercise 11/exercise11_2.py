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
            if car.travelled_distance >= race.km:
                return True
        return False


if __name__ == "__main__":
    # append 10 car objects to a list with random max speed
    car_list = []
    for i in range(10):
        car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    # Create the race
    race = Race("Grand Demolition Derby", 8000, car_list)
    while True:
        if race.total_hours % 10 == 0:
            print(f"The race has been going on for {race.total_hours} hours. Here are the current stats: \n")
            race.print_status()
        race.hour_passes()
        race.total_hours += 1
        if race.race_finished():
            # Find out which car won
            for car in race.car_list:
                if car.travelled_distance >= 8000:
                    winner = car

            print(f"The race is over! The winner is the car: {winner.registration_number}!!\nHere are the race results:")
            break

    race.print_status()
