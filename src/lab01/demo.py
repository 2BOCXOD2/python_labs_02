from models import Car, Bus, Transport

if __name__ == "__main__":
    print("===============================================")
    print("Демонстрация создания объектов и вывода их описания")
    car1 = Car("Volkswagen Golf", 5, 120.0, "GTI")
    bus1 = Bus("Neoplan", 40, 90.0, 2015)

    print("\nВывод описания созданных объектов:")
    print(car1.opisanie())  # Машина Volkswagen Golf, модель GTI: вместимость - 5, средняя скорость - 120.0 км/ч.
    print(bus1.opisanie())  # Автобус Neoplan, год выпуска 2015: вместимость - 40, средняя скорость - 90.0 км/ч.

    print("-------------------")
    print("Изменение атрибутов и повторный вывод")
    car1.name = "Audi A4"
    bus1.god_vipuska = 2020

    print("\nИзменённые данные:")
    print(car1.opisanie())  # Машина Audi A4, модель GTI: вместимость - 5, средняя скорость - 120.0 км/ч.
    print(bus1.opisanie())  # Автобус Neoplan, год выпуска 2020: вместимость - 40, средняя скорость - 90.0 км/ч.

    print("===============================================")
    print("Проверка корректности вводимых значений")
    try:
        print("Устанавливаем заведомо невалидную вместимость = 0:")
        car1.vmestimost = 0  # Невалидная вместимость
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        print("Устанавливаем заведомо невалидный год выпуска = 1800:")
        bus1.god_vipuska = 1800  # Год выпуска раньше 1900-го
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("Устанавливаем заведомо невалидную скорость = -30:")
        Auto_exp = Car("?", 2, -30, "10")
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("Устанавливаем невалидный тип данных для имени = int(1.2)")
        Auto_exp_2 = Car(int(1.2), 2, 30, "10")
        print(Auto_exp_2.name)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        print("Устанавливаем заведомо пустое имя = ''")
        Auto_exp_3 = Car("", 2, 30, "10")
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    
    # Вычисление стоимости проезда и времени в пути
    print("===============================================")
    print("Вычисление стоимости проезда и времени в пути")
    print("Входные данные: расстояние для машины - 100, для автобуса - 150")
    car1.rasstoyanie = 100
    bus1.rasstoyanie = 150

    print("-------------------")
    print("Стоимость проезда и время в пути:")
    print(f"Стоимость проезда автомобилем: {car1.oplatit_proezd_Car()} руб.")  # 4000 рублей
    print(f"Время в пути автомобилем: {car1.vremya_v_puti()} часов")  # ~0.83 часа

    print("-------------------")
    print(f"Стоимость проезда автобусом: {bus1.oplatit_proezd_Bus()} руб.")  # 4500 рублей
    print(f"Время в пути автобусом: {bus1.vremya_v_puti()} часов")  # ~1.67 часа


    print("===============================================")
    print("Логическое состояние объекта")
    
    print("-------------------")
    print("Создание автомобиля")
    car1 = Car("Tesla Model S", 5, 250.0, "P100D")
    print(car1.opisanie())

    print("Активация автомобиля")
    car1.activate()
    print("Автомобиль активирован:", car1.active)

    print("Повышение уровня обслуживания")
    try:
        for i in range(7):
            car1.upgrade()
            print(f"Уровень обслуживания увеличен до {car1.service_level}")
    except ValueError as err:
        print(err)

    print("Поездка на автомобиле")
    try:
        car1.drive(100)
    except ValueError as err:
        print(err)
    
    print("-----------------")
    print("Создание автобуса")
    bus1 = Bus("Hyundai Universe", 40, 100.0, 2015)
    print(bus1.opisanie())

    print("Активация автобуса")
    bus1.activate()
    print("Автобус активирован:", bus1.active)

    print("Заливка топлива и поездка")
    try:
        bus1.refill_fuel(50)
        bus1.drive(40)
    except ValueError as err:
        print(err)

    print("Проверка границы топливного бака")
    try:
        print("Заведомо превышаем лимит")
        bus1.refill_fuel(60)  # Заведомо превышаем лимит
    except ValueError as err:
        print(err)


    print("===============================================")
    print("Обращение к атрибуту класса через класс и через экземпляр:")

    print("Пример доступа к атрибуту класса через класс")
    print(f"Максимальная скорость автомобиля: {Car.MAX_SPEED} км/ч")

    print("Пример доступа к атрибуту через экземпляр")
    print(f"Скорость экземпляра car1: {car1.sr_skorost} км/ч")