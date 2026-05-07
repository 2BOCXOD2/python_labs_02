from typing import List, Iterator, Callable, Any

class Fleet:
    def __init__(self):
        self._items: List = []

    def add(self, item) -> None:
        self._items.append(item)

    def remove(self, item) -> None:
        self._items.remove(item)

    def get_all(self) -> List:
        return self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator:
        return iter(self._items)
    
    # ЗАДАНИЕ 1 -----------------------------------------------------

    # --- НОВЫЙ МЕТОД: СОРТИРОВКА ПО СТРАТЕГИИ ---
    def sort_by_strategy(self, strategy_func: Callable):
        """
        Сортирует коллекцию, используя переданную функцию-стратегию.
        Использует встроенную функцию sorted() с параметром key=.
        """
        # sorted() возвращает НОВЫЙ отсортированный список
        self._items = sorted(self._items, key=strategy_func)
    
    # --- НОВЫЙ МЕТОД: ФИЛЬТРАЦИЯ ПО СТРАТЕГИИ ---
    def filter_by_strategy(self, filter_func: Callable) -> 'Fleet':
        """
        Возвращает НОВУЮ коллекцию, отфильтрованную по переданной функции.
        Использует встроенную функцию filter().
        """
        new_fleet = Fleet()
        # filter() возвращает итератор. Мы оборачиваем его в list().
        filtered_items = list(filter(filter_func, self._items))
        new_fleet._items = filtered_items # Наполняем новую коллекцию напрямую для эффективности
        return new_fleet
    
    # ЗАДАНИЕ 2 -----------------------------------------------------

    # --- НОВЫЙ МЕТОД: ПРЕОБРАЗОВАНИЕ ЧЕРЕЗ MAP() ---
    
    '''
    def apply(self, transform_func: Callable) -> List[Any]:
        """
        Применяет функцию-трансформер к каждому объекту в коллекции.
        Аналог функции map().
        Возвращает список преобразованных объектов.
        """
        return list(map(transform_func, self._items))

    
    # --- НОВЫЙ МЕТОД: СОРТИРОВКА ---
    def sort_by(self, key_func: Callable):
        """
        Сортирует коллекцию по ключу, используя переданную функцию.
        Пример использования: my_collection.sort_by(lambda x: x.name)
        """
        self._items = sorted(self._items, key=key_func)

    # --- НОВЫЙ МЕТОД: ФИЛЬТРАЦИЯ ---
    def filter_by(self, predicate_func: Callable) -> 'Fleet':
        """
        Возвращает новую коллекцию, отфильтрованную по предикату.
        Предикат - это функция, возвращающая True или False.
        Пример использования: my_collection.filter_by(lambda x: x.price > 100)
        """
        new_fleet = Fleet()
        new_fleet._items = list(filter(predicate_func, self._items))
        return new_fleet
    '''

    # ЗАДАНИЕ 3 -----------------------------------------------------

    # --- НОВЫЙ МЕТОД: ПРИМЕНЕНИЕ ПРОИЗВОЛЬНОЙ ФУНКЦИИ ---
    def apply(self, func: Callable) -> List[Any]:
        """
        Применяет произвольную функцию (стратегию) ко всем элементам коллекции.
        
        Args:
            func: Callable-объект или функция, принимающая один аргумент (элемент).
            
        Returns:
            Список с результатами применения функции к каждому элементу.
        """
        return [func(item) for item in self._items]
    
    # --- МЕТОДЫ ДЛЯ ЦЕПОЧЕК (CHAINING) ---
    # Они возвращают self, чтобы можно было продолжать вызывать методы

    def filter_by(self, predicate_func: Callable) -> 'Fleet':
        """
        Фильтрует коллекцию по предикату. Возвращает СЕБЯ для цепочек.
        
        Args:
            predicate_func: Функция, возвращающая True/False для элемента.
            
        Returns:
            self: Текущий объект Fleet с отфильтрованными элементами.
        """
        self._items = list(filter(predicate_func, self._items))
        return self

    def sort_by(self, key_func: Callable) -> 'Fleet':
        """
        Сортирует коллекцию по ключу. Возвращает СЕБЯ для цепочек.
        
        Args:
            key_func: Функция, возвращающая значение для сортировки элемента.
            
        Returns:
            self: Текущий объект Fleet с отсортированными элементами.
        """
        self._items = sorted(self._items, key=key_func)
        return self