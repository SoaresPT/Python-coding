# 9.1
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    print(vars(new_car)) # Too overkill ?
    print(f"Registration Number : {new_car.registration_number}")
    print(f"Maximum Speed : {new_car.maximum_speed}")
    print(f"Current Speed : {new_car.current_speed}")
    print(f"Travelled Distance : {new_car.travelled_distance}")
