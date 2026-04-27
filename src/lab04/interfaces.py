
from abc import ABC, abstractmethod

class Pricable(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        pass

class Describable(ABC):
    @abstractmethod
    def get_short_description(self) -> str:
        pass

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

# --- НОВЫЙ ИНТЕРФЕЙС: Comparable ---
class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
         *  0, если объекты равны.
         * -1, если текущий объект "меньше".
         *  1, если текущий объект "больше".
        """
        pass

'''
from abc import ABC, abstractmethod

# Интерфейс 1: Контракт на расчет цены
class Pricable(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        """
        Абстрактный метод для расчета стоимости.
        Каждый класс, реализующий этот интерфейс,
        обязан предоставить свою реализацию.
        """
        pass


# Интерфейс 2: Контракт на описание
class Describable(ABC):
    @abstractmethod
    def get_short_description(self) -> str:
        """
        Абстрактный метод для получения краткого описания.
        """
        pass


# --- Новый Интерфейс 3: Контракт на печать ---
class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть полное строковое представление объекта."""
        pass


# НОВЫЙ ИНТЕРФЕЙС для сортировки объектов
class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
         *  0, если объекты равны.
         * -1, если текущий объект "меньше".
         *  1, если текущий объект "больше".
        """
        pass

'''