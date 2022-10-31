# 10.3
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

        for i in range(self.no_elevators):
            elevator = Elevator(self.bottom_floor, self.top_floor)
            self.list_of_elevators.append(elevator)

    def run_elevator(self, no_elevator: int, floor: int):
        self.list_of_elevators[no_elevator - 1].go_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.list_of_elevators:
            elevator.go_to_floor(self.bottom_floor)


if __name__ == "__main__":
    # building with 1-10 floors, 4 elevators
    building = Building(1, 10, 4)

    print(f"The first elevator is on the floor: {building.list_of_elevators[0].current_floor}")
    print(f"Moving the first elevator to the floor 5\n")
    building.run_elevator(1, 5)
    print(f"The first elevator is on the floor: {building.list_of_elevators[0].current_floor} \n")

    print(f"The second elevator is currently on the floor: {building.list_of_elevators[1].current_floor}")
    building.run_elevator(2, 9)
    print(f"Moving the second elevator to the floor 9\n")
    print(f"The second elevator is currently on the floor: {building.list_of_elevators[1].current_floor}\n")

    print(f"The third elevator is currently on the floor: {building.list_of_elevators[2].current_floor}")
    building.run_elevator(3, 10)
    print(f"Moving the third elevator to the floor 10\n")
    print(f"The second elevator is currently on the floor: {building.list_of_elevators[2].current_floor}\n")

    print(f"The fourth elevator is currently on the floor: {building.list_of_elevators[3].current_floor}")
    building.run_elevator(4, 6)
    print(f"Moving the fourth elevator to the floor 6\n")
    print(f"The second elevator is currently on the floor: {building.list_of_elevators[3].current_floor}\n")

    print("All the elevators are on the following floors: ")
    for elevator in range(len(building.list_of_elevators)):
        print(f"The Elevator #{elevator + 1} is on the {building.list_of_elevators[elevator].current_floor}")

    building.fire_alarm()
    print("\n\nFire alarm detected! Moving all the elevators to the bottom floor...")
    print("All the elevators are on the following floors: ")
    for elevator in range(len(building.list_of_elevators)):
        print(f"The Elevator #{elevator + 1} is on the {building.list_of_elevators[elevator].current_floor}")
