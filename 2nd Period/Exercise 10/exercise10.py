# 10.1 - 10.3
class Elevator:

    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        self.name = ""

    def go_to_floor(self, floor: int):
        # Check if the arg passed to this method is a valid floor [Not asked by the exercise but figured it would be a nice addiction]
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Invalid Floor")
            return

        while floor < self.current_floor:
            self.floor_down()
            print(f"The elevator {self.name} is on the floor : {self.current_floor}")

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
            elevator.name = f"#{i + 1}"

    def run_elevator(self, no_elevator: int, floor: int):
        self.list_of_elevators[no_elevator - 1].go_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.list_of_elevators:
            elevator.go_to_floor(1)

if __name__ == "__main__":
    # Phase 1

    h = Elevator(1, 5)
    print("Moving to the 5th floor: ")
    h.go_to_floor(5)
    print("-----------------------------")
    print("Moving to the bottom floor: ")
    h.go_to_floor(h.bottom_floor)

    print("\n")
    # Phase 2
    # create a building with 4 elevators with floors (1-10)
    building = Building(1, 10, 4)

    # Moving elevators to a random user-specified location just to show that it's working
    print(f"The first elevator is on the floor: {building.list_of_elevators[0].current_floor}")
    print(f"Moving the first elevator to the floor 5\n")
    building.run_elevator(1, 5)
    print(f"The first elevator is now on the floor: {building.list_of_elevators[0].current_floor} \n")

    print(f"The second elevator is currently on the floor: {building.list_of_elevators[1].current_floor}")
    print(f"Moving the second elevator to the floor 9")
    building.run_elevator(2, 9)
    print(f"The second elevator is now on the floor: {building.list_of_elevators[1].current_floor}\n")

    print(f"The third elevator is currently on the floor: {building.list_of_elevators[2].current_floor}")
    print(f"Moving the third elevator to the floor 10\n")
    building.run_elevator(3, 10)
    print(f"The third elevator is now on the floor: {building.list_of_elevators[2].current_floor}\n")

    print(f"The fourth elevator is currently on the floor: {building.list_of_elevators[3].current_floor}")
    print(f"Moving the fourth elevator to the floor 6\n")
    building.run_elevator(4, 6)
    print(f"The fourth elevator is now on the floor: {building.list_of_elevators[3].current_floor}\n")

    print("All the elevators are on the following floors: ")
    for elevator in range(len(building.list_of_elevators)):
        print(f"The Elevator #{elevator + 1} is now on the floor: {building.list_of_elevators[elevator].current_floor}")

    print("\n")

    # Phase 3
    print("Fire alarm detected! Moving all the elevators to the bottom floor...")
    building.fire_alarm()
    print("\nThe fire alarm has stopped. Let's check if all the elevators got down sucessfully.")
    print("All the elevators are on the following floors: ")
    for elevator in range(len(building.list_of_elevators)):
        print(f"The Elevator #{elevator + 1} is on the {building.list_of_elevators[elevator].current_floor}")
