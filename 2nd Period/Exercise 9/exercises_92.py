# 9.2
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

if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    print(f"Registration Number : {new_car.registration_number}")
    print(f"Maximum Speed : {new_car.maximum_speed}")
    print(f"Current Speed : {new_car.current_speed}")
    print(f"Travelled Distance : {new_car.travelled_distance}")
    print("-------------------------------------------------------")

    new_car.accerelate(30)
    new_car.accerelate(70)
    new_car.accerelate(50)
    print(new_car.current_speed)
    new_car.accerelate(-200)
    print(new_car.current_speed)
