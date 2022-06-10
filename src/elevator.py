import time
from random import choice, randint
from passenger import Passenger


class Elevator:
    """
    max_floor/min_floor -> максимальный/минимальный этаж
    на который нужно пассажирам лифта.
    direction=True => направление лифта ВВЕРХ
    direction=False=> направление лифта ВНИЗ
    """

    def __init__(self, current_floor=1, capacity=5, total_floors=20):
        self.total_passengers = 0
        self.passengers_dict = {}
        self.direction = None
        self.total_floors = randint(5, total_floors)
        self.capacity = capacity
        self.current_floor = current_floor
        self.max_floor = self.total_floors
        self.min_floor = 1
        self.elevator_list = []
        self.generate_passengers()
        self.print_general_info()

        if self.current_floor > self.total_floors:
            raise ValueError(
                'Текущий этаж не может быть больше максимального этажа'
            )

    def passengers_of_current_floor(self):
        """Возвращает список пассажиров на этаже"""
        return self.passengers_dict.get(self.current_floor)

    def random_floor_to_passenger(self, floor):
        """ Генерация случайного этажа, отличного
        от того на котором находиться пассажир.
        """
        return choice([i for i in range(1, self.total_floors) if i != floor])

    def generate_passengers(self):
        """ Генерация случайных пассажиров
        в диапазоне от 0 до 10 человек на каждом этаже."""
        for floor in range(1, self.total_floors + 1):
            for passenger in range(randint(0, 10)):
                self.passengers_dict.setdefault(floor, []).append(
                    Passenger(
                        floor, self.random_floor_to_passenger(floor),
                    )
                )
                self.total_passengers += 1

    def passengers_exit_elevator(self):
        """
        Пассажиры покидают лифт при достижении нужного этажа.
        Вышедшему пассажиру назначается новый случайный этаж.
        """
        for passenger in self.elevator_list:
            if passenger.to_floor == self.current_floor:
                print(f'❌ Пассажир {passenger} выходит из лифта ❌')
                self.elevator_list = list(
                    filter(lambda a: a != passenger, self.elevator_list)
                )
                self.passengers_dict.setdefault(self.current_floor, []).append(
                    Passenger(
                        self.current_floor,
                        self.random_floor_to_passenger(self.current_floor)
                    )
                )

    def passengers_enter_elevator(self):
        """ Пассажиры входят в лифт в зависимости от направления лифта. """
        print(f'Пассажиры на этаже {self.passengers_of_current_floor()}')
        if self.direction and self.passengers_of_current_floor():
            for passenger in self.passengers_of_current_floor():
                if (
                        passenger.to_floor > self.current_floor
                        and len(self.elevator_list) < self.capacity
                ):
                    print(f'✅ Пассажир {passenger} входит в лифт ✅')
                    self.elevator_list.append(passenger)
                    self.passengers_dict[self.current_floor] = list(
                        filter(
                            lambda p: p != passenger,
                            self.passengers_dict[self.current_floor],
                        )
                    )

            if self.elevator_list:
                self.max_floor = max(
                    [
                        passenger.to_floor
                        for passenger in self.elevator_list
                    ]
                )

        elif not self.direction and self.passengers_of_current_floor():
            for passenger in self.passengers_of_current_floor():
                if (
                        passenger.to_floor < self.current_floor
                        and len(self.elevator_list) < self.capacity
                ):
                    print(f'✅ Пассажир {passenger} входит в лифт ✅')
                    self.elevator_list.append(passenger)
                    self.passengers_dict[self.current_floor] = list(
                        filter(
                            lambda p: p != passenger,
                            self.passengers_dict[self.current_floor],
                        )
                    )
            if self.elevator_list:
                self.min_floor = min(
                    [p.to_floor for p in self.elevator_list]
                )
        else:
            print('ПАССАЖИРОВ НЕТ НА ЭТАЖЕ')

    def move_up(self):
        time.sleep(0.5)
        self.direction = True
        print(f'*** ЭТАЖ {self.current_floor} ***')
        print('┃⤊  ', *self.elevator_list, '  ⤊┃')

        if self.current_floor <= self.total_floors:
            self.passengers_exit_elevator()
            self.passengers_enter_elevator()
        else:
            raise ValueError('ЛИФТ НЕ МОЖЕТ БЫТЬ ВЫШЕ ПОСЛЕДНЕГО ЭТАЖА!')

        if self.current_floor != self.max_floor:
            self.current_floor += 1
        else:
            print(">>> ЭТО МАКСИМАЛЬНЫЙ ЭТАЖ <<<")

        print('┃⟰  ', *self.elevator_list, '  ⟰┃')
        print()

    def move_down(self):
        time.sleep(0.5)
        self.direction = False
        print(f'*** ЭТАЖ {self.current_floor} ***')
        print('┃⤋  ', *self.elevator_list, '  ⤋┃')

        if self.current_floor >= 1:
            self.passengers_exit_elevator()
            self.passengers_enter_elevator()
        else:
            raise ValueError('ЛИФТ НЕ МОЖЕТ БЫТЬ НИЖЕ НАЧАЛЬНОГО ЭТАЖА')

        print('┃⤋  ', *self.elevator_list, '  ⤋┃')
        if self.current_floor != self.min_floor:
            self.current_floor -= 1
        else:
            print(">>> ЭТО МИНИМАЛЬНЫЙ ЭТАЖ <<<")
        print()

    def move_up_to_max(self):
        """Лифт едет вверх до максимально необходимого этажа"""
        while self.current_floor != self.max_floor:
            self.move_up()
        self.move_up()

    def move_down_to_min(self):
        """Лифт едет вниз до минимально необходимого этажа"""
        while self.current_floor != self.min_floor:
            self.move_down()
        self.move_down()

    def print_general_info(self):
        """Выводит на экран общую информацию о пассажирах на каждом этаже."""
        print('------------------------------------------------')
        print('Общая информация:')
        print('Генерация здания и пассажиров...')
        print(f'Всего в здании {self.total_passengers} пассажир(а/ов)')
        print(f'Здание состоит из {self.total_floors} этажей')
        print(f'Текущий этаж: {self.current_floor}')

        from collections import OrderedDict
        od_passengers = OrderedDict(sorted(self.passengers_dict.items()))
        for floor, passengers in od_passengers.items():
            if self.current_floor == floor:
                print(f"{floor} этаж: пассажиры - {passengers}  <----- ЛИФТ ЗДЕСЬ")
            else:
                print(f"{floor} этаж: пассажиры - {passengers}")
        print('------------------------------------------------')
