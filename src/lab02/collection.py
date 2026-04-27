'''
from typing import Type, List, Iterator, Callable, TypeVar
from src.lab01.models import Car, Transport 

T = TypeVar('T')

class Fleet:
    """
    Универсальная коллекция для хранения любых видов транспорта.
    Здесь НЕТ проверки на дубликаты по ID, чтобы она работала с ЛЮБЫМ транспортом.
    """
    def __init__(self):
        self._items: List = [] 

    def add(self, item) -> None: 
        self._items.append(item)

    def remove(self, item: Transport) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[Transport]:
        """Возвращает список всех объектов."""
        return self._items

    # --- НОВЫЙ МЕТОД: Демонстрация полиморфизма ---
    def calculate_total_price(self) -> float:
        """
        Демонстрирует полиморфное поведение.
        Вызывает метод calculate_price() у каждого объекта.
        """
        total = 0.0
        print("Расчет стоимости для каждого объекта:")
        
        for transport in self._items:
            # Полиморфизм: Python сам вызовет нужный метод
            total += transport.calculate_price()
        
        return total
    

    # lab04!!!

    # --- НОВЫЙ МЕТОД: УНИВЕРСАЛЬНАЯ ФИЛЬТРАЦИЯ ---
    def filter_by_interface(self, interface_type) -> 'Fleet':
        """
        Возвращает новую коллекцию с объектами, реализующими заданный интерфейс.
        """
        new_fleet = Fleet()
        for transport in self._items:
            if isinstance(transport, interface_type):
                new_fleet.add(transport)
        return new_fleet

    # --- НОВЫЙ МЕТОД: СОРТИРОВКА ЧЕРЕЗ ИНТЕРФЕЙС ---
    def sort_by_comparable(self) -> None:
        """
        Сортирует коллекцию.
        """
        for item in self._items:
            # Проверка на наличие атрибута 'compare_to', чтобы избежать жесткой привязки к интерфейсу
            if not hasattr(item, 'compare_to'):
                raise TypeError(f"Невозможно отсортировать. Объект {getattr(item, 'name', 'Без имени')} не имеет метода compare_to.")
        
        self._items.sort(key=lambda x: x.name)
'''
### lab02 ################################################

from typing import Type, List, Iterator, Callable, TypeVar
from src.lab01.models import Car, Transport  # Импортируем самый базовый класс # lab02

T = TypeVar('T')

class Fleet:
    """
    Универсальная коллекция для хранения любых видов транспорта.
    Здесь НЕТ проверки на дубликаты по ID, чтобы она работала с ЛЮБЫМ транспортом.
    """
    def __init__(self):
        # Может хранить ЛЮБОЙ объект, наследующий Transport
        self._items: List = [] # self._items: List[Transport] = [] # lab02

    def add(self, item) -> None: # def add(self, item: Transport) -> None: # В лабе 2 вот это
        """
        Добавляет объект в коллекцию.
        Теперь мы не проверяем дубликаты, чтобы избежать ошибок с CargoShip/Airplane.
        """
        self._items.append(item)

    def remove(self, item: Transport) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[Transport]:
        """Возвращает список всех объектов."""
        return self._items

    # --- НОВЫЙ МЕТОД: Демонстрация полиморфизма ---
    def calculate_total_price(self) -> float:
        """
        Демонстрирует полиморфное поведение.
        Вызывает метод calculate_price() у каждого объекта.
        """
        total = 0.0
        print("Расчет стоимости для каждого объекта:")
        
        for transport in self._items:
            # Полиморфизм: Python сам вызовет нужный метод
            total += transport.calculate_price()
        
        return total


    # lab04!!!
    # --- НОВЫЙ МЕТОД: УНИВЕРСАЛЬНАЯ ФИЛЬТРАЦИЯ ---
    def filter_by_interface(self, interface_type) -> 'Fleet':
        """
        Возвращает новую коллекцию с объектами, реализующими заданный интерфейс.
        """
        new_fleet = Fleet()
        for transport in self._items:
            if isinstance(transport, interface_type):
                new_fleet.add(transport)
        return new_fleet

    # --- НОВЫЙ МЕТОД: СОРТИРОВКА ЧЕРЕЗ ИНТЕРФЕЙС ---
    def sort_by_comparable(self) -> None:
        """
        Сортирует коллекцию.
        """
        for item in self._items:
            # Проверка на наличие атрибута 'compare_to', чтобы избежать жесткой привязки к интерфейсу
            if not hasattr(item, 'compare_to'):
                raise TypeError(f"Невозможно отсортировать. Объект {getattr(item, 'name', 'Без имени')} не имеет метода compare_to.")
        
        self._items.sort(key=lambda x: x.name)


    # --- РЕАЛИЗАЦИЯ СПЕЦИАЛЬНЫХ МЕТОДОВ ---
    def __len__(self) -> int:
        """Позволяет использовать функцию len(fleet)."""
        return len(self._items)

    def __iter__(self) -> Iterator[Transport]:
        """Позволяет использовать коллекцию в циклах for."""
        return iter(self._items)
    
    # --- НОВЫЕ МЕТОДЫ ДЛЯ ФИЛЬТРАЦИИ --- lab03
    
    def filter_by_type(self, type_to_find: Type[Transport]) -> 'Fleet':
        """
        Возвращает НОВУЮ коллекцию, содержащую только объекты указанного типа.
        
        Пример использования: fleet.filter_by_type(Car)
        
        Args:
            type_to_find: Класс, объекты которого нужно найти (например, Car или CargoShip).
            
        Returns:
            Новый объект Fleet с отфильтрованными элементами.
        """
        new_fleet = Fleet()
        for transport in self._items:
            if isinstance(transport, type_to_find):
                new_fleet.add(transport)
        return new_fleet

    # Для удобства — методы-сокращения (как ты и просил)
    def get_only_cars(self) -> 'Fleet':
        """Возвращает новую коллекцию только с автомобилями."""
        return self.filter_by_type(Car)

    def get_only_cargo_ships(self) -> 'Fleet':
        """Возвращает новую коллекцию только с грузовыми кораблями."""
        from src.lab03.models import CargoShip # Импорт здесь, чтобы избежать циклических зависимостей
        return self.filter_by_type(CargoShip)


        

####################
'''
from typing import List, Iterator, Callable
from src.lab01.models import Transport # Импортируем самый базовый класс

class Fleet:
    """
    Универсальная коллекция для хранения любых видов транспорта.
    """
    def __init__(self):
        # Теперь список может хранить ЛЮБОЙ объект, наследующий Transport
        self._items: List[Transport] = [] 

    def add(self, item: Transport) -> None:
        """
        Добавляет объект в коллекцию, если он является транспортом.
        
        Args:
            item: Объект для добавления.
            
        Raises:
            TypeError: Если объект не является наследником Transport.
            ValueError: Если объект с таким же ID уже существует.
        """
        # Проверка типа через isinstance()
        if not isinstance(item, Transport):
            raise TypeError("В коллекцию Fleet можно добавлять только объекты типа Transport.")

        # Проверка на дубликат по ID (унаследована из логики)
        for existing in self._items:
            if existing.id == item.id:
                raise ValueError(f"Транспорт с ID {item.id} уже существует.")
                
        self._items.append(item)

    def remove(self, item: Transport) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[Transport]:
        """Возвращает список всех объектов в коллекции."""
        return self._items

    # --- НОВЫЙ МЕТОД: Демонстрация полиморфизма ---
    def calculate_total_price(self) -> float:
        """
        Демонстрирует полиморфное поведение.
        Вызывает метод calculate_price() у каждого объекта в коллекции.
        
        Возвращает:
            Суммарную стоимость всех транспортов в коллекции.
        """
        total = 0.0
        print("Расчет стоимости для каждого объекта:")
        
        for transport in self._items:
            # Полиморфизм в действии:
            # Python сам вызовет нужный метод (Car.calculate_price или CargoShip.calculate_price)
            total += transport.calculate_price()
            
            # Проверка типа для красивого вывода
            if hasattr(transport, 'model'): # У Car есть атрибут 'model'
                print(f"Автомобиль {transport.name} ({transport.model}): {transport.calculate_price()} у.е.")
            elif hasattr(transport, 'cargo_capacity_tons'): # У CargoShip есть этот атрибут
                print(f"Корабль {transport.name}: {transport.calculate_price()} у.е.")
        
        return total
    

    def remove(self, item: Car) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[Car]:
        """Возвращает список всех объектов в коллекции."""
        return self._items

    # --- НОВЫЕ МЕТОДЫ ПОИСКА ---
    
    def find_by_name(self, name: str) -> Optional[Car]:
        """
        Ищет автомобиль по его имени.
        
        Returns:
            Первый найденный автомобиль или None, если не найден.
        """
        for car in self._items:
            if car.name == name:
                return car
        return None

    def find_by_id(self, car_id: int) -> Optional[Car]:
        """
        Ищет автомобиль по его уникальному ID.
        
        Returns:
            Автомобиль или None, если не найден.
        """
        for car in self._items:
            if car.id == car_id:
                return car
        return None
    
    # --- НОВЫЙ МЕТОД: УДАЛЕНИЕ ПО ИНДЕКСУ ---
    def remove_at(self, index: int) -> None:
        """
        Удаляет объект из коллекции по его индексу.
        
        Args:
            index: Индекс объекта в коллекции.
            
        Raises:
            IndexError: Если индекс выходит за границы коллекции.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона коллекции.")
        self._items.pop(index)

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: ИНДЕКСАЦИЯ ---
    def __getitem__(self, index: int) -> Car:
        """
        Позволяет использовать синтаксис collection[index] для доступа к элементам.
        
        Args:
            index: Индекс объекта.
            
        Returns:
            Объект Car по указанному индексу.
            
        Raises:
            IndexError: Если индекс выходит за границы коллекции.
        """
        return self._items[index]

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: СОРТИРОВКА ---
    def sort(self, key: Callable[[Car], any]) -> None:
        """
        Сортирует коллекцию по заданному ключу.
        
        Args:
            key: Функция, которая принимает объект Car и возвращает значение для сортировки.
                  Например: lambda car: car.name или lambda car: car.price
        """
        self._items.sort(key=key)

    # Для удобства можно добавить методы-сокращения
    def sort_by_name(self) -> None:
        """Сортирует коллекцию по имени автомобиля (по возрастанию)."""
        self.sort(key=lambda car: car.name)

    def sort_by_price(self) -> None:
        """Сортирует коллекцию по цене автомобиля (по возрастанию)."""
        self.sort(key=lambda car: car.price)

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: ФИЛЬТРАЦИЯ (ЛОГИЧЕСКИЕ ОПЕРАЦИИ) ---
    def filter(self, condition: Callable[[Car], bool]) -> 'Fleet':
        """
        Возвращает НОВУЮ коллекцию, содержащую только те объекты, для которых условие истинно.
        
        Args:
            condition: Функция, которая принимает объект Car и возвращает True или False.
        
        Returns:
            Новый объект Fleet с отфильтрованными элементами.
        """
        new_fleet = Fleet()
        for car in self._items:
            if condition(car):
                new_fleet.add(car)
        return new_fleet

    # Примеры методов-фильтров
    def get_expensive(self, threshold: float) -> 'Fleet':
        """
        Возвращает новую коллекцию с автомобилями, цена которых выше порога.
        
        Args:
            threshold: Минимальная цена для отбора.
            
        Returns:
            Новый объект Fleet с дорогими автомобилями.
        """
        return self.filter(lambda car: car.price > threshold)


    # --- РЕАЛИЗАЦИЯ СПЕЦИАЛЬНЫХ МЕТОДОВ (МАГИЧЕСКИХ МЕТОДОВ) ---
    
    def __len__(self) -> int:
        """Позволяет использовать функцию len(fleet)."""
        return len(self._items)

    def __iter__(self) -> Iterator[Transport]:
        """
        Позволяет использовать коллекцию в циклах for.
            for car in fleet:
                print(car)
        """
        return iter(self._items)
'''


###################################
'''
from typing import List, Iterator, Optional, Callable
from src.lab01.models import Car, Transport

class Fleet:
    """
    Контейнер для хранения и управления коллекцией автомобилей (Car).
    Реализует поиск, защиту от дубликатов и протокол итерирования.
    """

    def __init__(self):
        """Инициализирует пустой список для хранения автомобилей."""
        self._items: List[Car] = []

    def add(self, item: Transport) -> None:
        """
        Добавляет объект в коллекцию с проверкой на дубликаты.
        
        Проверяет:
        1. Тип объекта (должен быть Car).
        2. Отсутствие дубликата по ID.
        3. Отсутствие другого автомобиля с таким же именем.
        
        Args:
            item: Объект для добавления в коллекцию.
            
        Raises:
            TypeError: Если объект не является экземпляром класса Car.
            ValueError: Если объект является дубликатом.
        """
        if not isinstance(item, Transport):
            raise TypeError("В коллекцию Fleet можно добавлять только объекты типа Transport.")
        
        
        if not isinstance(item, Car):
            raise TypeError("В коллекцию Fleet можно добавлять только объекты класса Car.")
        
        # Проверка на дубликат по ID (самый надежный способ)
        if self.find_by_id(item.id):
            raise ValueError(f"Автомобиль с ID {item.id} уже есть в автопарке.")
        
        # Проверка на дубликат по имени (дополнительное бизнес-правило)
        if self.find_by_name(item.name):
            raise ValueError(f"Автомобиль с именем '{item.name}' уже есть в автопарке.")
        
        self._items.append(item)

    def remove(self, item: Car) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[Car]:
        """Возвращает список всех объектов в коллекции."""
        return self._items

    # --- НОВЫЕ МЕТОДЫ ПОИСКА ---
    
    def find_by_name(self, name: str) -> Optional[Car]:
        """
        Ищет автомобиль по его имени.
        
        Returns:
            Первый найденный автомобиль или None, если не найден.
        """
        for car in self._items:
            if car.name == name:
                return car
        return None

    def find_by_id(self, car_id: int) -> Optional[Car]:
        """
        Ищет автомобиль по его уникальному ID.
        
        Returns:
            Автомобиль или None, если не найден.
        """
        for car in self._items:
            if car.id == car_id:
                return car
        return None
    
    # --- НОВЫЙ МЕТОД: УДАЛЕНИЕ ПО ИНДЕКСУ ---
    def remove_at(self, index: int) -> None:
        """
        Удаляет объект из коллекции по его индексу.
        
        Args:
            index: Индекс объекта в коллекции.
            
        Raises:
            IndexError: Если индекс выходит за границы коллекции.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона коллекции.")
        self._items.pop(index)

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: ИНДЕКСАЦИЯ ---
    def __getitem__(self, index: int) -> Car:
        """
        Позволяет использовать синтаксис collection[index] для доступа к элементам.
        
        Args:
            index: Индекс объекта.
            
        Returns:
            Объект Car по указанному индексу.
            
        Raises:
            IndexError: Если индекс выходит за границы коллекции.
        """
        return self._items[index]

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: СОРТИРОВКА ---
    def sort(self, key: Callable[[Car], any]) -> None:
        """
        Сортирует коллекцию по заданному ключу.
        
        Args:
            key: Функция, которая принимает объект Car и возвращает значение для сортировки.
                  Например: lambda car: car.name или lambda car: car.price
        """
        self._items.sort(key=key)

    # Для удобства можно добавить методы-сокращения
    def sort_by_name(self) -> None:
        """Сортирует коллекцию по имени автомобиля (по возрастанию)."""
        self.sort(key=lambda car: car.name)

    def sort_by_price(self) -> None:
        """Сортирует коллекцию по цене автомобиля (по возрастанию)."""
        self.sort(key=lambda car: car.price)

    # --- НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: ФИЛЬТРАЦИЯ (ЛОГИЧЕСКИЕ ОПЕРАЦИИ) ---
    def filter(self, condition: Callable[[Car], bool]) -> 'Fleet':
        """
        Возвращает НОВУЮ коллекцию, содержащую только те объекты, для которых условие истинно.
        
        Args:
            condition: Функция, которая принимает объект Car и возвращает True или False.
        
        Returns:
            Новый объект Fleet с отфильтрованными элементами.
        """
        new_fleet = Fleet()
        for car in self._items:
            if condition(car):
                new_fleet.add(car)
        return new_fleet

    # Примеры методов-фильтров
    def get_expensive(self, threshold: float) -> 'Fleet':
        """
        Возвращает новую коллекцию с автомобилями, цена которых выше порога.
        
        Args:
            threshold: Минимальная цена для отбора.
            
        Returns:
            Новый объект Fleet с дорогими автомобилями.
        """
        return self.filter(lambda car: car.price > threshold)

    # --- РЕАЛИЗАЦИЯ СПЕЦИАЛЬНЫХ МЕТОДОВ (МАГИЧЕСКИХ МЕТОДОВ) ---
    
    def __len__(self) -> int:
        """Позволяет использовать функцию len(fleet)."""
        return len(self._items)

    def __iter__(self) -> Iterator[Car]:
        """
        Позволяет использовать коллекцию в циклах for:
            for car in fleet:
                print(car)
        """
        return iter(self._items)
'''