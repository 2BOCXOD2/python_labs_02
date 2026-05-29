class ItemNotFoundError(Exception):
    """Исключение, когда объект не найден в коллекции."""
    pass

class DuplicateItemError(Exception):
    """Исключение, когда объект с таким ID уже существует в коллекции."""
    pass

class InputError(Exception):
    """Исключение для некорректного ввода пользователя."""
    pass