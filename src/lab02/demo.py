from .collection import Fleet
from src.lab01.models import Car

def main():
    # --- ДЕМОНСТРАЦИИ (шаги 1-5) ---
    print("=== ДЕМОНСТРАЦИЯ БАЗОВОЙ РАБОТЫ КОЛЛЕКЦИИ ===\n")

    # Создаем коллекцию автопарк
    fleet = Fleet()

    # Создаем несколько автомобилей
    car1 = Car("Lada", 5, 120.5, "Vesta")
    car2 = Car("Toyota", 5, 180.0, "Camry")
    
    print("1. Добавляем автомобили в автопарк:")
    fleet.add(car1)
    fleet.add(car2)
    
    print(f"   Количество автомобилей в автопарке: {len(fleet)}")

    print("\n2. Получаем список всех автомобилей:")
    all_cars = fleet.get_all()
    for car in all_cars:
        print(f"   - {car.name} ({car.model})")

    print("\n3. Итерируемся по автопарку напрямую:")
    for car in fleet:
        print(f"   - {car}")

    print("\n4. Удаляем автомобиль из автопарка:")
    fleet.remove(car1)
    
    print(f"   Количество автомобилей после удаления: {len(fleet)}")
    
    print("\n5. Проверяем содержимое автопарка после удаления:")
    for car in fleet.get_all():
        print(f"   - {car.name}")

    # --- ДЕМОНСТРАЦИИ (поиск, ограничения) ---
   
    print("\n\n=== ДЕМОНСТРАЦИЯ НОВЫХ ВОЗМОЖНОСТЕЙ ===\n")

    # Пересоздадим автопарк для чистоты эксперимента
    fleet = Fleet()
    car1 = Car("Lada", 5, 120.5, "Vesta")
    car2 = Car("Toyota", 5, 180.0, "Camry")

    print("6. Проверка ограничений на добавление (дубликаты):")
    fleet.add(car1)
    fleet.add(car2)
    print(f"   - Успешно добавлены: {car1.name} и {car2.name}")

    try:
        # Создаем новый объект с тем же именем "Lada"
        duplicate_car = Car("Lada", 4, 150, "Granta")
        fleet.add(duplicate_car)
        # Если мы дошли до этой строки, значит ошибка не сработала
        print("   -  Дубликат был добавлен!")
    except ValueError as e:
        # Это ожидаемый результат
        print(f"   - ОШИБКА: Добавление отклонено: {e}")

    try:
        # Создаем копию объекта car1 (у него будет тот же ID)
        # Для простоты просто передадим тот же объект
        print("\n7. Проверка ограничения по ID:")
        fleet.add(car1)
        print("   - ОШИБКА: Объект с тем же ID был добавлен!")
    except ValueError as e:
        print(f"   - Успех! Добавление отклонено: {e}")

    # --- Демонстрация поиска ---
    print("\n8. Демонстрация поиска:")
    
    # Поиск по имени (должен найти)
    found_car = fleet.find_by_name("Toyota")
    if found_car:
        print(f"   - Поиск по имени 'Toyota': Найден -> {found_car.model}")
    
    # Поиск по несуществующему имени (должен вернуть None)
    not_found = fleet.find_by_name("Ferrari")
    if not_found is None:
        print("   - Поиск по имени 'Ferrari': Не найден (вернул None)")
    
    # Поиск по ID (должен найти)
    car_id_to_find = car2.id
    found_by_id = fleet.find_by_id(car_id_to_find)
    if found_by_id:
        print(f"   - Поиск по ID {car_id_to_find}: Найден -> {found_by_id.name}")
    

    # --- СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ И ИНДЕКСАЦИЯ ---
    print("=== СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ И ИНДЕКСАЦИЯ ===\n")
    
    fleet = Fleet()
    
    # --- ИЗМЕНЕНИЕ: Добавляем цену всем автомобилям ---
    car1 = Car("Lada", 5, 120.5, "Vesta", price=800_000)
    car2 = Car("Toyota", 5, 180.0, "Camry", price=2_500_000)
    car3 = Car("Kia", 5, 150.0, "Rio", price=1_500_000)
    
    fleet.add(car1)
    fleet.add(car2)
    fleet.add(car3)
    
    print("Коллекция создана. Проверяем индексацию:")
    print(f"   fleet[0] -> {fleet[0].name}") # Должен вывести Lada
    print(f"   fleet[2] -> {fleet[2].name}") # Должен вывести Kia

    print("\nУдаляем автомобиль по индексу 1 (Toyota):")
    fleet.remove_at(1)
    
    print(f"   Осталось автомобилей: {len(fleet)}")
    print(f"   Теперь fleet[1] -> {fleet[1].name}") # Должен вывести Kia

    # --- СЦЕНАРИЙ 2: СОРТИРОВКА ---
    print("\n\n=== СЦЕНАРИЙ 2: СОРТИРОВКА ===\n")
    
    # Пересоздаем автопарк для чистоты эксперимента
    fleet = Fleet()
    fleet.add(Car("Ford", 5, 170, "Focus", price=1_600_000))
    fleet.add(Car("BMW", 4, 220, "3 Series", price=3_500_000))
    fleet.add(Car("Audi", 5, 210, "A4", price=3_200_000))
    
    print("До сортировки по цене:")
    for car in fleet:
        print(f"   - {car.name}: {car.price}")
        
    fleet.sort_by_price()
    
    print("\nПосле сортировки по цене:")
    for car in fleet:
        print(f"   - {car.name}: {car.price}")
        
    # Универсальная сортировка по имени в обратном порядке
    print("\nУниверсальная сортировка по имени (Z-A):")
    fleet.sort(key=lambda c: c.name) # Метод sort в коде коллекции использует .sort() списка, где reverse=False по умолчанию
    sorted_fleet = Fleet()
    for car in sorted(fleet.get_all(), key=lambda c: c.name, reverse=True):
        sorted_fleet.add(car)
    for car in sorted_fleet:
        print(f"   - {car.name}")

    # --- СЦЕНАРИЙ 3: ФИЛЬТРАЦИЯ ---
    print("\n\n=== СЦЕНАРИЙ 3: ФИЛЬТРАЦИЯ ===\n")
    
    # Пересоздаем автопарк с разными ценами
    fleet = Fleet()
    fleet.add(Car("Lanos", 5, 100, "Cheap", price=300_000))
    fleet.add(Car("Mazda", 5, 180, "6", price=2_200_000))
    fleet.add(Car("Tesla", 5, 200, "Model S", price=12_000_000))
    
    expensive_fleet = fleet.get_expensive(2_000_000) # Создаем новую коллекцию!
    
    print("Исходная коллекция:")
    for car in fleet:
        print(f"   - {car.name} ({car.price})")
        
    print("\nОтфильтрованная коллекция (дорогие авто > 2 млн):")
    for car in expensive_fleet:
        print(f"   - {car.name} ({car.price})")


if __name__ == "__main__":
    main()


# python -m src.lab02.demo      Запуск программы через терминал






"""
from .collection import Fleet
from src.lab01.models import Car # Импорт из первой лабораторной работы

def main():
    # Создаем коллекцию (флот)
    fleet = Fleet()

    # Создаем несколько автомобилей
    car1 = Car("Lada", 5, 120.5, "Vesta")
    car2 = Car("Toyota", 5, 180.0, "Camry")
    
    # --- Демонстрация работы методов ---

    print("1. Добавляем автомобили в автопарк:")
    fleet.add(car1)
    fleet.add(car2)
    
    # Попытка добавить объект неверного типа (например, строку) вызовет ошибку
    # fleet.add("Это не автомобиль") 

    print(f"   Количество автомобилей в автопарке: {len(fleet)}")

    print("\n2. Получаем список всех автомобилей:")
    all_cars = fleet.get_all()
    for car in all_cars:
        print(f"   - {car.name} ({car.model})")

    print("\n3. Итерируемся по автопарку напрямую:")
    for car in fleet:
        print(f"   - {car}")

    print("\n4. Удаляем автомобиль из автопарка:")
    fleet.remove(car1)
    
    print(f"   Количество автомобилей после удаления: {len(fleet)}")
    
    print("\n5. Проверяем содержимое автопарка после удаления:")
    for car in fleet.get_all():
        print(f"   - {car.name}")

if __name__ == "__main__":
    main()

"""