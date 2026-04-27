from src.lab01.models import Transport
from src.lab04.interfaces import Pricable, Describable, Printable, Comparable

class CargoShip(Transport, Pricable, Describable, Printable, Comparable):
    def __init__(self, name, vmestimost, sr_skorost, cargo_capacity_tons, route_length_nm):
        super().__init__(name, vmestimost, sr_skorost)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.route_length_nm = route_length_nm

    # Реализация интерфейса Pricable
    def calculate_price(self) -> float:
        return self.cargo_capacity_tons * self.route_length_nm * 0.5

    # Реализация интерфейса Describable
    def get_short_description(self) -> str:
        return f"Грузовой корабль '{self.name}'"

    # Реализация интерфейса Printable
    def to_string(self) -> str:
        return (f"   Корабль: {self.name}\n"
                f"   Грузоподъемность: {self.cargo_capacity_tons} тонн\n"
                f"   Маршрут: {self.route_length_nm} миль\n"
                f"   Стоимость фрахта: {self.calculate_price()} у.е.")
    
    # НОВАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, CargoShip):
            raise TypeError("Сравнивать можно только с другим CargoShip")
        # Сравниваем по цене доставки
        return (self.calculate_price() > other.calculate_price()) - (self.calculate_price() < other.calculate_price())
        

class Airplane(Transport, Pricable, Describable, Printable, Comparable):
    def __init__(self, name, vmestimost, sr_skorost, max_flight_altitude_m, fuel_consumption_lph):
        super().__init__(name, vmestimost, sr_skorost)
        self.max_flight_altitude_m = max_flight_altitude_m
        self.fuel_consumption_lph = fuel_consumption_lph

    # Реализация интерфейса Pricable (ДРУГАЯ ЛОГИКА!)
    def calculate_price(self) -> float:
        return self.vmestimost * self.sr_skorost * 10

    # Реализация интерфейса Describable (ДРУГАЯ ЛОГИКА!)
    def get_short_description(self) -> str:
        return f"Самолет '{self.name}'"

    # Реализация интерфейса Printable (ДРУГАЯ ЛОГИКА!)
    def to_string(self) -> str:
        return (f"   Самолет: {self.name}\n"
                f"   Пассажиров: {self.vmestimost}\n"
                f"   Высота полета: {self.max_flight_altitude_m} м\n"
                f"   Стоимость аренды: {self.calculate_price()} у.е.")
    
    # НОВАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Airplane):
            raise TypeError("Сравнивать можно только с другим Airplane")
        # Сравниваем по цене доставки
        return (self.calculate_price() > other.calculate_price()) - (self.calculate_price() < other.calculate_price())