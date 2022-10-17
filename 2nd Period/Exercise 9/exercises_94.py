# 9.4
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
    new_car = Car("ABC-123", 142)
    new_car.travelled_distance = 2000
    new_car.accerelate(60)
    new_car.drive(1.5)
    print(new_car.travelled_distance)        