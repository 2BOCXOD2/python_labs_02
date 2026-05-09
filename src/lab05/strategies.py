from src.lab01.models import Transport
from src.lab03.models import CargoShip, Airplane # Для фильтрации по типу

# ЗАДАНИЕ 1 ---------------------------------------------

# --- СТРАТЕГИИ СОРТИРОВКИ ---

def by_name_asc(item):
    """Стратегия: Сортировка по имени (по возрастанию)."""
    return item.name 

def by_price_desc(item):
    """Стратегия: Сортировка по цене (по убыванию)."""
    # Знак минус, чтобы перевернуть порядок сортировки
    return -item.calculate_price()

def by_speed_and_name(item):
    """Стратегия: Сортировка по нескольким атрибутам.
    Сначала по скорости (от большей к меньшей), потом по имени."""
    # Кортеж (-скорость, имя) позволяет сортировать по нескольким ключам
    return (-item.sr_skorost, item.name)

''' lab01
# --- СТРАТЕГИИ ФИЛЬТРАЦИИ ---

def is_expensive(threshold):
    """
    Стратегия-фильтр: Создает функцию для проверки, является ли объект дорогим.
    Это пример замыкания (closure).
    """
    def check(item):
        return item.calculate_price() > threshold
    return check

def is_ship(item):
    """Стратегия-фильтр: Проверяет, является ли объект кораблем."""
    return isinstance(item, CargoShip)
'''

# --- СТРАТЕГИИ ФИЛЬТРАЦИИ (PREDICATES) --- lab03

def is_expensive(item, threshold=5_000_000):
    """
    Функция-стратегия для фильтрации.
    Возвращает True, если цена объекта превышает заданный порог.

    Args:
        item: Объект коллекции.
        threshold: Пороговое значение цены.

    Returns:
        bool: True, если объект дорогой.
    """
    return item.calculate_price() > threshold

def is_ship(item):
    """
    Функция-стратегия для фильтрации по типу.
    Возвращает True, если объект является экземпляром CargoShip.

    Args:
        item: Объект коллекции.

    Returns:
        bool: True, если это корабль.
    """
    return isinstance(item, CargoShip)

# ЗАДАНИЕ 2 ---------------------------------------------------------

# В этом файле мы храним "фабрики" функций.
# Сами стратегии (сортировки) теперь будут простыми lambda в demo.py.

def make_price_filter(max_price):
    """
    Фабрика функций. Создает и возвращает функцию-фильтр.
    Созданный фильтр будет пропускать только объекты с ценой <= max_price.
    """
    def filter_fn(item):
        # Предполагаем, что у объекта есть метод calculate_price()
        return item.calculate_price() <= max_price
    return filter_fn

def apply_discount(discount_rate):
    """
    Фабрика функций для трансформации.
    Создает функцию, которая применяет скидку к цене объекта.
    """
    def apply_to_item(item):
        discounted_price = item.calculate_price() * (1 - discount_rate)
        return discounted_price
    return apply_to_item


# ЗАДАНИЕ 3 ---------------------------------------------------------

# --- СТРАТЕГИИ ОБРАБОТКИ (CALLABLE OBJECTS) ---

class DiscountStrategy:
    """
    Паттерн 'Стратегия' через callable-объект.
    Применяет фиксированную скидку к цене объекта.
    """
    def __init__(self, discount_rate=0.1):
        """
        Инициализация стратегии.

        Args:
            discount_rate: Размер скидки (например, 0.1 для 10%).
        """
        self.discount_rate = discount_rate

    def __call__(self, item):
        """
        Применяет стратегию к объекту.

        Args:
            item: Объект, к которому применяется стратегия.

        Returns:
            float: Новая цена со скидкой.
        """
        return item.calculate_price() * (1 - self.discount_rate)

class UpgradeStrategy:
    """
    Паттерн 'Стратегия' через callable-объект.
    Применяет действие 'upgrade' к объекту и возвращает его описание.
    """
    def __call__(self, item):
        """
        Применяет стратегию к объекту.

        Args:
            item: Объект, к которому применяется стратегия.

        Returns:
            str: Строка с результатом действия.
        """
        # Проверяем, есть ли у объекта метод upgrade, чтобы избежать ошибок
        if hasattr(item, 'upgrade'):
            item.upgrade()
            return f"Объект {item.name} обновлен. Новый уровень сервиса: {getattr(item, 'service_level', 'N/A')}"
        else:
            return f"У объекта {item.name} нет метода обновления."

# --- СТРАТЕГИИ СОРТИРОВКИ (KEY FUNCTIONS) ---
# Эти функции мы будем передавать в sort_by

def by_name_asc(item):
    """Стратегия сортировки по имени (по возрастанию)."""
    return item.name

def by_price_desc(item):
    """Стратегия сортировки по цене (по убыванию)."""
    return -item.calculate_price()