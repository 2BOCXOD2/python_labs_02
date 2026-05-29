from src.lab07.app import TransportApp
from src.lab07.models import Transport, Car, CargoShip, Airplane
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError


def show_menu():
    print("\n" + "="*30 + " МЕНЮ " + "="*30)
    print("1. Добавить транспорт")
    print("2. Показать весь транспорт")
    print("3. Найти транспорт по названию")
    print("4. Фильтровать по цене")
    print("5. Удалить транспорт")
    print("6. Сортировать коллекцию")
    print("0. Выход")
    print("="*70)

def print_table(items: list) -> None:
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

def run_cli():
    app = TransportApp()
    
    while True:
        show_menu()
        
        try:
            choice = int(input("Выберите пункт меню: "))
            
            if choice == 1:
                # --- ДОБАВЛЕНИЕ ---
                print("\n--- ТИПЫ ТРАНСПОРТА ---")
                print("1. Автомобиль")
                print("2. Грузовой корабль")
                print("3. Самолет")
                
                type_code = int(input("Выберите тип (1-3): "))
                # name = input("Название: ")
                # vmestimost = int(input("Вместимость: "))
                # sr_skorost = float(input("Средняя скорость: "))
                
                if type_code == 1:
                    name = input("Название: ")
                    vmestimost = int(input("Вместимость: "))
                    sr_skorost = float(input("Средняя скорость: "))
                    model = input("Модель авто: ")
                    price = float(input("Цена: "))
                    new_item = Car(name, vmestimost, sr_skorost, model, price)
                    
                elif type_code == 2:
                    name = input("Название: ")
                    vmestimost = int(input("Вместимость: "))
                    sr_skorost = float(input("Средняя скорость: "))
                    cargo_tons = int(input("Грузоподъемность (т): "))
                    route_nm = int(input("Длина маршрута (м.м.): "))
                    new_item = CargoShip(name, vmestimost, sr_skorost, cargo_tons, route_nm)
                    
                elif type_code == 3:
                    name = input("Название: ")
                    vmestimost = int(input("Вместимость: "))
                    sr_skorost = float(input("Средняя скорость: "))
                    altitude = int(input("Макс. высота (м): "))
                    fuel_cons = int(input("Расход топлива (л/ч): "))
                    new_item = Airplane(name, vmestimost, sr_skorost, altitude, fuel_cons)
                
                # Ошибка ввода неверного значения
                else:
                    print(f"   ❌ ОШИБКА ВВОДА: {e}")
                
                # Пытаемся добавить, ловим нашу ошибку-дубликат
                try:
                    result = app.add_item(new_item)
                    print(result)
                except DuplicateItemError as e:
                    print(f"   ❌ ОШИБКА: {e}")

            elif choice == 2:
                # --- ПОКАЗАТЬ ВСЕ ---
                items = app.get_all_items()
                print_table(items)

            elif choice == 3:
                # --- ПОИСК ПО НАЗВАНИЮ ---
                query = input("Введите часть названия для поиска: ")
                try:
                    results = app.search_by_name(query)
                    print_table(results)
                except ItemNotFoundError as e:
                    print(f"   ❌ {e}")

            elif choice == 4:
                # --- ФИЛЬТРАЦИЯ ПО ЦЕНЕ ---
                try:
                    min_p = float(input("Минимальная цена: "))
                    max_p = float(input("Максимальная цена: "))
                    results = app.filter_by_price_range(min_p, max_p)
                    # print_table(results)
                    print("-" * 50)
                    print("Отфильтрованная коллекция:")
                    for transport in results:
                        print(f"/// {transport.name} --- {transport.calculate_price()}")
                    print("-" * 50)
                except ItemNotFoundError as e:
                    print(f"   ❌ {e}")

            elif choice == 5:
                 # --- УДАЛЕНИЕ С ПОДТВЕРЖДЕНИЕМ ---
                 name = input("Введите название для удаления: ")
                 confirm = input(f"Удалить '{name}'? (y/n): ").lower()
                 if confirm == 'y':
                     try:
                         result = app.remove_item_by_name(name)
                         print(result)
                     except ItemNotFoundError as e:
                         print(f"   ❌ {e}")
                 else:
                     print(f"   ❌ Удаление '{name}' отменено.")


            elif choice == 6:
                # --- НОВЫЙ БЛОК: СОРТИРОВКА ---
                print("\n--- ВЫБЕРИТЕ СТРАТЕГИЮ СОРТИРОВКИ ---")
                print("1. По названию")
                print("2. По цене")
                print("3. По дате добавления")
                
                sort_choice = int(input("Стратегия (1-3): "))
                
                # Определяем, какую строку передать в app.sort_items()
                if sort_choice == 1:
                    strategy = 'name'
                elif sort_choice == 2:
                    strategy = 'price'
                elif sort_choice == 3:
                    strategy = 'date'
                else:
                    print("Неверный выбор стратегии.")
                    continue # Возвращаемся в начало цикла while

                # Вызываем бизнес-логику сортировки
                try:
                    result = app.sort_items(strategy)
                    print(result)
                    
                    # Получаем отсортированный список и выводим его
                    items = app.get_all_items() 
                    print_table(items)
                    
                except ValueError as e:
                    print(f"   ❌ ОШИБКА: {e}")


            elif choice == 0:
                # --- НОВОЕ: Вызываем метод выхода с сохранением ---
                app.exit_app()
                # print("   До свидания!")
                # break

        except ValueError as ve:
            print(f"   ❌ Ошибка ввода: {ve}. Вводите корректные значения.")
        except Exception as e:
            # Ловим любые другие непредвиденные ошибки
            print(f"   ❌ Непредвиденная ошибка: {e}")












#################################################


'''
from src.lab07.app import TransportApp

def show_menu():
    print("\n" + "="*30 + " МЕНЮ " + "="*30)
    print("1. Добавить транспорт")
    print("2. Показать весь транспорт")
    print("3. Найти транспорт по названию")
    print("4. Фильтровать по цене")
    print("5. Фильтровать по статусу (Активен)")
    print("6. Удалить транспорт")
    print("7. Стратегии сортировки")
    print("0. Выход")
    print("="*70)

def run_cli() -> None:  # Добавили аннотацию типа
    """Запускает цикл работы консольного интерфейса."""
    app = TransportApp()
    
    while True:
        show_menu()
        
        try:
            choice = int(input("Выберите пункт меню: "))
            
            if choice == 1:
                # --- ЭТОТ БЛОК НУЖНО ИСПРАВИТЬ ---
                print("\n--- ТИПЫ ТРАНСПОРТА ---")
                print("1. Автомобиль")
                print("2. Грузовой корабль")
                print("3. Самолет")
                
                # 1. Собираем данные от пользователя
                type_code = int(input("Выберите тип (1-3): "))
                
                name = input("Название: ")
                vmestimost = int(input("Вместимость: "))
                sr_skorost = float(input("Средняя скорость: "))
                    
                # 2. Формируем словарь с данными (data)
                data = {
                    'name': name,
                    'vmestimost': vmestimost,
                    'sr_skorost': sr_skorost
                }
                    
                # 3. Добавляем специфичные параметры для каждого типа
                if type_code == 1:
                    model = input("Модель авто: ")
                    price = float(input("Цена: "))
                    data.update({'model': model, 'price': price})
                elif type_code == 2:
                    cargo_tons = int(input("Грузоподъемность (т): "))
                    route_nm = int(input("Длина маршрута (м.м.): "))
                    data.update({'cargo_capacity_tons': cargo_tons, 'route_length_nm': route_nm})
                elif type_code == 3:
                    altitude = int(input("Макс. высота (м): "))
                    fuel_cons = int(input("Расход топлива (л/ч): "))
                    data.update({'max_flight_altitude_m': altitude, 'fuel_consumption_lph': fuel_cons})
                else:
                    raise ValueError("Ошибка ввода. Вводите корректные значения.")    
                # 4. Вызываем метод БИЗНЕС-ЛОГИКИ и передаем ему аргументы!
                result_message = app.add_item(item_type_code=type_code, data=data)
                print(result_message) # Выводим результат, который вернул app.py
                

            elif choice == 2:
                app.show_all() # Этот метод уже вызывает print_table внутри себя

            elif choice == 3:
                query = input("Введите часть названия для поиска: ")
                results = app.search_by_name(query)
                # Было: TransportApp.print_table(results)
                app.print_table(results) # Стало: вызываем через экземпляр app

            elif choice == 4:
                min_p = float(input("Минимальная цена: "))
                max_p = float(input("Максимальная цена: "))
                results = app.filter_by_price_range(min_p, max_p)
                # Было: TransportApp.print_table(results)
                app.print_table(results) # Стало: вызываем через экземпляр app

            elif choice == 5:
                status = bool(int(input("Статус (1 - Активен, 0 - Неактивен): ")))
                results = app.filter_by_status(status)
                # Было: TransportApp.print_table(results)
                app.print_table(results) # Стало: вызываем через экземпляр app

            elif choice == 6:
                 name = input("Введите название для удаления: ")
                 # Для удаления можно использовать старый метод или добавить новый в app.py
                 # Сейчас просто вызовем существующий
                 app.remove_item(name) 

            
            # --- НОВОЕ МЕНЮ СОРТИРОВКИ ---
            elif choice == 7:
                print("\n--- СОРТИРОВКА ---")
                print("1. По названию")
                print("2. По цене")
                print("3. По дате добавления")
                sort_choice = int(input("Выберите стратегию сортировки: "))
                
                if sort_choice == 1:
                    app.sort_by_name()
                elif sort_choice == 2:
                    app.sort_by_price()
                elif sort_choice == 3:
                    app.sort_by_date()
                else:
                    print("Неверный выбор стратегии.")
                
                app.show_all() # Показываем результат сортировки


            # --- ВЫХОД С СОХРАНЕНИЕМ ---
            elif choice == 0:
                app.exit_app() # Вызываем метод для сохранения и выхода

            else:
                print("Неверный пункт меню.")
                
        except ValueError as ve:
            print(f"Ошибка ввода: {ve}. Вводите числа.")

'''










'''
from src.lab07.app import TransportApp

def show_menu():
    print("\n=== МЕНЮ УПРАВЛЕНИЯ ТРАНСПОРТОМ ===")
    print("1. Добавить транспорт")
    print("2. Показать весь транспорт")
    print("3. Найти транспорт по названию")
    print("4. Удалить транспорт")
    print("5. Очистить коллекцию")
    print("0. Выход")

def run_cli():
    app = TransportApp()
    
    while True:
        show_menu()
        
        try:
            choice = int(input("\nВыберите пункт меню: "))
            
            if choice == 1:
                app.add_item()
            elif choice == 2:
                app.show_all()
            elif choice == 3:
                app.find_item()
            elif choice == 4:
                app.remove_item()
            elif choice == 5:
                confirm = input("Вы уверены, что хотите очистить коллекцию? (y/n): ")
                if confirm.lower() == 'y':
                    app.collection._items.clear()
                    print("Коллекция очищена.")
            elif choice == 0:
                print("До свидания!")
                break
            else:
                print("Ошибка: выберите пункт из списка (0-5).")
                
        except ValueError:
            # Срабатывает, если input() не может быть преобразован в int
            print("Ошибка: введите число от 0 до 5.")
'''