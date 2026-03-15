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
