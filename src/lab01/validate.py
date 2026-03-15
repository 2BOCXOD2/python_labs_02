def validate_vmestimost(vmestimost):
    """
    Валидирует вместимость транспортного средства.
    :param vmestimost: целое число, представляющее количество мест
    :raises ValueError: если вместимость меньше единицы
    """
    if vmestimost < 1:
        raise ValueError("В транспортном средстве не может быть меньше одного места")

def validate_sr_skorost(sr_skorost):
    """
    Валидирует среднюю скорость транспортного средства.
    :param sr_skorost: вещественное число, среднее значение скорости
    :raises ValueError: если скорость меньше единицы
    """
    if sr_skorost < 1:
        raise ValueError("Средняя скорость не может быть ниже 1 км/ч.")


def validate_name_type(name):
    """
    Валидирует название транспортного средства.
    Непустая строка
    :raises ValueError: если строка пустая или тип данных не строка
    """
    if type(name) != str:
        raise ValueError("Тип вводимых данных должен быть строкой")
    
def validate_name_exist(name):
    if len(name) == 0:
        raise ValueError("Название транспортного средства не может быть пустым")
    
# Логическое состояние объекта
def validate_service_level(current_level, max_level=6):
    """
    Проверяет текущий уровень обслуживания на превышение максимального предела.
    """
    if current_level >= max_level:
        raise ValueError(f"Максимальный уровень обслуживания ({max_level}) достигнут!")

def validate_fuel_amount(current_fuel, needed_fuel):
    """
    Проверяет достаточное количество топлива для поездки.
    """
    if current_fuel < needed_fuel:
        raise ValueError("Недостаточно топлива для поездки!")

def validate_positive_number(value):
    """
    Проверяет, что значение положительно и ненулевое.
    """
    if value <= 0:
        raise ValueError("Значение должно быть положительным!")

def validate_active_state(active_status):
    """
    Проверяет активное состояние объекта.
    """
    if not active_status:
        raise ValueError("Объект не активирован!")

def validate_fuel_limit(new_fuel, tank_capacity=100):
    """
    Проверяет заправку топлива относительно ёмкости бензобака.
    """
    if new_fuel > tank_capacity:
        raise ValueError(f"Превышен максимальный объем бака ({tank_capacity} литров)!")
