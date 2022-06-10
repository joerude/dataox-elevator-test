from elevator import Elevator


def main():
    elevator = Elevator()
    elevator.move_up_to_max()
    elevator.print_general_info()
    elevator.move_down_to_min()
    elevator.print_general_info()


if __name__ == "__main__":
    main()
