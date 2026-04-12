# Импортируем новую универсальную коллекцию из ЛР-2
# и наши новые модели из ЛР-3
from src.lab02.collection import Fleet
from src.lab03.models import CargoShip, Airplane

def main():
    
    print("=== ДЕМОНСТРАЦИЯ ИЕРАРХИИ ТРАНСПОРТА ===\n")
    
    # Создаем объекты дочерних классов
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
    
    # --- Демонстрация наследования ---
    print("1. Использование методов базового класса:")
    print(ship.opisanie()) # Метод из базового класса Transport
    print(plane.opisanie()) # Метод из базового класса Transport

    # --- Демонстрация новых атрибутов и методов ---
    print("\n2. Использование новых методов дочерних классов:")
    
    # Для корабля
    duration = ship.calculate_flight_duration()
    print(f"   - {ship.name}: Рейс займет {duration} суток.")
    
    # Для самолета (предположим, бак на 180 000 литров)
    range_km = plane.calculate_flight_range(180_000)
    print(f"   - {plane.name}: Дальность полета составит ~{range_km} км.")
    
    # --- Демонстрация работы конструктора через super() ---
    print("\n3. Проверка методов из базового конструктора:")
    print(f"   - Средняя скорость корабля: {ship.sr_skorost} узлов")
    print(f"   - Вместимость самолета: {plane.vmestimost} человек")


    print("=== ДЕМОНСТРАЦИЯ ПОЛИМОФИЗМА И ИНТЕГРАЦИИ ===\n")
    
    # 1. Создаем коллекцию
    mixed_fleet = Fleet()
    
    # 2. Создаем объекты РАЗНЫХ типов
    from src.lab01.models import Car # Добавим и машину для полноты картины
    
    car1 = Car("Lada", 5, 120.5, "Vesta")
    
    ship1 = CargoShip(
        name="Контейнеровоз Надежда",
        vmestimost=20,
        sr_skorost=40.0,
        cargo_capacity_tons=15000,
        route_length_nm=4800
    )
    
    plane1 = Airplane(
        name="Боинг-747",
        vmestimost=420,
        sr_skorost=900.0,
        max_flight_altitude_m=13000,
        fuel_consumption_lph=12000
    )
    
    # 3. Интеграция: Добавляем разные типы объектов в одну коллекцию
    print("4. Добавляем объекты разных типов в коллекцию:")
    mixed_fleet.add(car1)
    mixed_fleet.add(ship1)
    mixed_fleet.add(plane1)
    
    print(f"   Успешно! В коллекции теперь {len(mixed_fleet)} объектов.\n")
    
    # 4. Демонстрация работы с коллекцией разных типов (вывод через __str__)
    print("5. Вывод объектов из коллекции (используется переопределенный __str__):")
    for transport in mixed_fleet:
         print(f"   - {transport}")
    
    # 5. Демонстрация полиморфизма: вызов одного метода - разное поведение
    print("\n6. Демонстрация полиморфного поведения (вызов calculate_price()):")
    
    total_cost = mixed_fleet.calculate_total_price()
    
    print(f"\n   Итого по всем объектам в коллекции: {total_cost} руб.")


    print("=== СЦЕНАРИЙ 1: ПОЛИМОРФИЗМ И ЕДИНЫЙ ИНТЕРФЕЙС ===\n")
    
    mixed_fleet = Fleet()
    
    from src.lab01.models import Car # Импортируем Car здесь для создания объектов

    car1 = Car("Lada", 5, 120.5, "Vesta")
    ship1 = CargoShip("Надежда", 20, 40.0, 15000, 4800)
    plane1 = Airplane("Боинг", 420, 900.0, 13000, 12000)
    
    mixed_fleet.add(car1)
    mixed_fleet.add(ship1)
    mixed_fleet.add(plane1)
    
    print("Вызов единого метода process() для всех объектов:")
    print("-" * 50)
    for transport in mixed_fleet:
         # Это и есть полиморфизм без условий!
         # Мы вызываем один и тот же метод .process(),
         # но каждый объект выполняет свою реализацию.
         print(transport.process())
    
    print("\n=== СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ ПО ТИПУ ===\n")
    
    # Используем метод фильтрации из коллекции
    car_fleet = mixed_fleet.get_only_cars()
    
    print("В коллекции остались только автомобили:")
    for car in car_fleet:
         print(f"   - {car.name} ({car.model})")
         
    print(f"\nПроверка через isinstance(): {isinstance(car_fleet.get_all()[0], Car)}")
    
    print("\n=== СЦЕНАРИЙ 3: КОМБИНИРОВАННЫЙ СЦЕНАРИЙ ===\n")
    
    # Создадим новую большую коллекцию для наглядности
    big_fleet = Fleet()
    big_fleet.add(Car("BMW", 4, 250, "X5"))
    big_fleet.add(Car("Mercedes", 5, 220, "S-Class"))
    big_fleet.add(CargoShip("Evergreen", 10, 35.0, 220000, 1200))
    
    print("Исходная большая коллекция:")
    for t in big_fleet:
         print(f"   - {t.name}")
    
    # Отфильтруем только машины и вызовем у них специфический метод (например, drive)
    cars_only = big_fleet.get_only_cars()
    
    print("\nВызов специфического метода у отфильтрованных объектов:")
    for car in cars_only.get_all():
         # Теперь мы точно знаем, что это Car, и можем вызвать drive()
         car.activate() # Активируем машину перед поездкой
         car.drive(50)   # Вызываем метод из ЛР-1
    
if __name__ == "__main__":
    main()


# python -m src.lab03.demo    Запуск через терминал



######### На 4
'''
# Импортируем коллекцию из ЛР-1 и наши новые модели из ЛР-3
from src.lab02.collection import Fleet
from src.lab03.models import CargoShip, Airplane

def main():
    print("=== ДЕМОНСТРАЦИЯ ПОЛИМОФИЗМА И ИНТЕГРАЦИИ ===\n")
    
    # 1. Создаем коллекцию (наш универсальный флот из ЛР-1)
    mixed_fleet = Fleet()
    
    # 2. Создаем объекты разных типов (Корабль и Самолет из ЛР-3)
    ship1 = CargoShip(
        name="Контейнеровоз Надежда",
        vmestimost=20,
        sr_skorost=40.0,
        cargo_capacity_tons=15000,
        route_length_nm=4800
    )
    
    plane1 = Airplane(
        name="Боинг-747",
        vmestimost=420,
        sr_skorost=900.0,
        max_flight_altitude_m=13000,
        fuel_consumption_lph=12000
    )
    
    # 3. Интеграция: Добавляем разные типы объектов в одну коллекцию
    print("1. Добавляем объекты в коллекцию:")
    mixed_fleet.add(ship1)
    mixed_fleet.add(plane1)
    
    # 4. Демонстрация работы с коллекцией разных типов
    print("\n2. Вывод объектов из коллекции:")
    for transport in mixed_fleet:
         # Благодаря переопределенному __str__(), каждый объект выводит себя по-своему
         print(f"   - {transport}")
    
    # 5. Демонстрация полиморфизма и проверки типов через isinstance()
    print("\n3. Демонстрация полиморфного поведения (расчет цены):")
    
    total_cost = 0
    for transport in mixed_fleet:
        # Полиморфизм: вызываем один метод, а выполняется разный код
        price = transport.calculate_price()
        
        # Проверка типа для кастомного вывода
        if isinstance(transport, CargoShip):
            print(f"{transport.name}: Цена фрахта {price} у.е.")
            total_cost += price
        elif isinstance(transport, Airplane):
            print(f"{transport.name}: Цена аренды {price} у.е.")
            total_cost += price
            
    print(f"\n   Общая стоимость операций флота: {total_cost} у.е.")
    
if __name__ == "__main__":
    main()
'''
###################### На 3

"""
from .models import CargoShip, Airplane

def main():

    
    print("=== ДЕМОНСТРАЦИЯ ИЕРАРХИИ ТРАНСПОРТА ===\n")
    
    # Создаем объекты дочерних классов
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
    
    # --- Демонстрация наследования ---
    print("1. Использование методов базового класса:")
    print(ship.opisanie()) # Метод из базового класса Transport
    print(plane.opisanie()) # Метод из базового класса Transport

    # --- Демонстрация новых атрибутов и методов ---
    print("\n2. Использование новых методов дочерних классов:")
    
    # Для корабля
    duration = ship.calculate_flight_duration()
    print(f"   - {ship.name}: Рейс займет {duration} суток.")
    
    # Для самолета (предположим, бак на 180 000 литров)
    range_km = plane.calculate_flight_range(180_000)
    print(f"   - {plane.name}: Дальность полета составит ~{range_km} км.")
    
    # --- Демонстрация работы конструктора через super() ---
    print("\n3. Проверка атрибутов из базового конструктора:")
    print(f"   - Средняя скорость корабля: {ship.sr_skorost} узлов")
    print(f"   - Вместимость самолета: {plane.vmestimost} человек")
    
if __name__ == "__main__":
    main()
"""


