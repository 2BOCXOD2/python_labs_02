
from validate import validate_vmestimost, validate_sr_skorost, validate_name_type, validate_name_exist, \
                     validate_active_state, validate_fuel_amount, validate_fuel_limit, validate_positive_number, \
                     validate_service_level


class Transport:
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, rasstoyanie=None):
        self._name = name
        self._vmestimost = vmestimost
        self._sr_skorost = sr_skorost
        self._rasstoyanie = rasstoyanie
        self.active = False  # Начальное состояние неактивно
        validate_vmestimost(vmestimost)  # Используется внешний валидатор
        validate_sr_skorost(sr_skorost)  # Используется внешний валидатор
        validate_name_type(name)
        validate_name_exist(name)

    def activate(self):
        """Активирует транспортное средство"""
        self.active = True

    def close(self):
        """Деактивирует транспортное средство"""
        self.active = False

    def upgrade(self):
        """Общий базовый метод, пока ничего не делает"""
        pass

    # Геттеры и сеттеры
    @property 
    def name(self):
        return self._name # Геттер: просто возвращает значение внутреннего атрибута

    @name.setter
    def name(self, value):
        self._name = value  # Просто устанавливаем значение без дополнительной валидации

    @property
    def vmestimost(self):
        return self._vmestimost

    @vmestimost.setter
    def vmestimost(self, value):
        validate_vmestimost(value)
        self._vmestimost = value  # Просто устанавливаем значение без дополнительной валидации

    @property
    def sr_skorost(self):
        return self._sr_skorost

    @sr_skorost.setter
    def sr_skorost(self, value):
        self._sr_skorost = value  # Просто устанавливаем значение без дополнительной валидации

    @property
    def rasstoyanie(self):
        return self._rasstoyanie

    @rasstoyanie.setter
    def rasstoyanie(self, value):
        self._rasstoyanie = value  # Просто устанавливаем значение без дополнительной валидации

    # dunder-методы
    def __str__(self):
        """Возвращает удобочитаемое строковое представление."""
        return f"Транспорт '{self.name}', вместимость {self.vmestimost}, средняя скорость {self.sr_skorost} км/ч."

    def __repr__(self):
        """Формальное строковое представление объекта."""
        return f"Transport(name='{self.name}', vmestimost={self.vmestimost}, sr_skorost={self.sr_skorost})"

    def __eq__(self, other):
        """Проверяет равенство двух транспортных средств по имени, вместимости и средней скорости."""
        if isinstance(other, Transport):
            return (
                self.name == other.name and
                self.vmestimost == other.vmestimost and
                self.sr_skorost == other.sr_skorost
            )
        return False

    # Мои методы
    def opisanie(self):
        return f"{self.name}: вместимость - {self.vmestimost}, средняя скорость - {self.sr_skorost}"

    def vremya_v_puti(self):
        if self.rasstoyanie is not None:
            vremya = round(self.rasstoyanie / self.sr_skorost, 2)
            return vremya
        else:
            raise ValueError("Расчёт невозможен без расстояния")

    def oplatit_proezd_Bus(self):
        if self.rasstoyanie is not None:
            stoimost = self.rasstoyanie * 3
            return stoimost
        else:
            raise ValueError("Оплата невозможна без указанного расстояния")

    def oplatit_proezd_Car(self):
        if self.rasstoyanie is not None:
            stoimost = self.rasstoyanie * 40
            return stoimost
        else:
            raise ValueError("Оплата невозможна без указанного расстояния")



class Car(Transport):
    MAX_SPEED = 300  # Максимально возможная скорость автомобиля
    
    def __init__(self, name, vmestimost, sr_skorost, model):
        super().__init__(name, vmestimost, sr_skorost)
        self._model = model
        self.service_level = 0  # Уровень технического обслуживания (может расти до 6)

    def upgrade(self):
        """Повышение уровня обслуживания (до максимум 6)"""
        validate_service_level(self.service_level)
        self.service_level += 1

    def drive(self, km):
        """Начинает поездку на указанное расстояние"""
        validate_active_state(self.active)
        validate_positive_number(km)
        print(f"Автомобиль движется на {km} километров.")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value  # Просто присваиваем значение без дополнительной валидации

    def __str__(self):
        return f"Машина '{self.name}' ({self.model}), вместимость {self.vmestimost}, средняя скорость {self.sr_skorost} км/ч."

    def __repr__(self):
        return f"Car(name='{self.name}', vmestimost={self.vmestimost}, sr_skorost={self.sr_skorost}, model='{self.model}')"

    def __eq__(self, other):
        if isinstance(other, Car):
            return (
                super().__eq__(other) and
                self.model == other.model
            )
        return False

    def opisanie(self):
        return f"Машина {self.name}, модель {self.model}: вместимость - {self.vmestimost}, средняя скорость - {self.sr_skorost}"


class Bus(Transport):
    def __init__(self, name, vmestimost, sr_skorost, god_vipuska):
        super().__init__(name, vmestimost, sr_skorost)
        self._god_vipuska = god_vipuska
        self.fuel_tank = 100  # Бензобак объемом 100 литров

    def refill_fuel(self, liters):
        """Заливает топливо в бак (максимум 100 литров)"""
        validate_fuel_limit(liters + self.fuel_tank)
        self.fuel_tank += liters

    def drive(self, km):
        """Начинает поездку на указанное расстояние (расход топлива: 1 литр/км)"""
        fuel_needed = km
        validate_active_state(self.active)
        validate_fuel_amount(self.fuel_tank, fuel_needed)
        self.fuel_tank -= fuel_needed
        print(f"Автобус едет на {km} километров.")

    @property
    def god_vipuska(self):
        return self._god_vipuska

    @god_vipuska.setter
    def god_vipuska(self, value):
        if (value >= 1900) and (value <= 2026):
            self._god_vipuska = value 
        else:
            raise ValueError("Год выпуска должен быть позже 1900 года.")
        

    def __str__(self):
        return f"Автобус '{self.name}', год выпуска {self.god_vipuska}, вместимость {self.vmestimost}, средняя скорость {self.sr_skorost} км/ч."

    def __repr__(self):
        return f"Bus(name='{self.name}', vmestimost={self.vmestimost}, sr_skorost={self.sr_skorost}, god_vipuska={self.god_vipuska})"

    def __eq__(self, other):
        if isinstance(other, Bus):
            return (
                super().__eq__(other) and
                self.god_vipuska == other.god_vipuska
            )
        return False

    def opisanie(self):
        return f"Автобус {self.name}, год выпуска {self.god_vipuska}: вместимость - {self.vmestimost}, средняя скорость - {self.sr_skorost}"

