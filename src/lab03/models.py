
from src.lab01.models import Transport

class CargoShip(Transport):
    """
    Класс, представляющий грузовой корабль.
    """
    def __init__(self, name, vmestimost, sr_skorost, cargo_capacity_tons, route_length_nm):
        super().__init__(name, vmestimost, sr_skorost)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.route_length_nm = route_length_nm

    # НОВОЕ: Переопределение метода базового класса для красивого вывода
    def __str__(self):
        return f"Корабль '{self.name}': Грузоподъемность {self.cargo_capacity_tons}т, Маршрут {self.route_length_nm}м. миль"
    
    # НОВАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА
    def process(self) -> str:
        """Моделирует процесс погрузки и отправки корабля."""
        return f"Корабль '{self.name}' загружен {self.cargo_capacity_tons} тоннами. Курс на выход из порта!"

    # НОВОЕ: Полиморфный метод
    def calculate_price(self) -> float:
        """Цена фрахта зависит от объема груза и расстояния."""
        return self.cargo_capacity_tons * self.route_length_nm * 0.5

    # метод для совместимости
    def calculate_flight_duration(self):
        hours = self.route_length_nm / self.sr_skorost
        days = hours / 24
        return round(days, 2)
    



class Airplane(Transport):
    """
    Класс, представляющий самолет.
    """
    def __init__(self, name, vmestimost, sr_skorost, max_flight_altitude_m, fuel_consumption_lph):
        super().__init__(name, vmestimost, sr_skorost)
        self.max_flight_altitude_m = max_flight_altitude_m
        self.fuel_consumption_lph = fuel_consumption_lph

    # НОВОЕ: Переопределение метода базового класса
    def __str__(self):
        return f"Самолет '{self.name}': Высота {self.max_flight_altitude_m}м, Расход топлива {self.fuel_consumption_lph} л/ч"
    
    # НОВАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА
    def process(self) -> str:
        """Моделирует процесс подготовки самолета к взлету."""
        return f"Самолет '{self.name}' принял на борт пассажиров. Запрашиваем разрешение на взлет с высоты {self.max_flight_altitude_m}м."

    # НОВОЕ: Полиморфный метод
    def calculate_price(self) -> float:
        """Цена аренды зависит от вместимости и скорости."""
        return self.vmestimost * self.sr_skorost * 10

    # метод для совместимости
    def calculate_flight_range(self, fuel_tank_liters):
        flight_hours = fuel_tank_liters / self.fuel_consumption_lph
        distance_km = self.sr_skorost * flight_hours
        return round(distance_km, 2)



'''
# Импортируем базовый класс из лабораторной работы №1
from src.lab01.models import Transport

class CargoShip(Transport):
    """
    Класс, представляющий грузовой корабль.
    Наследует общие свойства от Transport.
    """
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, cargo_capacity_tons: int, route_length_nm: float):
        """
        Инициализация грузового корабля.
        
        Args:
            cargo_capacity_tons: Грузоподъемность в тоннах.
            route_length_nm: Длина маршрута в морских милях.
        """
        # Используем super() для вызова конструктора базового класса
        super().__init__(name, vmestimost, sr_skorost)
        
        # Новые атрибуты, специфичные для CargoShip
        self.cargo_capacity_tons = cargo_capacity_tons
        self.route_length_nm = route_length_nm

    # Новый метод для CargoShip
    def calculate_flight_duration(self) -> float:
        """
        Рассчитывает продолжительность рейса в сутках.
        (При средней скорости в узлах, 1 морская миля = 1 час пути)
        """
        hours = self.route_length_nm / self.sr_skorost
        days = hours / 24
        return round(days, 2)


class Airplane(Transport):
    """
    Класс, представляющий самолет.
    Наследует общие свойства от Transport.
    """
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, max_flight_altitude_m: int, fuel_consumption_lph: float):
        """
        Инициализация самолета.
        
        Args:
            max_flight_altitude_m: Максимальная высота полета в метрах.
            fuel_consumption_lph: Расход топлива в литрах в час.
        """
        # Используем super() для вызова конструктора базового класса
        super().__init__(name, vmestimost, sr_skorost)
        
        # Новые атрибуты, специфичные для Airplane
        self.max_flight_altitude_m = max_flight_altitude_m
        self.fuel_consumption_lph = fuel_consumption_lph

    # Новый метод для Airplane
    def calculate_flight_range(self, fuel_tank_liters: int) -> float:
        """
        Рассчитывает дальность полета в километрах.
        
        Args:
            fuel_tank_liters: Объем топливного бака в литрах.
            
        Returns:
            Дальность полета в километрах.
        """
        flight_hours = fuel_tank_liters / self.fuel_consumption_lph
        distance_km = self.sr_skorost * flight_hours # Скорость км/ч * часы
        return round(distance_km, 2)
'''