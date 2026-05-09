############################# Рабочий вариант со всеми методами из ЛР 2

from typing import TypeVar, Generic, List, Iterator, Type, Callable, Any, Optional, Protocol


class Displayable(Protocol):
    """
    Протокол для объектов, которые можно отобразить.
    Любой класс, у которого есть метод display(), считается соответствующим этому протоколу.
    """
    def display(self) -> str:
        ...

class Scorable(Protocol):
    """
    Протокол для объектов, которые можно оценить (проставить балл).
    Любой класс, у которого есть метод score(), считается соответствующим этому протоколу.
    """
    def score(self) -> float:
        ...

# --- 2) TYPEVAR С ОГРАНИЧЕНИЯМИ (BOUND) ---

# T - для общего случая (любой тип)
# T - это переменная типа. Она обозначает "любой тип", который мы укажем при создании коллекции.
T = TypeVar('T')
R = TypeVar('R')

# D - только для типов, соответствующих протоколу Displayable
D = TypeVar('D', bound=Displayable)

# S - только для типов, соответствующих протоколу Scorable
S = TypeVar('S', bound=Scorable)



class TypedCollection(Generic[T]):
    """
    Типизированная коллекция, которая хранит объекты только заданного типа T.
    Повторяет интерфейс коллекции из ЛР-2, но с проверкой типов и аннотациями.
    """

    def __init__(self, item_type: Type[T] = None) -> None:
        """
        Инициализация коллекции.
        
        Args:
            item_type: Тип объектов, которые будут храниться в коллекции.
                      Если None, проверка типов при добавлении не выполняется.
        """
        self._items: List[T] = []
        self._item_type = item_type

    # --- БАЗОВЫЕ МЕТОДЫ (ИЗ ЛР-2) ---

    def add(self, item: T) -> None:
        """
        Добавляет объект в коллекцию с проверкой типа.
        
        Args:
            item: Объект для добавления.
            
        Raises:
            TypeError: Если тип объекта не совпадает с ожидаемым типом коллекции.
        """
        if self._item_type is not None and not isinstance(item, self._item_type):
            raise TypeError(
                f"Невозможно добавить объект типа {type(item).__name__}. "
                f"Ожидается тип {self._item_type.__name__}."
            )
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает список всех объектов в коллекции."""
        return list(self._items)


    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит и возвращает первый элемент, удовлетворяющий условию (предикату).
        
        Args:
            predicate: Функция, которая принимает элемент и возвращает True/False.
            
        Returns:
            Первый найденный элемент или None, если ничего не найдено.
        """
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """
        Возвращает список всех элементов, удовлетворяющих условию (предикату).
        
        Args:
            predicate: Функция, которая принимает элемент и возвращает True/False.
            
        Returns:
            Список элементов типа T.
        """
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """
        Применяет функцию-преобразование к каждому элементу коллекции.
        
        Args:
            transform: Функция, которая принимает элемент типа T и возвращает элемент типа R.
            
        Returns:
            Список результатов типа R. Тип результата может отличаться от типа элементов коллекции.
        """
        return [transform(item) for item in self._items]
    

    # --- 3) НОВЫЕ МЕТОДЫ, ИСПОЛЬЗУЮЩИЕ ПРОТОКОЛЫ ---

    def display_all(self: 'TypedCollection[D]') -> None:
        """
        Демонстрация работы с Protocol.
        Принимает коллекцию объектов, соответствующих протоколу Displayable.
        Вызывает метод .display() у каждого.
        """
        for item in self._items:
            # IDE теперь знает, что у item точно есть метод display()
            print(item.display())

    def calculate_average_score(self: 'TypedCollection[S]') -> float:
        """
        Демонстрация работы со вторым протоколом.
        Принимает коллекцию объектов, соответствующих протоколу Scorable.
        """
        if not self._items:
            return 0.0
        
        total = sum(item.score() for item in self._items)
        return total / len(self._items)
    

    # --- МЕТОДЫ ДЛЯ ПОЛИМОРФИЗМА И ОБРАБОТКИ (ИЗ ЛР-2/4) ---

    def calculate_total_price(self) -> float:
        """
        Демонстрирует полиморфное поведение.
        Вызывает метод calculate_price() у каждого объекта, если он есть.
        """
        total = 0.0
        print("Расчет стоимости для каждого объекта:")
        
        for item in self._items:
            # Проверяем наличие метода, чтобы работать с ЛЮБЫМ типом T, а не только Transport
            if hasattr(item, 'calculate_price'):
                total += item.calculate_price()
        
        return total

    # --- МЕТОДЫ ФИЛЬТРАЦИИ (ИЗ ЛР-3/4) ---

    def filter_by_type(self, type_to_find: Type[T]) -> 'TypedCollection[T]':
        """
        Возвращает НОВУЮ коллекцию, содержащую только объекты указанного типа.
        
        Args:
            type_to_find: Класс, объекты которого нужно найти.
            
        Returns:
            Новый объект TypedCollection с отфильтрованными элементами.
        """
        new_collection = TypedCollection(self._item_type)
        for item in self._items:
            if isinstance(item, type_to_find):
                new_collection.add(item)
        return new_collection

    def filter_by_interface(self, interface_type: Type[Any]) -> 'TypedCollection[T]':
        """
        Возвращает новую коллекцию с объектами, реализующими заданный интерфейс.
        
        Args:
            interface_type: Тип интерфейса (например, Pricable или Printable).
            
        Returns:
            Новый объект TypedCollection с отфильтрованными элементами.
        """
        new_collection = TypedCollection(self._item_type)
        for item in self._items:
            if isinstance(item, interface_type):
                new_collection.add(item)
        return new_collection

    # --- МЕТОДЫ СОРТИРОВКИ (ИЗ ЛР-5) ---

    def sort_by(self, key_func: Callable[[T], Any]) -> 'TypedCollection[T]':
        """
        Сортирует коллекцию по ключу и возвращает СЕБЯ для цепочек вызовов.
        
        Args:
            key_func: Функция, принимающая элемент и возвращающая значение для сортировки.
            
        Returns:
            self: Текущий объект для поддержки цепочек (method chaining).
        """
        self._items.sort(key=key_func)
        return self

    def sort_by_comparable(self) -> 'TypedCollection[T]':
        """
        Сортирует коллекцию по имени объекта (универсальный вариант).
        Возвращает СЕБЯ для цепочек вызовов.
        
        Returns:
            self: Текущий объект.
        """
        # Используем универсальный подход: сортируем по атрибуту 'name', если он есть
        try:
            self._items.sort(key=lambda x: getattr(x, 'name', ''))
        except AttributeError:
            # Если у объектов нет атрибута 'name', просто сортируем как есть
            pass
            
        return self

    # --- МЕТОДЫ ДЛЯ ПРИМЕНЕНИЯ ФУНКЦИЙ (ИЗ ЛР-5/6) ---

    def apply(self, func: Callable[[T], Any]) -> List[Any]:
        """
        Применяет произвольную функцию ко всем элементам коллекции.
        
        Args:
            func: Функция для применения к каждому элементу.
            
        Returns:
            Список результатов применения функции.
        """
        return [func(item) for item in self._items]

    # --- СПЕЦИАЛЬНЫЕ МЕТОДЫ (ИЗ ЛР-2) ---

    def __len__(self) -> int:
        """Позволяет использовать функцию len(collection)."""
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        """Позволяет использовать коллекцию в циклах for."""
        return iter(self._items)









############################# Рабочий вариант с базовыми методами
'''
from typing import TypeVar, Generic, List, Iterator, Type

# T - это переменная типа. Она обозначает "любой тип".
T = TypeVar('T')

class TypedCollection(Generic[T]):
    """
    Типизированная коллекция, которая хранит объекты только заданного типа T.
    Повторяет интерфейс коллекции из ЛР-2, но с проверкой типов.
    """

    def __init__(self, item_type: Type[T] = None) -> None:
        """
        Инициализация коллекции.
        
        Args:
            item_type: Тип объектов, которые будут храниться в коллекции.
                      Если None, проверка типов при добавлении не выполняется.
        """
        self._items: List[T] = []
        self._item_type = item_type

    def add(self, item: T) -> None:
        """
        Добавляет объект в коллекцию с проверкой типа.
        
        Args:
            item: Объект для добавления.
            
        Raises:
            TypeError: Если тип объекта не совпадает с ожидаемым типом коллекции.
        """
        # Если тип коллекции задан и тип добавляемого объекта не совпадает
        if self._item_type is not None and not isinstance(item, self._item_type):
            raise TypeError(
                f"Невозможно добавить объект типа {type(item).__name__}. "
                f"Ожидается тип {self._item_type.__name__}."
            )
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает список всех объектов в коллекции."""
        return list(self._items)

    # --- Методы из ЛР-2 (с аннотациями типов) ---

    def __len__(self) -> int:
        """Позволяет использовать функцию len(collection)."""
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        """Позволяет использовать коллекцию в циклах for."""
        return iter(self._items)
'''



################### Запасной вариант
'''
from typing import TypeVar, Generic, List

# 1. Определяем переменную-тип (TypeVar)
# Это говорит Python, что T — это какой-то тип, который мы укажем позже.
T = TypeVar('T')

class TypedCollection(Generic[T]):
    """
    Типизированная коллекция, которая хранит элементы только одного типа T.
    Повторяет интерфейс коллекции из ЛР-2, но с проверкой типов.
    """

    def __init__(self) -> None:
        """
        Инициализирует пустую коллекцию.
        Атрибут _items аннотирован как список элементов типа T.
        """
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """
        Добавляет элемент в коллекцию.
        :param item: Элемент типа T для добавления.
        """
        self._items.append(item)

    def remove(self, item: T) -> None:
        """
        Удаляет элемент из коллекции.
        :param item: Элемент типа T для удаления.
        :raises ValueError: Если элемента нет в коллекции.
        """
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """
        Возвращает копию списка всех элементов коллекции.
        :return: Новый список (List) элементов типа T.
        """
        return list(self._items)
'''