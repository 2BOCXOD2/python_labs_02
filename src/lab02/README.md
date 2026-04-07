# Задание на 3

## Cоздание нескольких объектов
### Создаем несколько автомобилей
car1 = Car("Lada", 5, 120.5, "Vesta")
car2 = Car("Toyota", 5, 180.0, "Camry")
### Добавляем их в автопарк
fleet.add(car1)
fleet.add(car2)
### Результат через len:
![01](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Список через get_all:
![02](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Вывод всех элементов через for:
![03](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Удаление элемента:
![04](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Повторный вывод  после удаления:
![05](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

# Задание на 4
## Пересоздадим автопарк для чистоты эксперимента
### fleet = Fleet()
### car1 = Car("Lada", 5, 120.5, "Vesta")
### car2 = Car("Toyota", 5, 180.0, "Camry")
### fleet.add(car1)
### fleet.add(car2)
### Автомобили успешно добавлены, но при создании дубликата (duplicate_car = Car("Lada", 4, 150, "Granta")) вызывается ошибка:
![06](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Дальше идёт проверка на уникальность ID:
![07](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

### Далее демонстрируется поиск среди объектов на автостоянке (found_car = fleet.find_by_name("Toyota")):
![08](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

# Задание на 5
## Создаём новую автостоянку:
### fleet = Fleet()
### car1 = Car("Lada", 5, 120.5, "Vesta", price=800_000)
### car2 = Car("Toyota", 5, 180.0, "Camry", price=2_500_000)
### car3 = Car("Kia", 5, 150.0, "Rio", price=1_500_000)

## Проверяем индексацию:
![09](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

## Удаление по индексу:
![10](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

## Сортировка
### fleet = Fleet()
### fleet.add(Car("Ford", 5, 170, "Focus", price=1_600_000))
### fleet.add(Car("BMW", 4, 220, "3 Series", price=3_500_000))
### fleet.add(Car("Audi", 5, 210, "A4", price=3_200_000))
## До сортировки по цене:
![11](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)
## После сортировке по цене:
![12](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)
## Универсальная сортировка по имени (Z-A):
![13](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)

## Фильтрация
### fleet = Fleet()
### fleet.add(Car("Lanos", 5, 100, "Cheap", price=300_000))
### fleet.add(Car("Mazda", 5, 180, "6", price=2_200_000))
### fleet.add(Car("Tesla", 5, 200, "Model S", price=12_000_000))
## Исходная коллекция:
![14](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)
## Отфильтрованная коллекция (авто дороже 2 млн руб.):
![15](https://github.com/2BOCXOD2/python_labs_02/blob/main/images/lab01/01%20Создание%20и%20описание.PNG)





Ключевые моменты реализации
Хранение данных: объекты хранятся во внутреннем списке self._items, как и требовалось.
Типизация: метод add(item) строго проверяет тип добавляемого объекта с помощью isinstance(item, Car). Это гарантирует, что коллекция будет содержать только автомобили.
Управление коллекцией: Реализованы методы add(), remove() и get_all() для полного контроля над содержимым.
Итерируемость: класс реализует магический метод __iter__(). Это позволяет перебирать элементы коллекции в цикле for без необходимости вручную вызывать get_all().
Удобство: добавлен метод __len__(), который позволяет использовать стандартную функцию len() для получения размера коллекции.



add(): перед добавлением проверяет, нет ли уже машины с таким же id или name. Если есть — выбрасывает понятную ошибку.
find_by_name() и find_by_id(): позволяют легко найти нужный автомобиль в большой коллекции.
len(fleet): работает благодаря методу __len__.
for car in fleet: работает благодаря методу __iter__.