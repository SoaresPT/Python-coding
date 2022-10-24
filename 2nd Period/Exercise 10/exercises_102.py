# 10.1
class Elevator:
    
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    
    def go_to_floor(self, floor: int):
        # Check if the arg passed to this method is a valid floor [Not asked by the exercise but figured it would be a nice addiction]
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Invalid Floor")
            return
        
        while floor < self.current_floor:
                self.floor_down()
                print(f"The elevator is on the floor : {self.current_floor}")
        
        while floor > self.current_floor:
                self.floor_up()
                print(f"The elevator is on the floor : {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1

class Building:
    def __init__(self, bottom_floor: int, top_floor: int, no_elevators: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.no_elevators = no_elevators
        self.list_of_elevators = []
    
    def create_elevators(self):
        for i in range(1, self.no_elevators+1):
            elevator = "elevator" + str(i)
            elevator = Elevator(self.bottom_floor, self.top_floor)
            self.list_of_elevators.append(elevator)
    
    def run_elevator(self, no_elevator: int, floor: int):
        self.list_of_elevators[no_elevator-1].go_to_floor(floor)

if __name__ == "__main__":
    #building with 1-10 floors, 4 elevators
    building = Building(1, 10, 4)

    building.create_elevators()
    print(building.list_of_elevators)
    print()
    print(building.list_of_elevators[0].current_floor)
    building.run_elevator(1,5)
    print(building.list_of_elevators[0].current_floor)
