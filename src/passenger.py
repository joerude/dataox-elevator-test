class Passenger:
    """
    Класс пассажир имеет два атрибута:
    from_floor -> начальный этаж
    to_floor -> этаж на который нужно добраться
    """
    def __init__(self, from_floor=1, to_floor=None):
        self.from_floor = from_floor
        self.to_floor = to_floor

    def __repr__(self):
        return f"{self.to_floor}"
