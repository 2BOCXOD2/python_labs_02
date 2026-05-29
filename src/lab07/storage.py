import json
import os
from typing import List, Dict, Any

# Импортируем модели, чтобы знать, как их восстанавливать
from src.lab07.models import Car, CargoShip, Airplane

def save(collection, filepath: str) -> None:
    """
    Сохраняет коллекцию объектов в JSON-файл.

    Функция проходит по всем элементам коллекции, преобразует каждый объект
    в словарь с его данными и типом, а затем записывает весь список в файл.
    Также автоматически создает директорию для файла, если она не существует.

    Args:
        collection: Коллекция объектов с методом get_all().
        filepath: Путь к файлу (включая имя файла), куда нужно сохранить данные.
    """
    # Создаем папку 'data', если ее нет.
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    data_to_save = []
    
    
    # --- ИЗМЕНЕНИЕ: Проверяем, что нам передали ---
    # Если у объекта есть метод get_all(), используем его (для обратной совместимости)
    # Иначе считаем, что нам передали сам список (наш новый случай)
    items_to_save = collection.get_all() if hasattr(collection, 'get_all') else collection
    
    for item in items_to_save:
        # 1. Создаем словарь с общими полями для всех Transport
        item_data = {
            'name': item.name,
            'vmestimost': item.vmestimost,
            'sr_skorost': item.sr_skorost,
            'active': item.active,
        }
        
        # 2. Добавляем специфичные поля для каждого типа объекта
        if isinstance(item, Car):
            item_data['model'] = item.model
            item_data['price'] = item.price
        elif isinstance(item, CargoShip):
            item_data['cargo_capacity_tons'] = item.cargo_capacity_tons
            item_data['route_length_nm'] = item.route_length_nm
        elif isinstance(item, Airplane):
            item_data['max_flight_altitude_m'] = item.max_flight_altitude_m
            item_data['fuel_consumption_lph'] = item.fuel_consumption_lph

        # 3. Собираем финальный словарь для JSON
        item_dict = {
            "type": item.__class__.__name__, # Например, "Car"
            "data": item_data               # Словарь со всеми атрибутами
        }
        data_to_save.append(item_dict)

    # Записываем данные в файл
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    
    print(f"   💾 Данные успешно сохранены в {filepath}")


def load(filepath: str) -> List[Any]:
    """
    Загружает объекты из JSON-файла и возвращает их список.

    Функция читает JSON-файл, восстанавливает тип каждого объекта на основе
    поля "type" и создает экземпляр соответствующего класса.

    Args:
        filepath: Путь к файлу, из которого нужно загрузить данные.

    Returns:
        Список восстановленных объектов (экземпляров классов).
        Если файл не найден, возвращает пустой список.
    """
    if not os.path.exists(filepath):
        print(f"   📂 Файл {filepath} не найден. Коллекция будет пустой.")
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    loaded_items = []
    for item_dict in data:
        obj_type = item_dict["type"]
        obj_data = item_dict["data"]
        
        try:
            if obj_type == "Car":
                loaded_items.append(Car(**obj_data))
            elif obj_type == "CargoShip":
                loaded_items.append(CargoShip(**obj_data))
            elif obj_type == "Airplane":
                loaded_items.append(Airplane(**obj_data))
        except Exception as e:
            print(f"   ⚠️  Ошибка при загрузке объекта типа {obj_type}: {e}")
    
    print(f"   📂 Данные загружены из {filepath}")
    return loaded_items