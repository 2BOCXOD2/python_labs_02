from src.lab02.collection import Fleet
from src.lab04.models import CargoShip, Airplane
from src.lab04.interfaces import Pricable, Printable, Comparable, Describable
from src.lab01.models import Car

def main():
    print("=== ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСОВ (КОНТРАКТОВ) ===\n")
    
    # Создаем объекты разных типов
    ship = CargoShip(
        name="Контейнеровоз Надежда",
        vmestimost=20,
        sr_skorost=40.0,
        cargo_capacity_tons=15000,
        route_length_nm=4800
    )
    
    plane = Airplane(
        name="Боинг-747",
        vmestimost=420,
        sr_skorost=900.0,
        max_flight_altitude_m=13000,
        fuel_consumption_lph=12000
    )
    
    # --- Демонстрация полиморфизма через интерфейсы ---
    
    # У нас есть список "Оцениваемых" объектов (Pricable)
    print("1. Демонстрация интерфейса Pricable (расчет цены):")
    print("-" * 50)
    
    items_to_price = [ship, plane]
    
    for item in items_to_price:
        # Мы вызываем один и тот же метод у разных объектов!
        # Но поведение (результат) будет разным.
        price = item.calculate_price()
        
        # Проверяем тип для красивого вывода, но логика расчета уже сработала полиморфно
        if hasattr(item, 'cargo_capacity_tons'): # hasattr(объект, "имя_атрибута_в_виде_строки")
            print(f"Груз корабля '{item.name}': {price} у.е.") # Возвращает: True, если у объекта есть такой атрибут.
        else:
            print(f"Аренда самолета '{item.name}': {price} у.е.") # Возвращает: False, если атрибута нет.
    
    # --- Демонстрация интерфейса Describable ---
    
    print("\n2. Демонстрация интерфейса Describable (краткое описание):")
    print("-" * 50)
    
    for item in items_to_price:
        # Снова вызываем один и тот же метод!
        description = item.get_short_description()
        
        if hasattr(item, 'cargo_capacity_tons'):
            print(f"Описание груза: {description}")
        else:
            print(f"Описание рейса: {description}")

    
    print("\n=== ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСОВ КАК ТИПОВ И МНОЖЕСТВЕННОЙ РЕАЛИЗАЦИИ ===\n")
    
    ship = CargoShip("Надежда", 20, 40.0, 15000, 4800)
    plane = Airplane("Боинг", 420, 900.0, 13000, 12000)
    
    # --- Сценарий 1: Универсальная функция через интерфейс (как тип) ---
    
    # Функция принимает список объектов, которые реализуют интерфейс Printable
    # Это и есть использование интерфейса как типа.
    def print_all(items: list[Printable]):
        print("--- Вывод информации об объектах через универсальную функцию ---")
        for item in items:
            # Мы не знаем, что это за объект. Но мы ЗНАЕМ, что у него есть метод to_string().
            print(item.to_string())
            print("-" * 30)
    
    # Создаем список из разных объектов
    items_to_print = [ship, plane]
    
    # Вызываем функцию
    print_all(items_to_print)
    
    # --- Сценарий 2: Проверка через isinstance() ---
    
    print("\n--- Проверка принадлежности к интерфейсу через isinstance() ---")
    
    # Проверяем для каждого объекта, реализует ли он интерфейс Pricable
    for obj in items_to_print:
        if isinstance(obj, Pricable):
            print(f"   Объект '{obj.name}' реализует интерфейс Pricable (можно посчитать цену).")
            print(f"   Цена: {obj.calculate_price()} у.е.")
        else:
            print(f"   Объект не реализует интерфейс Pricable.")
    
    # --- Сценарий 3: Множественная реализация интерфейсов ---
    
    print("\n--- Демонстрация множественной реализации интерфейсов ---")
    
    # Мы знаем, что ship - это Transport, который зарегистрирован как Pricable, Describable И Printable.
    print(f"1. isinstance(ship, Printable): {isinstance(ship, Printable)}")
    print(f"2. isinstance(ship, Pricable): {isinstance(ship, Pricable)}")
    print(f"3. isinstance(ship, Describable): {isinstance(ship, Describable)}")


    print("=== СЦЕНАРИЙ 1: ЕДИНЫЙ СПИСОК И РАБОТА ЧЕРЕЗ ИНТЕРФЕЙСЫ ===\n")
    
    mixed_fleet = Fleet()
    
    car1 = Car("Lada Vesta", 5, 150.5, "Vesta", price=1_000_000)
    ship1 = CargoShip("Надежда", 20, 40.0, 15000, 4800)
    plane1 = Airplane("Боинг", 420, 900.0, 13000, 12000)
    
    mixed_fleet.add(car1)
    mixed_fleet.add(ship1)
    mixed_fleet.add(plane1)
    
    # 1. Используем универсальный метод фильтрации по интерфейсу
    # Передаем в него сам класс-интерфейс (Printable)
    printable_items = mixed_fleet.filter_by_interface(Printable)

    print("1. Демонстрация полиморфизма (Вызов единого метода .to_string()):")
    print("-" * 60)

    # 2. Теперь мы можем быть уверены, что у каждого объекта есть метод to_string()
    for item in printable_items:
        print(item.to_string())
        print("-" * 60)
    
    print("\n=== СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ ПО ИНТЕРФЕЙСУ ===\n")
    
    # --- ФИЛЬТРАЦИЯ ---
    # Используем универсальный метод коллекции и передаем ему тип интерфейса
    # Используем тот же универсальный метод, но для другого интерфейса
    pricable_items = mixed_fleet.filter_by_interface(Pricable)

    print("Выводим только те объекты, у которых можно посчитать цену (Pricable):")
    for item in pricable_items:
        print(f"- {item.name}: Стоимость {item.calculate_price()} у.е.")
    
    print("\n=== СЦЕНАРИЙ 3: СОРТИРОВКА ЧЕРЕЗ ИНТЕРФЕЙС Comparable ===\n")


    ship_fleet = Fleet()
    expensive_ship = CargoShip("Гигант", 10, 30.0, 50000, 500)
    cheap_ship = CargoShip("Малыш", 5, 20.0, 1000, 100)

    ship_fleet.add(expensive_ship)
    ship_fleet.add(cheap_ship)

    print("До сортировки:")
    for ship in ship_fleet:
        print(f" - {ship.name}: {ship.calculate_price()}")

    # --- ИСПРАВЛЕННАЯ и ПРОСТАЯ ЛОГИКА ---
    # 1. Получаем список всех объектов из коллекции
    items_to_sort = ship_fleet.get_all()

    # 2. Сортируем этот список по цене (используя метод calculate_price как ключ)
    # Функция sorted() возвращает НОВЫЙ отсортированный список, не меняя старый
    sorted_items = sorted(items_to_sort, key=lambda x: x.calculate_price()) 

    # 3. ЗАМЕНЯЕМ содержимое исходной коллекции на отсортированный список
    ship_fleet._items = sorted_items 

    # Теперь, когда мы вывели коллекцию, она будет использовать новое содержимое (_items)
    print("\nПосле сортировки (от дешевого к дорогому):")
    for ship in ship_fleet:
        print(f" - {ship.name}: {ship.calculate_price()}")

if __name__ == "__main__":
    main()


# python -m src.lab04.demo  Запуск через терминал