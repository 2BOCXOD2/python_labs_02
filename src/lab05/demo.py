from src.lab05.collection import Fleet
from src.lab05.strategies import by_name_asc, by_price_desc, by_speed_and_name, is_expensive, is_ship, make_price_filter, apply_discount, DiscountStrategy, UpgradeStrategy, by_name_asc, by_price_desc
from src.lab01.models import Car
from src.lab03.models import CargoShip, Airplane

def main():
    print("=== ЛАБОРАТОРНАЯ РАБОТА №5: ПАТТЕРН 'СТРАТЕГИЯ' ===\n")
    
    # ЗАДАНИЕ 1 ------------------------------------------------------------
    print("Задание 1 ------------------------------------------------------------\n")

    # 1. Создаем коллекцию и наполняем её (минимум 5 объектов)
    transport_fleet = Fleet()
    
    transport_fleet.add(Car("Lada", 5, 120.5, "Vesta", price=1_200_000))
    transport_fleet.add(Car("BMW", 4, 220.0, "X5", price=8_500_000))
    transport_fleet.add(Airplane("Боинг", 420, 900.0, 13000, 12000))
    transport_fleet.add(CargoShip("Контейнеровоз", 20, 40.0, 15000, 4800))
    transport_fleet.add(Airplane("Аэробус", 350, 850.5, 12500, 11500))
    
    print("--- ИСХОДНАЯ КОЛЛЕКЦИЯ ---")
    for t in transport_fleet:
         print(f" - {t.name} (Цена: {t.calculate_price():,.0f} у.е.)")
    
    # 2. Демонстрация сортировки тремя разными стратегиями

    print("\n1. СОРТИРОВКА ПО ИМЕНИ (по возрастанию):")
    transport_fleet.sort_by_strategy(by_name_asc)
    for t in transport_fleet:
         print(f" - {t.name}")

    print("\n2. СОРТИРОВКА ПО ЦЕНЕ (по убыванию):")
    transport_fleet.sort_by_strategy(by_price_desc)
    for t in transport_fleet:
         print(f" - {t.name}: {t.calculate_price():,.0f} у.е.")
         
    print("\n3. СОРТИРОВКА ПО СКОРОСТИ И ИМЕНИ (скорость вниз, имя вверх):")
    transport_fleet.sort_by_strategy(by_speed_and_name)
    for t in transport_fleet:
         print(f" - {t.name}: Скорость {t.sr_skorost} км/ч")

    # 3. Демонстрация фильтрации двумя разными функциями

    print("\n--- ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ ---")
    
    # Стратегия 1: Фильтр по условию (цена > 5 млн)
    print("\n1. Только дорогие объекты (цена > 5 000 000):")
    
    ''' lab01
    expensive_filter = is_expensive(5_000_000) # Создаем функцию-фильтр с порогом
    expensive_items = transport_fleet.filter_by_strategy(expensive_filter)
    
    for t in expensive_items:
         print(f" - {t.name}: {t.calculate_price():,.0f} у.е.")
    
    # Стратегия 2: Фильтр по типу объекта (только корабли)
    print("\n2. Только объекты типа 'Корабль':")
    ships_only = transport_fleet.filter_by_strategy(is_ship)
    
    for t in ships_only:
         print(f" - {t.name}")
     '''

    expensive_items = transport_fleet.filter_by(is_expensive)
    print("Фильтр 'is_expensive' (цена > 5 млн):")
    for t in expensive_items:
         print(f" - {t.name}: {t.calculate_price():,.0f} у.е.")

    print("\n2. Только объекты типа 'Корабль':")
    ships_only = transport_fleet.filter_by_strategy(is_ship)
    
    for t in ships_only:
         print(f" - {t.name}")

    # ЗАДАНИЕ 2 ------------------------------------------------------------
    print("\nЗадание 2 ------------------------------------------------------------\n")

    def to_dict(item):
        """Именованная функция для преобразования объекта в словарь."""
        return {
            "name": item.name,
            "type": item.__class__.__name__,
            "price": item.calculate_price()
        }


    print("=== ДЕМОНСТРАЦИЯ LAB05: MAP, ФАБРИКИ И LAMBDA ===\n")
    
    # 1. Создаем коллекцию и наполняем её
    transport_fleet = Fleet()
    
    transport_fleet.add(Car("Lada Vesta", 5, 150.5, "Vesta", price=1_500_000))
    transport_fleet.add(Car("BMW X5", 5, 220.0, "X5", price=9_000_000))
    transport_fleet.add(Airplane("Боинг-747", 420, 900.0, 13000, 12000))
    transport_fleet.add(CargoShip("Надежда", 20, 40.0, 15000, 4800))
    transport_fleet.add(Airplane("Аэробус A380", 525, 950.5, 13500, 13000))
    
    print("--- ИСХОДНАЯ КОЛЛЕКЦИЯ ---")
    for t in transport_fleet:
         print(f" - {t.name}: {t.calculate_price():,.0f} у.е.")

    # 2. Демонстрация MAP(): Преобразование объектов в словари
    print("\n1. ПРИМЕНЕНИЕ MAP(): Преобразование в словари")
    
    # Вариант А: Через именованную функцию (to_dict)
    dicts_via_named_fn = transport_fleet.apply(to_dict)
    
    # Вариант Б: Через lambda (сравнение)
    dicts_via_lambda = transport_fleet.apply(lambda x: {"name": x.name, "type": x.__class__.__name__, "price": x.calculate_price()})
    
    print("   Результат через именованную функцию:")
    for d in dicts_via_named_fn[:2]:
        print(f"   - {d['name']} ({d['type']}): {d['price']:,.0f} у.е.")
        
    print("\n   Результат через lambda (тот же):")
    for d in dicts_via_lambda[:2]:
        print(f"   - {d['name']} ({d['type']}): {d['price']:,.0f} у.е.")

    # 3. Демонстрация MAP(): Применение скидки
    print("\n2. ПРИМЕНЕНИЕ MAP(): Применение скидки 15%")
    
    # Используем фабрику apply_discount для создания функции применения скидки
    apply_15_discount = apply_discount(0.15)
    discounted_prices = transport_fleet.apply(apply_15_discount)
    
    for name, price in zip([t.name for t in transport_fleet], discounted_prices):
        print(f"   - {name}: Новая цена {price:,.0f} у.е.")

    # 4. Демонстрация ФАБРИКИ ФУНКЦИЙ и ФИЛЬТРАЦИИ
    print("\n3. ДЕМО ФАБРИКИ ФУНКЦИЙ (Фильтр по цене)")
    
    # Создаем фильтр с порогом 5 млн, используя фабрику
    cheap_items_filter = make_price_filter(5_000_000)
    
    # Применяем его через новый метод filter_by()
    cheap_transport = transport_fleet.filter_by(cheap_items_filter)
    
    print("   Объекты дешевле 5 млн:")
    for t in cheap_transport:
         print(f"   - {t.name}: {t.calculate_price():,.0f} у.е.")

    # 4. Демонстрация методов sort_by() и filter_by() с lambda
    print("\n4. ДЕМО МЕТОДОВ sort_by() и filter_by() С ИСПОЛЬЗОВАНИЕМ LAMBDA")
    
    # Сортировка по имени (используем lambda)
    print("\n   Сортировка по имени:")
    transport_fleet.sort_by(lambda x: x.name)
    for t in transport_fleet:
         print(f"   - {t.name}")

    # Фильтрация по типу объекта (используем lambda с isinstance)
    print("\n   Фильтрация только для Airplane:")
    planes_only = transport_fleet.filter_by(lambda x: isinstance(x, Airplane))
    
    for p in planes_only:
         print(f"   - {p.name}")




    
    # ЗАДАНИЕ 3 ------------------------------------------------------------
    print("Задание 3 ------------------------------------------------------------\n") 

    # --- СЦЕНАРИЙ 1: Полная цепочка filter → sort → apply ---
    print("--- СЦЕНАРИЙ 1: ПОЛНАЯ ЦЕПОЧКА ОПЕРАЦИЙ (filter -> sort -> apply) ---")
    
    # 1.1: Создаем коллекцию
    chain_fleet = Fleet()
    chain_fleet.add(Car("Lada", 5, 120.5, "Vesta", price=1_200_000))
    chain_fleet.add(Car("BMW", 4, 220.0, "X5", price=8_500_000))
    chain_fleet.add(Airplane("Боинг", 420, 900.0, 13000, 12000))
    chain_fleet.add(CargoShip("Надежда", 20, 40.0, 15000, 4800))
    chain_fleet.add(Airplane("Аэробус", 525, 950.5, 13500, 13000))

    print("Исходная коллекция:")
    for t in chain_fleet:
        print(f" - {t.name} (Цена: {t.calculate_price():,.0f})")

    # 1.3: Шаг 1 - Фильтрация (оставляем только дорогие)
    filtered = chain_fleet.filter_by(lambda x: x.calculate_price() > 5_000_000)
    print("\n1 - После фильтрации (цена > 5 млн):")
    for t in filtered:
        print(f" - {t.name}")

    # 1.5: Шаг 2 - Сортировка (по имени)
    filtered.sort_by(by_name_asc)
    print("\n2 - После сортировки (по имени):")
    for t in filtered:
        print(f" - {t.name}")

    # 1.7: Шаг 3 - Применение функции (скидка 25%)
    apply_discount1 = DiscountStrategy(0.25)
    discounted_prices = filtered.apply(apply_discount1)
    print("\n3 - После применения скидки 25%:")
    for price in discounted_prices:
        print(f" - Новая цена: {price:,.0f} у.е.")


    # --- СЦЕНАРИЙ 2: Замена стратегии ---
    print("\n\n--- СЦЕНАРИЙ 2: ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА ---")
    
    # Создаем коллекцию машин для этого сценария
    cars = Fleet()
    cars.add(Car("Тесла S", 4, 250, "S", price=1_100_000))
    cars.add(Car("Тесла X", 5, 250, "X", price=1_300_000))

    # Стратегия А: Скидка 10%
    strategy_a = DiscountStrategy(0.1)
    result_a = cars.apply(strategy_a)
    
    # Стратегия Б: Скидка 30%
    strategy_b = DiscountStrategy(0.3)
    result_b = cars.apply(strategy_b)

    print("Применение разных стратегий к одним и тем же объектам:")
    names = [car.name for car in cars.get_all()]
    
    for name, price_a, price_b in zip(names, result_a, result_b):
        print(f" - {name}:")
        print(f"     * Скидка 10% -> {price_a:,.0f} у.е.")
        print(f"     * Скидка 30% -> {price_b:,.0f} у.е.")


    # --- СЦЕНАРИЙ 3: Демонстрация callable-объекта ---
    print("\n\n--- СЦЕНАРИЙ 3: CALLABLE-ОБЪЕКТ КАК СТРАТЕГИЯ ---")
    
    # Создаем коллекцию для сценария с обновлением
    upgradable = Fleet()
    upgradable.add(Car("Старый Авто", 4, 180, "Model S", price=900_000))

    # Создаем объект-стратегию
    upgrade_strategy = UpgradeStrategy()
    
    # Применяем его как обычную функцию!
    # Метод apply() вызывает strategy(item), а стратегия внутри вызывает item.upgrade()
    reports = upgradable.apply(upgrade_strategy)

    print("Результат применения callable-объекта:")
    for report in reports:
        print(f" - {report}")


##################################################################
    '''
    print("=== ЛАБОРАТОРНАЯ РАБОТА №5: ПАТТЕРН 'СТРАТЕГИЯ' И ЦЕПОЧКИ ===\n")
    
    # --- СЦЕНАРИЙ 1: Полная цепочка filter -> sort -> apply ---
    
    print("--- СЦЕНАРИЙ 1: ЦЕПОЧКА ОПЕРАЦИЙ ---")
    
    # Создаем НОВУЮ коллекцию для этого сценария, чтобы не мешать другим
    transport_fleet = Fleet()
    
    transport_fleet.add(Car("Lada Vesta", 5, 150.5, "Vesta", price=1_500_000))
    transport_fleet.add(Car("BMW X5", 5, 220.0, "X5", price=9_000_000))
    transport_fleet.add(Airplane("Боинг-747", 420, 900.0, 13000, 12000))
    transport_fleet.add(CargoShip("Надежда", 20, 40.0, 15000, 4800))
    transport_fleet.add(Airplane("Аэробус A380", 525, 950.5, 13500, 13000))
    
    print("ИСХОДНАЯ КОЛЛЕКЦИЯ:")
    for t in transport_fleet.get_all():
         print(f" - {t.name}: {t.calculate_price():,.0f} у.е.")
    
    # Цепочка: Фильтруем дорогие -> Сортируем по цене -> Применяем скидку 25%
    print("\nРЕЗУЛЬТАТ ЦЕПОЧКИ (filter -> sort -> apply):")
    
    # 1. Фильтрация (оставляет в коллекции только дорогие)
    # 2. Сортировка (сортирует эту отфильтрованную коллекцию)
    # 3. apply (применяет функцию к результату сортировки)
    results = (transport_fleet
               .filter_by(lambda x: x.calculate_price() > 2_000_000) # Фильтр через lambda
               .sort_by(by_price_desc)                              # Сортировка через именованную функцию
               .apply(DiscountStrategy(0.25)))                     # Применение callable-объекта
    
    for result in results:
         print(f" - {result:,.0f} у.е.") # Выводим только новые цены

    # --- СЦЕНАРИЙ 2: Замена стратегии ---
    
    print("\n--- СЦЕНАРИЙ 2: ВЗАИМОЗАМЕНЯЕМЫЕ СТРАТЕГИИ ---")
    
    # Создаем еще одну коллекцию для чистоты эксперимента
    cars_only = Fleet()
    cars_only.add(Car("Авто 1", 4, 180, "Model S", price=1_000_000))
    cars_only.add(Car("Авто 2", 5, 220, "Model X", price=1_200_000))
    
    print("Применяем разные стратегии к одной и той же коллекции:")
    
    # Стратегия А: Скидка 15%
    discount_15 = DiscountStrategy(0.15)
    prices_after_discount_15 = cars_only.apply(discount_15)
    print("\nСтратегия А (Скидка 15%):")
    for p in prices_after_discount_15:
         print(f" - {p:,.0f} у.е.")
         
    # Стратегия Б: Обновление (upgrade)
    upgrader = UpgradeStrategy()
    
    # Важно: Мы создаем НОВУЮ коллекцию или заново наполняем старую,
    # так как метод apply() в сценарии 1 изменил коллекцию!
    cars_only_for_upgrade = Fleet()
    cars_only_for_upgrade.add(Car("Авто 1", 4, 180, "Model S", price=1_000_000))
    cars_only_for_upgrade.add(Car("Авто 2", 5, 220, "Model X", price=1_200_000))
    
    upgrade_reports = cars_only_for_upgrade.apply(upgrader)
    
    print("\nСтратегия Б (Обновление):")
    for report in upgrade_reports:
         print(f" - {report}")
         
         # Также покажем состояние объекта после изменения
         # Находим машину по имени и выводим уровень сервиса
         for car in cars_only_for_upgrade.get_all():
             if car.name in report:
                 print(f"   * Уровень сервиса {car.name} теперь: {car.service_level}")
    '''


if __name__ == "__main__":
    main()


# Запуск через терминал     python -m src.lab05.demo