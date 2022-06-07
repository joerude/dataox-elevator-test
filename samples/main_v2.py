# from random import choice, randint
#
#
# class Elevator:
#     """
#     direction=True => Вверх
#     direction=False => Вниз
#     """
#
#     def __init__(self, current_floor=1, capacity=5, total_floors=20, direction=True):
#         self.total_passengers = 0
#         self.passengers_dict = {}
#
#         self.total_floors = randint(5, total_floors)
#         self.capacity = capacity
#         self.current_floor = current_floor
#         self.direction = direction
#
#         self.max_floor = self.total_floors
#         self.min_floor = 1
#         self.elevator_list = []
#
#     def generate_passengers(self):
#         """
#         Генерация случайных пассажиров,
#         в диапазоне 0 до 10 на каждом этаже
#         """
#         for floor in range(1, self.total_floors + 1):
#             for passenger in range(randint(0, 10)):
#                 self.passengers_dict.setdefault(floor, []).append(
#                     Passenger(
#                         floor,
#                         choice([i for i in range(1, self.total_floors) if i != floor]),
#                     )
#                 )
#                 self.total_passengers += 1
#
#     def move_up(self):
#         if self.direction and self.current_floor != self.total_floors:
#             for passenger in self.elevator_list:
#                 if passenger.to_floor == self.current_floor:
#                     print(f"❌ Пассажир {passenger} покидает лифт")
#                     self.elevator_list = list(filter(lambda a: a != passenger, self.elevator_list))
#
#                     random_floor = choice([i for i in range(1, self.total_floors) if i != self.current_floor])
#                     self.passengers_dict.setdefault(self.current_floor, []).append(
#                         Passenger(
#                             self.current_floor,
#                             random_floor,
#                         )
#                     )
#                     print(f"Вышедшему пассажиру {passenger} назначается новый случайный этаж {random_floor}")
#
#             if self.get_passengers_of_current_floor():
#                 print(f"Пассажиры на этаже {self.get_passengers_of_current_floor()}")
#                 for passenger in self.get_passengers_of_current_floor():
#                     if (
#                             passenger.to_floor > self.current_floor
#                             and len(self.elevator_list) < self.capacity
#                     ):
#                         print(f"✅ Пассажир {passenger} заходит в лифт")
#                         self.elevator_list.append(passenger)
#                         self.passengers_dict[self.current_floor] = \
#                             list(filter(lambda a: a != passenger, self.passengers_dict[self.current_floor]))
#
#                 if not self.elevator_list:
#                     print("*** THE END! ***")
#                 else:
#                     self.max_floor = max([passenger.to_floor for passenger in self.elevator_list])
#
#             else:
#                 print("Пассажиров на этаже НЕТ")
#
#         print("┃▲  ", *self.elevator_list, "  ▲┃")
#         self.current_floor += 1
#
#     def general_info(self):
#         print("------------------------------------------------")
#         print("Общая информация:")
#         print(f"Всего в здании {self.total_passengers} пассажира/ов")
#         print(f"Здание состоит из {self.total_floors} этажей")
#         print("------------------------------------------------")
#
#     def current_status(self):
#         print("------------------------------------------------")
#         print("Информация о лифте🛗:")
#         print(f"Направление: вверх" if self.direction else f"Направление: вниз")
#         print(f"Текущий этаж: {self.current_floor}")
#         print(f"На этаже всего {len(self.get_passengers_of_current_floor())} пассажира/ов")
#         print(f"Лифт: {self.elevator_list}")
#         print(f"Доступно мест в лифте: {self.capacity - len(self.elevator_list)}")
#         print(f"Занято мест в лифте: {len(self.elevator_list)}")
#         print(f"Максимальный(необходимый) этаж: {self.max_floor}")
#         print("------------------------------------------------")
#
#     def get_passengers_of_current_floor(self):
#         return self.passengers_dict.get(self.current_floor)
#
#     def move_down(self):
#         pass
#
#
# class Passenger:
#     def __init__(self, current_floor=1, to_floor=None):
#         self.from_floor = current_floor
#         self.to_floor = to_floor
#
#     def __repr__(self):
#         return f"{self.to_floor}"
#
#
# def main():
#     elevator = Elevator()
#     elevator.generate_passengers()
#     elevator.general_info()
#
#     if elevator.direction:
#         print("ИДЁМ ВВЕРХ")
#         while elevator.current_floor != elevator.max_floor + 1:
#             print(f"*** ЭТАЖ {elevator.current_floor} ***")
#             elevator.move_up()
#             print()
#     else:
#         print("ИДЁМ ВНИЗ")
#         while elevator.current_floor != elevator.min_floor + 1:
#             elevator.move_down()
#
#
# if __name__ == "__main__":
#     main()
