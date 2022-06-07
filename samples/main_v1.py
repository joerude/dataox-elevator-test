# from random import choice, randint
#
# # to-do:
# # "Вышедшему пассажиру назначается новый случайный
# # этаж и он присоединяется к людям которые ждут лифт."
#
#
# class Elevator:
#     """
#     direction=True => Вверх
#     direction=False => Вниз
#     """
#
#     def __init__(self, direction=True, current_floor=1, capacity=5):
#         self.total_passengers = 0
#         self.passengers_dict = {}
#
#         self.total_floors = randint(5, 20)
#         self.capacity = capacity
#         self.current_floor = current_floor
#         self.direction = direction
#
#         self.max_floor = self.total_floors
#         self.min_floor = 1
#         self.elevator_list = []
#
#     def generate_passengers(self):
#         """Генерация случайных пассажиров по этажам """
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
#         print(f"Поднимаемся на этаж #{self.current_floor}" if self.current_floor != 1 else "Start")
#
#         if self.direction:
#             if self.elevator_list:
#                 for passenger in self.elevator_list:
#                     if passenger.to_floor == self.current_floor:
#                         print(f"❌ Пассажир {passenger} покидает лифт")
#                         self.elevator_list = list(filter(lambda a: a != passenger, self.elevator_list))
#                         print(self.elevator_list)
#
#             if self.get_passengers_of_current_floor():
#                 for passenger in self.get_passengers_of_current_floor():
#                     if (
#                             passenger.to_floor > self.current_floor
#                             and len(self.elevator_list) < self.capacity
#                     ):
#                         print(f"✅ Пассажир {passenger} заходит в лифт")
#                         self.elevator_list.append(passenger)
#
#                 if not self.elevator_list:
#                     print("ЛИФТ ПУСТ!")
#                 else:
#                     self.max_floor = max([passenger.to_floor for passenger in self.elevator_list])
#             else:
#                 print("НА ЭТОМ ЭТАЖЕ НЕТ ПАССАЖИРОВ ...")
#
#             # self.current_status()
#             self.current_floor += 1
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
#         if self.passengers_dict.get(self.current_floor):
#             return self.passengers_dict.get(self.current_floor)
#         return []
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
#         return f"{self.from_floor} => {self.to_floor}"
#
#
# def main():
#     elevator = Elevator()
#     elevator.generate_passengers()
#     elevator.general_info()
#
#     if elevator.direction:
#         while elevator.current_floor != elevator.max_floor + 1:
#             elevator.move_up()
#     else:
#         while elevator.current_floor != elevator.min_floor + 1:
#             elevator.move_down()
#
#     print(elevator.max_floor)
#     for floor in range(elevator.max_floor):
#         print("|       |")
#
#
# if __name__ == "__main__":
#     main()
