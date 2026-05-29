'''
Теория вопрос 1:
Что такое замыкание (closure) в Python?
Замыкание - это когда внутренняя функция может запоминать переменную из внешней функции и использовать её 
даже после закрытия внешней функции. Это функция, которая берёт с собой данные из того места, где она была создана.
Пример: счётчик, когда при вызове несколько раз внешней функции, она возвращает новый результат каждый раз.

Что такое «свободная переменная» и где она хранится после возврата из объемлющей функции?
Свободная переменная - это переменная, которая может использоваться во внутренней функции, но она в ней не определена,
а определена где-то снаружи функции. Питон создаёт ячейку памяти cell и хранит в ней переменную из внешней функции, 
пока внутренняя работает и в ней существует объект, а внутренней он даёт ссылку на эту ячейку.

Чем замыкание отличается от обычной вложенной функции?
Вложенную функцию мы просто вызываем в конце внешней функции, а когда у нас замыкание, мы не вызываем вложенную функцию,
а возвращаем её как объект. Вложенная функция уничтожается после вызова, а в замыкании она сохраняется и может использоваться 
дальше, уже храня какую-то информацию прошлых использований.


Пример (псевдокод)
Опишите с помощью псевдокода фабричную функцию make_speed_checker(max_speed), которая возвращает функцию-предикат. Возвращённая функция принимает объект транспорта и проверяет, не превышает ли его скорость заданный лимит. Поясните, где «живёт» переменная max_speed после возврата.

def make_speed_checker(max_speed):
    # Внутренняя функция, которая "запоминает" max_speed
    def normalno_tak_ezdet_A(transport):
        return transport.speed <= max_speed
    
    return normalno_tak_ezdet_A



# Два контроллера с разными лимитами
speed1 = make_speed_checker(60)   # Лимит не гоняйте пацаны
speed2 = make_speed_checker(390) # Лимит гоняйте пацаны

# Предположим, у нас есть объект транспорта (например, машина)
class Pushka_gonka:
    def __init__(self, speed):
        self.speed = speed

car = Pushka_gonka(200)

# Работа созданных функций предикатов:
print(speed1(car)) # Выведет False
print(speed2(car)) # Выведет True


Каждая функция контроллер (speed1, speed2) 
несет в себе «свой» собственный, неизменный лимит скорости.
Когда питон видит, что внутренняя функция normalno_tak_ezdet_A использует переменную max_speed 
из внешней функции, он создает ячейку cell и хранит значение в ней.



Покажите в псевдокоде классическую ловушку замыкания в цикле: внутри цикла создаётся несколько функций, ссылающихся на счётчик цикла. Почему все они возвращают одно и то же значение? Опишите способ исправления

# 1. Создаем пустой список для хранения функций
список_функций = []

# 2. Запускаем цикл от 0 до 2
ДЛЯ i В [0, 1, 2]:

    # 3. Внутри цикла создаем функцию
    #    Эта функция (по замыслу) должна возвращать текущее значение i.
    ФУНКЦИЯ f():
        ВОЗВРАТ i

    # 4. Добавляем созданную функцию в наш список
    ДОБАВИТЬ f В список_функций

# 5. Цикл закончился. Переменная i теперь имеет последнее значение, которое ей присваивал цикл.
#    В нашем случае это 2.
#    Значение i = 2.

ВЫЗВАТЬ список_функций[0]()
ВЫЗВАТЬ список_функций[1]()
ВЫЗВАТЬ список_функций[2]()

Везде получаем 2
В цикле используется одна и та же переменная i. На каждой итерации её значение просто перезаписывается.
Функции в цикле не запоминают значение i в момент своего создания, а запоминают переменную i.
Значение переменной i ищется не в момент создания функции, а только в момент её вызова.
Переменная i осталась в памяти со своим последним значением = 2. Поэтому все функции смотрят на одну и ту же переменную i и видят 2.


Исправленный способ:

список_функций = []

ДЛЯ i В [0, 1, 2]:

    # Создаем функцию с аргументом x, у которого есть значение по умолчанию i
    ФУНКЦИЯ f(x = i):
        ВОЗВРАТ x

    ДОБАВИТЬ f В список_функций

ВЫЗВАТЬ список_функций[0]()
ВЫЗВАТЬ список_функций[1]()
ВЫЗВАТЬ список_функций[2]()


Здесь x становится локальной переменной для каждой функции, и ей сразу присваивается текущее значение i.



'''

# Задание 2

class Car:
    """
    Класс, моделирующий автомобиль автопарка.
    """

    def __init__(self, plate: str, model: str, max_speed: int, 
                 current_speed: int = 0, fuel_level: float = 50.0) -> None:
        """
        Инициализация автомобиля.

        :param plate: Номер авто (6 символов).
        :param model: Модель авто.
        :param max_speed: Максимальная скорость (50-400).
        :param current_speed: Текущая скорость (по умолчанию 0).
        :param fuel_level: Уровень топлива (по умолчанию 50.0).
        :raises ValueError: Если параметры не проходят валидацию.
        """
        # Валидация и установка номера
        if not plate or len(plate) != 6:
            raise ValueError("plate должен быть непустой строкой из 6 символов")
        self._plate = plate

        # Валидация и установка модели
        model_stripped = model.strip()
        if not model_stripped:
            raise ValueError("model не может быть пустой строкой")
        self._model = model_stripped

        # Валидация и установка максимальной скорости
        if not (50 <= max_speed <= 400):
            raise ValueError("max_speed должен быть в диапазоне от 50 до 400 включительно")
        self._max_speed = max_speed

        # Установка текущей скорости через сеттер для валидации
        self.current_speed = current_speed 

        # Попытка установить топливо через сеттер
        # Если fuel_level по умолчанию (50.0) невалиден, это вызовет ошибку,
        # что соответствует логике валидации входных данных.
        self.fuel_level = fuel_level 

    # --- Свойства (Properties) ---

    @property
    def plate(self) -> str:
        return self._plate

    @property
    def model(self) -> str:
        return self._model

    @property
    def max_speed(self) -> int:
        return self._max_speed

    @property
    def current_speed(self) -> int:
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value: int) -> None:
        # Ограничение значения в пределах [0, max_speed]
        self._current_speed = max(0, min(value, self._max_speed))

    @property
    def fuel_level(self) -> float:
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, value: float) -> None:
        # Ограничение значения в пределах [0, 100]
        self._fuel_level = max(0.0, min(float(value), 100.0))

    # --- Методы управления ---

    def accelerate(self, delta: int) -> None:
        """
        Увеличивает текущую скорость на delta, не превышая max_speed.

        :param delta: Значение, на которое нужно увеличить скорость.
                       Если отрицательное, сработает как торможение.
                       Если не int/float, будет проигнорировано.
        """
        try:
            new_speed = self._current_speed + float(delta)
            self.current_speed = new_speed # Используем сеттер для ограничения
        except (TypeError, ValueError):
            # Игнорируем некорректный ввод
            pass

    def brake(self, delta: int) -> None:
        """
        Уменьшает текущую скорость на delta, не опускаясь ниже 0.

        :param delta: Значение, на которое нужно уменьшить скорость.
                      Если отрицательное, сработает как ускорение.
                      Если не int/float, будет проигнорировано.
        """
        try:
            new_speed = self._current_speed - float(delta)
            self.current_speed = new_speed # Используем сеттер для ограничения
        except (TypeError, ValueError):
            # Игнорируем некорректный ввод
            pass

    def refuel(self, litres: float) -> None:
        """
         Пополняет уровень топлива.

         :param litres: Количество литров для заправки. Должно быть > 0.
                        Если не число или <= 0, действие игнорируется.
        """
        if isinstance(litres, (int, float)) and litres > 0:
            # Используем сеттер для ограничения итогового значения
            self.fuel_level += litres 

    # --- Магические методы ---

    def __str__(self) -> str:
         """Возвращает строковое представление автомобиля."""
         return (f"{self.model} [{self.plate}]: "
                 f"{self.current_speed}/{self.max_speed} км/ч, "
                 f"топливо {self.fuel_level:.1f}л")

    def __eq__(self, other: object) -> bool:
         """Проверяет равенство автомобилей по номеру (plate)."""
         if isinstance(other, Car):
             return self.plate == other.plate
         return False
    

car = Car('A123BC', 'Toyota Camry', 200, 0, 45)
car.accelerate(60)
print(car.current_speed)  # 60
car.accelerate(200)       # обрежется до 200
print(car.current_speed)  # 200
car.brake(500)
print(car.current_speed)  # 0


Car('', 'Toyota', 200)      # ValueError: plate пустой
Car('A123BC', 'Toyota', 30) # ValueError: max_speed < 50





# Задание 3

from abc import ABC, abstractmethod
from typing import Callable, Dict, List

# Предполагается, что класс Car находится в car.py в той же папке
from car import Car

# --- Шаг 1: Класс Fleet ---

class Fleet:
    """
    Коллекция автомобилей с методами фильтрации и сортировки.
    """
    def __init__(self) -> None:
        # Используем список для хранения объектов Car
        self._cars: List[Car] = []
        # Словарь для быстрой проверки уникальности номера (plate)
        self._plates: Dict[str, bool] = {}

    def add(self, car: Car) -> None:
        """
        Добавляет автомобиль в парк.
        Проверяет тип объекта и уникальность номера.
        
        :param car: Объект класса Car.
        :raises TypeError: Если передан не объект Car.
        :raises ValueError: Если автомобиль с таким номером уже есть.
        """
        if not isinstance(car, Car):
            raise TypeError("В парк можно добавлять только объекты класса Car")
        
        if car.plate in self._plates:
            raise ValueError(f"Автомобиль с номером {car.plate} уже есть в парке")
        
        self._cars.append(car)
        self._plates[car.plate] = True

    def __len__(self) -> int:
        """Возвращает количество автомобилей в парке."""
        return len(self._cars)

    def __iter__(self):
        """Позволяет итерироваться по парку: for car in fleet:"""
        return iter(self._cars)

    def filter_by(self, predicate: Callable[[Car], bool]) -> 'Fleet':
        """
        Фильтрует парк по заданному предикату.
        
        :param predicate: Функция, принимающая Car и возвращающая bool.
        :return: Новый объект Fleet с отфильтрованными машинами.
        """
        new_fleet = Fleet()
        for car in self._cars:
            if predicate(car):
                # Добавляем без проверки типа и уникальности,
                # так как это копии из текущего валидного парка.
                new_fleet._cars.append(car)
                new_fleet._plates[car.plate] = True
        return new_fleet

    def sort_by(self, key_func: Callable[[Car], any]) -> 'Fleet':
        """
        Сортирует парк по заданному ключу.
        
        :param key_func: Функция, принимающая Car и возвращающая значение для сортировки.
        :return: Новый объект Fleet с отсортированными машинами.
        """
        new_fleet = Fleet()
        # sorted() возвращает новый отсортированный список
        sorted_cars = sorted(self._cars, key=key_func)
        for car in sorted_cars:
            new_fleet._cars.append(car)
            new_fleet._plates[car.plate] = True
        return new_fleet

    def estimate_trip(self, strategy: 'TripCostStrategy', distance_km: float) -> Dict[str, float]:
        """
        Оценивает стоимость поездки для всех машин парка по заданной стратегии.
        
        :param strategy: Объект стратегии расчета стоимости.
        :param distance_km: Дистанция поездки в километрах.
        :return: Словарь {номер_авто: стоимость_поездки}.
        """
        costs = {}
        for car in self._cars:
            costs[car.plate] = strategy.calculate(car, distance_km)
        return costs

# --- Шаг 2: Фабрики фильтров (Замыкания) ---

def make_speed_filter(min_speed: int, max_speed: int) -> Callable[[Car], bool]:
    """
    Фабрика функций-фильтров по максимальной скорости.
    
    :param min_speed: Минимальная граница скорости (включительно).
    :param max_speed: Максимальная граница скорости (включительно).
    :return: Функция-предикат для фильтрации.
    """
    def predicate(car: Car) -> bool:
         return min_speed <= car.max_speed <= max_speed
    return predicate

def make_fuel_filter(min_fuel: float) -> Callable[[Car], bool]:
    """
    Фабрика функций-фильтров по уровню топлива.
    
    :param min_fuel: Минимальный уровень топлива (включительно).
    :return: Функция-предикат для фильтрации.
    """
    def predicate(car: Car) -> bool:
         return car.fuel_level >= min_fuel
    return predicate

def make_model_filter(model_substring: str) -> Callable[[Car], bool]:
    """
    Фабрика функций-фильтров по подстроке в названии модели.
    
    :param model_substring: Подстрока для поиска (поиск без учета регистра).
    :return: Функция-предикат для фильтрации.
    """
    substr_lower = model_substring.lower()
    def predicate(car: Car) -> bool:
         return substr_lower in car.model.lower()
    return predicate

# --- Шаг 3: Стратегии расчета стоимости ---

class TripCostStrategy(ABC):
    """
    Абстрактный базовый класс для стратегий расчета стоимости поездки.
    """
    @abstractmethod
    def calculate(self, car: Car, distance_km: float) -> float:
        """
        Абстрактный метод расчета стоимости.
        
        :param car: Автомобиль, для которого считается стоимость.
        :param distance_km: Дистанция поездки в км.
        :return: Стоимость поездки.
        """
        pass

class FlatRate(TripCostStrategy):
    """
    Стратегия с фиксированной ставкой за километр.
    """
    def __init__(self, rate_per_km: float):
         self.rate_per_km = rate_per_km

    def calculate(self, car: Car, distance_km: float) -> float:
         return self.rate_per_km * distance_km

class FuelBased(TripCostStrategy):
    """
    Стратегия расчета на основе расхода топлива и его цены.
    """
    def __init__(self, price_per_litre: float, consumption_per_100km: float):
         self.price_per_litre = price_per_litre
         self.consumption_per_100km = consumption_per_100km

    def calculate(self, car: Car, distance_km: float) -> float:
         # Расход на всю дистанцию (в литрах)
         total_litres = (distance_km / 100) * self.consumption_per_100km
         return total_litres * self.price_per_litre

class SpeedBased(TripCostStrategy):
    """
    Стратегия расчета на основе базовой ставки и коэффициента скорости.
    """
    def __init__(self, base_rate: float, speed_coef: float):
        self.base_rate = base_rate
        self.speed_coef = speed_coef

    def calculate(self, car: Car, distance_km: float) -> float:
        # base_rate за км + доплата за скорость (max_speed * коэффициент)
        return (self.base_rate * distance_km) + (self.speed_coef * car.max_speed)
    

fleet = Fleet()
fleet.add(Car('A001AA', 'Toyota Camry', 220, 0, 80))
fleet.add(Car('B002BB', 'Lada Vesta', 180, 0, 30))
fleet.add(Car('C003CC', 'Toyota Prius', 170, 0, 70))


fast = fleet.filter_by(make_speed_filter(200, 300))
print(len(fast))                # 1


fueled = fleet.filter_by(make_fuel_filter(50))
for c in fueled.sort_by(lambda c: -c.fuel_level):
    print(c)                    # Toyota Camry, Toyota Prius


toyota = fleet.filter_by(make_model_filter('toyota'))
print(len(toyota))              # 2


costs = fleet.estimate_trip(FlatRate(20), 100)
print(costs)                    # {'A001AA': 2000, 'B002BB': 2000, ...}


costs = fleet.estimate_trip(FuelBased(55, 8), 100)
print(costs)                    # стоимость по расходу топлива


costs = fleet.estimate_trip(SpeedBased(15, 2), 100)
# {'A001AA': 1500 + 2*220 = 1940, ...}
