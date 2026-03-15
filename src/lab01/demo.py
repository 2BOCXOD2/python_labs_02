from models import Car, Bus, Transport

if __name__ == "__main__":
    # Демонстрация создания объектов и вывода их описания
    car1 = Car("Volkswagen Golf", 5, 120.0, "GTI")
    bus1 = Bus("Neoplan", 40, 90.0, 2015)

    print("\nОписание машин:")
    print(car1.opisanie())  # Машина Volkswagen Golf, модель GTI: вместимость - 5, средняя скорость - 120.0 км/ч.
    print(bus1.opisanie())  # Автобус Neoplan, год выпуска 2015: вместимость - 40, средняя скорость - 90.0 км/ч.

    # Изменение атрибутов и повторный вывод
    car1.name = "Audi A4"
    bus1.god_vipuska = 2020

    print("\nИзменённые данные:")
    print(car1.opisanie())  # Машина Audi A4, модель GTI: вместимость - 5, средняя скорость - 120.0 км/ч.
    print(bus1.opisanie())  # Автобус Neoplan, год выпуска 2020: вместимость - 40, средняя скорость - 90.0 км/ч.

    # Проверка корректности значений
    try:
        car1.vmestimost = 0  # Невалидная вместимость
    except ValueError as e:
        print(f"\nОшибка: {e}")

    try:
        bus1.god_vipuska = 1800  # Год выпуска раньше 1900-го
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        Auto_exp = Car("?", 2, -30, "10")
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        Auto_exp_2 = Car(int(1.2), 2, 30, "10")
        print(Auto_exp_2.name)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        Auto_exp_3 = Car("", 2, 30, "10")
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    
    # Вычисление стоимости проезда и времени в пути
    car1.rasstoyanie = 100
    bus1.rasstoyanie = 150

    print("\nСтоимость проезда и время в пути:")
    print(f"Стоимость проезда автомобилем: {car1.oplatit_proezd_Car()} руб.")  # 4000 рублей
    print(f"Время в пути автомобилем: {car1.vremya_v_puti()} часов")  # ~0.83 часа

    print(f"Стоимость проезда автобусом: {bus1.oplatit_proezd_Bus()} руб.")  # 4500 рублей
    print(f"Время в пути автобусом: {bus1.vremya_v_puti()} часов")  # ~1.67 часа


    print("===============================================")
    print("Логическое состояние объекта")

    # Создание автомобиля
    car1 = Car("Tesla Model S", 5, 250.0, "P100D")
    print(car1.opisanie())

    # Активация автомобиля
    car1.activate()
    print("Автомобиль активирован:", car1.active)

    # Увеличение уровня обслуживания
    try:
        for i in range(7):
            car1.upgrade()
            print(f"Уровень обслуживания увеличен до {car1.service_level}")
    except ValueError as err:
        print(err)

    # Поездка на автомобиле
    try:
        car1.drive(100)
    except ValueError as err:
        print(err)

    # Создание автобуса
    bus1 = Bus("Hyundai Universe", 40, 100.0, 2015)
    print(bus1.opisanie())

    # Активация автобуса
    bus1.activate()
    print("Автобус активирован:", bus1.active)

    # Заливка топлива и поездка
    try:
        bus1.refill_fuel(50)
        bus1.drive(40)
    except ValueError as err:
        print(err)

    # Проверка границы топливного бака
    try:
        bus1.refill_fuel(60)  # Заведомо превышаем лимит
    except ValueError as err:
        print(err)


    print("===============================================")
    print("Обращение к атрибуту класса через класс и через экземпляр:")

    # Пример доступа к атрибуту класса через класс
    print(f"Максимальная скорость автомобиля: {Car.MAX_SPEED} км/ч")  # Если атрибут MAX_SPEED объявлен в классе Car

    # Пример доступа к атрибуту через экземпляр
    print(f"Скорость экземпляра car1: {car1.sr_skorost} км/ч")