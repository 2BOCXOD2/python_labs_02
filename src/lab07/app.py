from typing import List
from src.lab07.models import Transport, Car, CargoShip, Airplane
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError
from src.lab07.storage import save, load
import os


class TransportApp:
    
    """
    Слой бизнес-логики приложения.
    Управляет коллекцией и реализует операции предметной области.
    """
    # Определяем путь к файлу как атрибут класса
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Путь к папке lab07
    FILEPATH = os.path.join(BASE_DIR, "data", "transports.json")

    def __init__(self):
        """Инициализирует приложение и автоматически загружает данные."""
        self.collection = []
        
        # --- НОВОЕ: Автозагрузка при запуске ---
        try:
            loaded_items = load(self.FILEPATH)
            for item in loaded_items:
                # Используем наш метод add_item, чтобы сработала проверка на дубликаты
                self.add_item(item)
        except Exception as e:
            print(f"   ⚠️  Ошибка при автозагрузке данных: {e}. Запуск с пустой коллекцией.")
        
    def exit_app(self) -> None:
        """
        Выполняет действия перед выходом из приложения (сохранение данных).
        """
        try:
            save(self.collection, self.FILEPATH) # Передаем коллекцию (self) и путь к файлу
            print("   🔚 До свидания! Данные сохранены.")
            # Импорт sys здесь, чтобы не загружать его без необходимости
            import sys
            sys.exit(0)
        except Exception as e:
            print(f"   ❌ Ошибка при сохранении: {e}")
            import sys
            sys.exit(1)
    
    
    """
    Слой бизнес-логики.
    Управляет коллекцией и реализует операции предметной области.
    """
    def __init__(self):
        """Инициализирует пустую коллекцию."""
        self.collection: List[Transport] = []

        # --- НОВАЯ СТРОКА ДЛЯ ОТЛАДКИ ---
        # Эта строка покажет нам АБСОЛЮТНЫЙ путь, по которому программа ищет файл.
        print(f"🔍 ПОПЫТКА ЗАГРУЗКИ. Ищу файл по пути: {os.path.abspath(self.FILEPATH)}") 

        # --- НОВОЕ: Автозагрузка при запуске ---
        try:
            loaded_items = load(self.FILEPATH)
            print(f"✅ УСПЕХ: Загружено {len(loaded_items)} объектов.") # Добавим это, чтобы видеть результат
            for item in loaded_items:
                self.add_item(item)
        except Exception as e:
            print(f"   ⚠️  Ошибка при автозагрузке данных: {e}. Запуск с пустой коллекцией.")


    # --- МЕТОДЫ ДЛЯ ДОБАВЛЕНИЯ И УДАЛЕНИЯ ---
    
    def add_item(self, item: Transport) -> str:
        """
        Добавляет объект в коллекцию с проверкой на дубликаты.
        Сначала проверяет по названию (бизнес-правило), затем по ID (техническое).

        Args:
            item: Объект для добавления.

        Raises:
            DuplicateItemError: Если объект с таким названием или ID уже существует.

        Returns:
            Строка с подтверждением.
        """
        # --- НОВАЯ ПРОВЕРКА: По названию (бизнес-логика) ---
        for existing in self.collection:
            if existing.name == item.name:
                # Вызываем наше исключение, если имя уже занято
                raise DuplicateItemError(f"Объект с названием '{item.name}' уже существует.")
        
        """
        # --- СТАРАЯ ПРОВЕРКА: По ID (техническая) ---
        for existing in self.collection:
            if existing.id == item.id:
                raise DuplicateItemError(f"Объект с ID {item.id} уже существует.")
        """

        # Если проверок не было — добавляем объект
        self.collection.append(item)
        return f"✅ {item.name} добавлен."
    

    def remove_item_by_name(self, name_to_remove: str) -> str:
        """
        Удаляет объект по названию с проверкой существования.
        
        Args:
            name_to_remove: Название объекта для удаления.
            
        Raises:
            ItemNotFoundError: Если объект не найден.
            
        Returns:
            Строка с подтверждением.
        """
        for item in self.collection:
            if item.name == name_to_remove:
                self.collection.remove(item)
                return f"✅ Объект '{name_to_remove}' удален."
        
        raise ItemNotFoundError(f"Объект с названием '{name_to_remove}' не найден.")

    # --- МЕТОДЫ ДЛЯ ПОИСКА И ФИЛЬТРАЦИИ ---
    
    def get_all_items(self) -> List[Transport]:
        """Возвращает список всех объектов."""
        return self.collection

    def search_by_name(self, name_part: str) -> List[Transport]:
        """
        Поиск по части названия (поиск по атрибуту).
        
        Args:
            name_part: Часть названия для поиска.
            
        Returns:
            Список найденных объектов.
        """
        results = []
        for item in self.collection:
            if name_part.lower() in item.name.lower():
                results.append(item)
        
        if not results:
            raise ItemNotFoundError(f"Ничего не найдено по запросу '{name_part}'.")
            
        return results

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Transport]:
        """
        Фильтрация по диапазону цен.
        
        Args:
            min_price: Минимальная цена.
            max_price: Максимальная цена.
            
        Returns:
            Список отфильтрованных объектов.
            
        Raises:
            ItemNotFoundError: Если ничего не найдено.
        """
        results = []
        for item in self.collection:
            # Проверяем, есть ли у объекта метод/атрибут calculate_price и цена > 0
            price = item.calculate_price()
            if price > 0 and min_price <= price <= max_price:
                results.append(item)
        
        if not results:
            raise ItemNotFoundError(f"Ничего не найдено в ценовом диапазоне {min_price} - {max_price}.")
            
        return results
    

    def sort_items(self, strategy: str) -> str:
        """
        Сортирует коллекцию по выбранной стратегии.

        Args:
            strategy: Название стратегии. Может быть 'name', 'price' или 'date'.

        Returns:
            Строка-подтверждение.

        Raises:
            ValueError: Если выбрана неверная стратегия.
        """
        if strategy == 'name':
            # Стратегия 1: Сортировка по названию
            self.collection.sort(key=lambda x: x.name)
        
        elif strategy == 'price':
            # Стратегия 2: Сортировка по цене (по убыванию)
            # Фильтруем только объекты, у которых есть цена > 0
            priced_items = [i for i in self.collection if i.calculate_price() > 0]
            priced_items.sort(key=lambda x: x.calculate_price(), reverse=True)
            
            # Обновляем основную коллекцию, сохраняя порядок безценных объектов
            # (это более сложная логика, для простоты просто сортируем всё)
            self.collection.sort(key=lambda x: x.calculate_price(), reverse=True)
        
        elif strategy == 'date':
            # Стратегия 3: Сортировка по дате добавления (от новых к старым)
            # Проверяем, есть ли у объекта атрибут даты
            self.collection.sort(key=lambda x: getattr(x, 'date_added', ''), reverse=True)
        
        else:
            raise ValueError("Неверная стратегия сортировки.")
            
        return f"Коллекция отсортирована по {strategy}."



'''
from src.lab06.container import TypedCollection
from src.lab01.models import Car, Transport
from src.lab03.models import CargoShip, Airplane
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError

import os
import sys
from typing import List, Dict, Any, Optional
from src.lab07.storage import save, load
from datetime import datetime


class TransportApp:
    """
    Бизнес-логика приложения.
    Управляет коллекцией транспортных средств.
    """
    # СТРОИМ ПУТЬ ОТНОСИТЕЛЬНО ЭТОГО ФАЙЛА (app.py)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Путь к папке lab07
    FILEPATH = os.path.join(BASE_DIR, "data", "new_transports.json")

    def __init__(self):
        """Инициализирует приложение и загружает данные из файла."""
        self.collection = TypedCollection[Transport](Transport)
        
        # 1. АВТОЗАГРУЗКА ДАННЫХ ПРИ СТАРТЕ
        try:
            loaded_items = load(self.FILEPATH)
            for item in loaded_items:
                self.collection.add(item)
            print("   🟢 Приложение запущено. Данные загружены.")
        except Exception as e:
            print(f"   ⚠️  Ошибка при загрузке данных: {e}. Запуск с пустой коллекцией.")
        
        # self.fill_test_data() # Тестовые данные теперь не нужны, так как есть автозагрузка

    def exit_app(self) -> None:
        """
        Выполняет действия перед выходом из приложения (сохранение данных).
        """
        try:
            save(self.collection, self.FILEPATH)
            print("   🔚 До свидания! Данные сохранены.")
            sys.exit(0)
        except Exception as e:
            print(f"   ❌ Ошибка при сохранении: {e}")
            sys.exit(1)
    
    
    """
    def __init__(self):
        # Используем типизированную коллекцию из ЛР6
        self.collection = TypedCollection[Transport](Transport)
        self.fill_test_data() # Добавим тестовые данные для удобства

    def fill_test_data(self):
        """Добавляет несколько объектов для демонстрации."""
        self.collection.add(Car("Lada Vesta", 5, 150, "Vesta", price=1_500_000))
        self.collection.add(Car("BMW X5", 5, 220, "X5", price=9_000_000))
        self.collection.add(CargoShip("Надежда", 20, 40, 15000, 4800))
        print("Тестовые данные добавлены.")
    """
    """
    def add_item(self):
        """Логика добавления нового транспорта."""
        print("\n--- ДОБАВИТЬ ТРАНСПОРТ ---")
        print("1. Автомобиль")
        print("2. Грузовой корабль")
        print("3. Самолет")
        
        try:
            choice = int(input("Выберите тип (1-3): "))
            name = input("Введите название: ")
            
            if choice == 1:
                vmestimost = int(input("Вместимость: "))
                sr_skorost = float(input("Средняя скорость: "))
                model = input("Модель: ")
                self.collection.add(Car(name, vmestimost, sr_skorost, model))
                print(f"Автомобиль '{name}' добавлен.")
            elif choice == 2:
                vmestimost = int(input("Вместимость: "))
                sr_skorost = float(input("Средняя скорость: "))
                cargo_tons = int(input("Грузоподъемность (тонн): "))
                route_nm = int(input("Длина маршрута (м. миль): "))
                self.collection.add(CargoShip(name, vmestimost, sr_skorost, cargo_tons, route_nm))
                print(f"Корабль '{name}' добавлен.")
            elif choice == 3:
                vmestimost = int(input("Вместимость: "))
                sr_skorost = float(input("Средняя скорость: "))
                altitude = int(input("Макс. высота (м): "))
                fuel_cons = int(input("Расход топлива (л/ч): "))
                self.collection.add(Airplane(name, vmestimost, sr_skorost, altitude, fuel_cons))
                print(f"Самолет '{name}' добавлен.")
            else:
                print("Неверный выбор типа.")
        except ValueError:
            print("Ошибка: вводите только числа там, где это требуется.")
    """

    def add_item(self, item_type_code: int, data: dict) -> str:
        """
        Бизнес-логика добавления с проверкой на дубликаты.
        """
        try:
            # 1. Создаем новый объект (как и раньше)
            if item_type_code == 1:
                new_item = Car(**data)
            elif item_type_code == 2:
                new_item = CargoShip(**data)
            elif item_type_code == 3:
                new_item = Airplane(**data)
            else:
                return "Неверный тип объекта."
            
            setattr(new_item, 'date_added', datetime.now().isoformat())

            # 2. НОВАЯ ЛОГИКА: Проверка на дубликаты в коллекции
            for existing in self.collection.get_all():
                # --- СТРОГАЯ ПРОВЕРКА (Техническая) ---
                # Если это буквально тот же объект в памяти (маловероятно, но для чистоты)
                # или если у них есть id и они совпадают.
                if hasattr(existing, 'id') and hasattr(new_item, 'id') and existing.id == new_item.id:
                    raise DuplicateItemError(f"Объект с ID {new_item.id} уже существует.")
            
                # --- БИЗНЕС-ПРОВЕРКА (По имени) ---
                # Проверяем, нет ли в коллекции объекта с ТАКИМ ЖЕ ИМЕНЕМ.
                # Это главное правило для нашей предметной области.
                if existing.name == new_item.name:
                    # Дополнительная проверка: если это машины, проверим и модель.
                    # Это делает проверку еще строже.
                    if isinstance(new_item, Car) and isinstance(existing, Car):
                        if existing.model == new_item.model:
                            raise DuplicateItemError(f"Автомобиль с названием '{new_item.name}' и моделью '{new_item.model}' уже существует.")
                    else:
                        # Для других типов (корабли, самолеты) достаточно совпадения имени.
                        raise DuplicateItemError(f"Объект с названием '{new_item.name}' уже существует.")
        
            # 3. Если проверки пройдены, добавляем объект
            self.collection.add(new_item)
            return f"{new_item.name} добавлен."
        
        except DuplicateItemError as e:
            return f"ОШИБКА: {e}"
        except Exception as e:
            return f"Ошибка при создании объекта: {e}"
    


    def show_all(self):
        """Выводит все объекты в коллекции."""
        print("\n--- ВСЕ ОБЪЕКТЫ В КОЛЛЕКЦИИ ---")
        items = self.collection.get_all()
        if not items:
            print("Коллекция пуста.")
            return

        for i, item in enumerate(items, 1):
            # Используем полиморфизм: у каждого объекта свой __str__
            print(f"{i}. {item}")

    def find_item(self):
        """Ищет объект по названию."""
        name = input("\nВведите название для поиска: ")
        # Используем метод find из ЛР6 и лямбда-функцию как стратегию
        found_item = self.collection.find(lambda x: name.lower() in x.name.lower())
        
        if found_item:
            print(f"НАЙДЕНО: {found_item}")
        else:
            print(f"Объект с названием '{name}' не найден.")

    def remove_item(self, name):
        """Удаляет объект по названию."""
        # name = input("\nВведите название для удаления: ")
        
        # Используем метод find, чтобы проверить наличие
        item_to_remove = self.collection.find(lambda x: x.name == name)
        
        if item_to_remove:
            self.collection.remove(item_to_remove)
            print(f"Объект '{name}' удален.")
        else:
            print(f"Объект с названием '{name}' не найден.")


    
    # --- НОВЫЕ МЕТОДЫ ДЛЯ ПОИСКА И ФИЛЬТРАЦИИ ---
    
    def search_by_name(self, name_part: str) -> list:
        """
        Поиск по части названия (поиск по атрибуту).
        """
        results = self.collection.filter(lambda x: name_part.lower() in x.name.lower())
        return results

    def filter_by_price_range(self, min_price: float, max_price: float) -> list:
        """
        Фильтрация по диапазону цен.
        """
        results = self.collection.filter(
            lambda x: hasattr(x, 'price') and min_price <= x.price <= max_price
        )
        return results

    def filter_by_status(self, status_active: bool) -> list:
        """
        Фильтрация по статусу (активен/неактивен).
        """
        results = self.collection.filter(lambda x: x.active == status_active)
        return results
    

    # --- УЛУЧШЕННЫЙ ВЫВОД ---
    
    
    def print_table(self, items: list) -> None:
        """
        Выводит список объектов в виде форматированной таблицы.
        """
        if not items:
            print("   Коллекция пуста.")
            return

        print("\n" + "="*60)
        for item in items:
            # Используем полиморфизм: у каждого объекта свой __str__
            print(f"   | {str(item):<50} |")
            print("-" * 60)



    # --- НОВЫЕ МЕТОДЫ ДЛЯ СОРТИРОВКИ (из ЛР5) ---
    
    def sort_by_name(self) -> None:
        """Сортирует коллекцию по названию (по возрастанию)."""
        self.collection.sort_by(lambda x: x.name)
    
    def sort_by_price(self) -> None:
        """Сортирует коллекцию по цене (по убыванию)."""
        self.collection.sort_by(lambda x: -x.calculate_price())
    
    def sort_by_date(self) -> None:
        """Сортирует коллекцию по дате добавления (от новых к старым)."""
        self.collection.sort_by(lambda x: x.date_added)

    # --- МЕТОД ПОДТВЕРЖДЕНИЯ УДАЛЕНИЯ ---
    
    def confirm_and_remove(self, name_to_remove: str) -> str:
        """
        Запрашивает подтверждение перед удалением объекта.
        
        Args:
            name_to_remove: Название объекта для удаления.
            
        Returns:
            Строка с результатом операции.
        """
        item_to_remove = self.collection.find(lambda x: x.name == name_to_remove)
        
        if not item_to_remove:
            return f"   ❌ Объект '{name_to_remove}' не найден."
            
        confirm = input(f"Удалить '{name_to_remove}'? (y/n): ").lower()
        if confirm == 'y':
            self.collection.remove(item_to_remove)
            return f"   ✅ Объект '{name_to_remove}' удален."
        else:
            return f"   ❌ Удаление '{name_to_remove}' отменено."
    
'''