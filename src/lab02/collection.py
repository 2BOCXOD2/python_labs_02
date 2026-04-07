from typing import List, Iterator, Optional, Callable
from src.lab01.models import Car

class Fleet:
    """
    Контейнер для хранения и управления коллекцией автомобилей (Car).
    Реализует поиск, защиту от дубликатов и протокол итерирования.
    """

    def __init__(self):
        """Инициализирует пустой список для хранения автомобилей."""
        self._items: List[Car] = []

    def add(self, item: Car) -> None:
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