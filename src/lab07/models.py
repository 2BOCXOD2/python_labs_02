class Transport:
    """Базовый класс для всех транспортных средств."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, active=False):
        self.name = name
        self.vmestimost = vmestimost
        self.sr_skorost = sr_skorost
        self.active = False  # Начальное состояние
        self.id = id(self)   # Уникальный ID для проверки дубликатов
        self.active = active

    def activate(self):
        """Активирует транспорт."""
        self.active = True

    def close(self):
        """Деактивирует транспорт."""
        self.active = False

    def calculate_price(self) -> float:
        """
        Метод для протоколов и фильтрации.
        По умолчанию возвращает 0.
        """
        return 0.0

    def __str__(self):
        return f"{self.__class__.__name__} '{self.name}'"


class Car(Transport):
    """Класс автомобиля."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, model: str, 
                 price: float = 0, active: bool = False): # <--- ВОТ ОН!
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.model = model
        self.price = price
        self.id = id(self)

    def calculate_price(self) -> float:
        return self.price

    def __str__(self):
        return f"{self.name} (Модель: {self.model}, Цена: {self.price:,.0f} ₽)"


class CargoShip(Transport):
    """Класс грузового корабля."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, cargo_capacity_tons: int, route_length_nm: int, active: bool = False):
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.route_length_nm = route_length_nm

    def calculate_price(self) -> float:
        return self.cargo_capacity_tons * self.route_length_nm * 0.5

    def __str__(self):
        return f"{self.name} | Груз: {self.cargo_capacity_tons}т | Маршрут: {self.route_length_nm}м.м."


class Airplane(Transport):
    """Класс самолета."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, max_flight_altitude_m: int, fuel_consumption_lph: int, active: bool = False):
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.max_flight_altitude_m = max_flight_altitude_m
        self.fuel_consumption_lph = fuel_consumption_lph

    def calculate_price(self) -> float:
        return self.vmestimost * self.sr_skorost * 10

    def __str__(self):
        return f"{self.name} | Пассажиров: {self.vmestimost} | Высота: {self.max_flight_altitude_m}м"

'''

# models.py - Слой предметной области.
# Здесь живут только классы данных. Никакой логики приложения.


class Transport:
    """Базовый класс для всех транспортных средств."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, active: bool = False):
        self.name = name
        self.vmestimost = vmestimost
        self.sr_skorost = sr_skorost
        # self.active = False  # Начальное состояние


    def activate(self):
        """Активирует транспорт."""
        self.active = True

    def close(self):
        """Деактивирует транспорт."""
        self.active = False

    def calculate_price(self) -> float:
        """
        Метод для протоколов и фильтрации.
        По умолчанию возвращает 0.
        """
        return 0.0

    def __str__(self):
        return f"{self.__class__.__name__} '{self.name}'"


class Car(Transport):
    """Класс автомобиля."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, model: str, 
                 price: float = 0, active: bool = False):
        # Передаем все параметры, которые нужны родителю + новый параметр date_added
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.model = model
        self.price = price
        # Простой ID для проверки дубликатов
        self.id = id(self)

    def calculate_price(self) -> float:
        return self.price

    def __str__(self):
        return f"Автомобиль '{self.name}' (Модель: {self.model}, Цена: {self.price:,.0f} ₽)"


class CargoShip(Transport):
    """Класс грузового корабля."""
    def __init__(self, name, vmestimost, sr_skorost, cargo_capacity_tons, route_length_nm,
                 active=False, id=None):
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.route_length_nm = route_length_nm
        self.id = id(self)

    def calculate_price(self) -> float:
        # Пример цены для корабля (груз * расстояние * коэффициент)
        return self.cargo_capacity_tons * self.route_length_nm * 0.5

    def __str__(self):
        return f"Корабль '{self.name}' | Груз: {self.cargo_capacity_tons}т | Маршрут: {self.route_length_nm}м.м."


class Airplane(Transport):
    """Класс самолета."""
    def __init__(self, name: str, vmestimost: int, sr_skorost: float,
                 max_flight_altitude_m: int, fuel_consumption_lph: int, active=False, id=None):
        super().__init__(name, vmestimost, sr_skorost, active=active)
        self.max_flight_altitude_m = max_flight_altitude_m
        self.fuel_consumption_lph = fuel_consumption_lph
        self.id = id(self)

    def calculate_price(self) -> float:
        # Пример цены для самолета (вместимость * скорость * коэффициент)
        return self.vmestimost * self.sr_skorost * 10

    def __str__(self):
        return f"Самолет '{self.name}' | Пассажиров: {self.vmestimost} | Высота: {self.max_flight_altitude_m}м"

'''