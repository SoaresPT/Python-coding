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


if __name__ == "__main__":
    h = Elevator(1, 5)
    h.go_to_floor(5)
    h.go_to_floor(h.bottom_floor)
