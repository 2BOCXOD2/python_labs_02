
'''
class Ticket(Transport):
    

class Route(Transport):
    

class Driver(Transport):
    
'''

class Transport:
    def __init__(self, name: str, vmestimost: int, sr_skorost: float, rasstoyanie=None):
        self._name = name                # Защищенный атрибут
        self._vmestimost = vmestimost    # Защищенный атрибут
        self._sr_skorost = sr_skorost    # Защищенный атрибут
        self._rasstoyanie = rasstoyanie  # Защищенный атрибут
        self.validate_vmestimost(vmestimost)
        self.validate_sr_skorost(sr_skorost)

    # Геттеры и сеттеры для всех основных атрибутов
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError("Имя должно содержать хотя бы один символ.")

    @property
    def vmestimost(self):
        return self._vmestimost

    @vmestimost.setter
    def vmestimost(self, value):
        if value >= 1:
            self._vmestimost = value
        else:
            raise ValueError("Вместимость должна быть минимум 1.")

    @property
    def sr_skorost(self):
        return self._sr_skorost

    @sr_skorost.setter
    def sr_skorost(self, value):
        if value >= 1:
            self._sr_skorost = value
        else:
            raise ValueError("Средняя скорость должна быть минимум 1 км/ч.")

    @property
    def rasstoyanie(self):
        return self._rasstoyanie

    @rasstoyanie.setter
    def rasstoyanie(self, value):
        if value is None or value >= 0:
            self._rasstoyanie = value
        else:
            raise ValueError("Расстояние должно быть неотрицательным или пустым.")

    # validate.py    
        # Проверяем значения атрибутов


    def validate_vmestimost(self, vmestimost):
        if vmestimost < 1:
            raise ValueError("В транспортном средстве не может быть меньше одного места")

    def validate_sr_skorost(self, sr_skorost):
        if sr_skorost < 1:
            raise ValueError("Средняя скорость не может быть ниже 1")

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
            raise ValueError("Расчет невозможен без расстояния")

    def oplatit_proezd_Bus(self):
        if self.rasstoyanie is not None:
            stoimost = self.rasstoyanie * 30
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
    def __init__(self, name, vmestimost, sr_skorost, model):
        super().__init__(name, vmestimost, sr_skorost)
        self._model = model
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if len(value.strip()) > 0:
            self._model = value
        else:
            raise ValueError("Модель должна содержать хотя бы один символ.")
    

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
    
    @property
    def god_vipuska(self):
        return self._god_vipuska

    @god_vipuska.setter
    def god_vipuska(self, value):
        if value >= 1900:
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



# demo.py


# Проверка @property
print("=======================================================")
print("Проверка @property")
print("")

auto1 = Car("Xiaomi", 3, 180, "1")
auto1.name = "Li"
auto1.model = "2"
print(auto1.opisanie())


# Проверка метода __str__ и метода __repr__
print("=======================================================")
print("Проверка метода __str__ и метода __repr__")
print("")

Auto_1 = Car("LADA", 4, 140.01, "X-ray")
Bus_1 = Bus("KAMAZ", 80, 90.05, 2019)

print(Auto_1.__str__())
print(Bus_1.__repr__())

# Проверка ограничений и корректности ввода
print("=======================================================")
print("Проверка ограничений и корректности ввода")
print("")

try: 
    Auto_exp = Car("", 2, -30, "10")
except:
    pass

# Проверка метода __eq__
print("=======================================================")
print("Проверка метода __eq__")
print("")

# Создание экземпляров объектов
car1 = Car("Toyota Camry", 5, 120.0, "Camry SE")
car2 = Car("Toyota Camry", 5, 120.0, "Camry SE")
car3 = Car("Honda Civic", 4, 110.0, "Civic EX")

bus1 = Bus("ПАЗ", 20, 80.0, 2020)
bus2 = Bus("ПАЗ", 20, 80.0, 2020)
bus3 = Bus("ЛИАЗ", 30, 70.0, 2018)

# == равно .__eq__()
print(car1.__eq__(car2))  # Должно вернуть True
print(car1 == car3)  # Должно вернуть False
print(bus1.__eq__(bus2))  # Должно вернуть True
print(bus1 == bus3)  # Должно вернуть False

# print(Auto_1.opisanie())
# print(Bus_1.opisanie())

