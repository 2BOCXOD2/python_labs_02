from src.lab06.container import TypedCollection, Displayable, Scorable
from src.lab01.models import Car
from src.lab03.models import CargoShip, Airplane


def main():
    print("=== ЛАБОРАТОРНАЯ РАБОТА №6: GENERIC ТИПЫ ===\n")
    
    ###################################### ЗАДАНИЕ 1
    print("ЗАДАНИЕ 1 ----------------------------------\n")


    # 1. Создаем типизированную коллекцию для объектов класса Car
    print("1. Создаем коллекцию для автомобилей:")
    car_collection = TypedCollection[Car](Car) # Явно указываем, что здесь будут только Car
    
    # 2. Добавляем корректный объект
    my_car = Car("MAZDA", 5, 180.0, "Mazda")
    car_0 = Car("КАМАЗ", 4, 110.3, "Камаз")
    car_collection.add(my_car)
    car_collection.add(car_0)
    print(f" - Успешно добавлена: {my_car.name}")
    print(f" - Успешно добавлен: {car_0.name}")
    
    # 3. Демонстрация валидации типов (Попытка добавить неверный тип)
    print("\n2. Демонстрация валидации типов:")
    some_plane = Airplane("Миг", 400, 900.0, 12000, 12000)
    
    try:
        print(f" - Пробуем добавить самолет '{some_plane.name}' в коллекцию машин...")
        car_collection.add(some_plane)
    except TypeError as e:
        print(f"   ОШИБКА (как и ожидалось): {e}")
    
    # 4. Получение всех элементов и вывод
    print("\n3. Получение всех элементов из коллекции:")
    all_cars = car_collection.get_all()
    
    for car in all_cars:
        # Благодаря Generic, IDE знает, что 'car' это объект типа Car
        # и предлагает подсказки для атрибутов .name и .model
        print(f" - Автомобиль: {car.name}, Модель: {car.model}")
    
    # 5. Демонстрация работы с len() и циклом for (из ЛР-2)
    print(f"\n4. Демонстрация интерфейса (len и for):")
    print(f" - Количество машин в коллекции: {len(car_collection)}")
    
    print(" - Список машин через цикл for:")
    for car in car_collection:
        print(f"   * {car.name}")



    ################################################ Задание 2
    print("\nЗАДАНИЕ 2 --------------------------------------\n")



    # Создаем коллекцию автомобилей
    cars = TypedCollection[Car](Car)
    cars.add(Car("BMW E34", 5, 220.0, "X5", price=9_000_000))
    cars.add(Car("Lada Vesta Cross", 5, 150.5, "Vesta", price=1_500_000))
    cars.add(Car("Mercedes Caban", 5, 210.0, "E-Class", price=7_500_000))
    
    print("Исходная коллекция автомобилей:")
    for car in cars:
        print(f" - {car.name}: {car.calculate_price():,.0f} у.е.")


    # --- СЦЕНАРИЙ 1: Метод find() ---
    print("\n1. ДЕМОНСТРАЦИЯ МЕТОДА find():")
    
    # 1.1: Поиск элемента (элемент найден)
    found_car = cars.find(lambda c: c.name == "Mercedes Caban")
    if found_car:
        print(f" - Найдено: {found_car.name}")
    else:
        print(" - Не найдено")
        
    # 1.2: Поиск элемента (элемент НЕ найден)
    not_found_car = cars.find(lambda c: c.name == "Audi A8")
    if not_found_car:
        print(f" - Найдено: {not_found_car.name}")
    else:
        print(" - Не найдено (Audi A8 отсутствует в коллекции)")


    # --- СЦЕНАРИЙ 2: Метод filter() ---
    print("\n2. ДЕМОНСТРАЦИЯ МЕТОДА filter():")
    
    # Фильтруем только дорогие машины (цена > 8 млн)
    expensive_cars = cars.filter(lambda c: c.calculate_price() > 8_000_000)
    
    print(" - Дорогие автомобили (цена > 8 млн):")
    for car in expensive_cars:
         print(f"   * {car.name}: {car.calculate_price():,.0f} у.е.")


    # --- СЦЕНАРИЙ 3: Метод map() ---
    print("\n3. ДЕМОНСТРАЦИЯ МЕТОДА map(): Изменение типа результата")
    
    # Сценарий 3.1: Преобразуем список машин в список СТРОК (list[str])
    car_names = cars.map(lambda c: c.name)
    
    print("   Тип результата:", type(car_names))
    print("   Содержимое (список имен):")
    for name in car_names:
         print(f"   - {name} (тип элемента: {type(name).__name__})")
    
    # Сценарий 3.2: Преобразуем список машин в список ЧИСЕЛ (list[float])
    car_prices = cars.map(lambda c: c.calculate_price())
    
    print("\n   Тип результата:", type(car_prices))
    print("   Содержимое (список цен):")
    for price in car_prices:
         print(f"   - {price:,.0f} у.е. (тип элемента: {type(price).__name__})")



    # -------------------------------------------------ЗАДАНИЕ 3
    print("\nЗадание 3 --------------------------------------------\n")
    
    # Создаем объекты для демонстрации
    ship1 = CargoShip("Атомный ледокол", 20, 40.0, 50000, 500)
    ship2 = CargoShip("Контейнеровоз", 10, 35.0, 220000, 1200)
    
    plane1 = Airplane("Миг", 440, 945.0, 13100, 17100)
    plane2 = Airplane("Су", 366, 903.0, 13000, 16500)
    
    # --- СЦЕНАРИЙ 1: TypedCollection[Displayable] ---
    print("--- СЦЕНАРИЙ 1: Коллекция Displayable (вывод информации) ---")
    
    displayables = TypedCollection[Displayable]()
    displayables.add(ship1)
    displayables.add(plane1)
    
    print("Объекты добавлены в коллекцию. Вызываем метод display_all():")
    # Метод знает, что у всех объектов внутри есть метод .display()
    displayables.display_all()
    
    # Добавим еще один объект другого типа (корабль)
    print("\nДобавляем еще один объект (другого типа):")
    displayables.add(ship2)
    displayables.display_all()
    
    # --- СЦЕНАРИЙ 2: TypedCollection[Scorable] ---
    print("\n\n--- СЦЕНАРИЙ 2: Коллекция Scorable (расчет оценки) ---")
    
    scorables = TypedCollection[Scorable]()
    scorables.add(ship1)
    scorables.add(ship2)
    scorables.add(plane1)
    
    print("В коллекции объекты разных типов (Корабли и Самолеты).")
    print("Они оцениваются по-разному (грузоподъемность vs скорость).")
    
    average_score = scorables.calculate_average_score()
    print(f"\nСредняя оценка всех объектов в коллекции: {average_score:.2f}")
    
    # Покажем индивидуальные оценки для наглядности
    print("\nИндивидуальные оценки:")
    for item in scorables.get_all():
        # Мы можем безопасно вызывать score(), так как коллекция TypedCollection[Scorable]
        print(f" - {item.name}: {item.score()}")




if __name__ == "__main__":
    main()


# Вызов через терминал:     python -m src.lab06.demo


'''
def a(x):
    def b(y):
        x * y
    return b()

a2 = a(2)

print(a2(3))  # = 6
'''