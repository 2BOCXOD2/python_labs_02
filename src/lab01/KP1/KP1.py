"""
MRO (Method Resolution Order) — это последовательность, в которой питон ищет методы и атрибуты когда класс наследуется.
Например, метод может быть в нескольких родительских классах и питон будет искать методы и атрибуты в определённом порядке.
Он проверяет каждый класс только один раз.
Сначала всегда идёт класс а потом родители.
Поядок проверки родительских классов берётся из того, в какой последовательности они записаны в классе 
(типа class Class3(Class1, Class2) сначала проверится класс 1, а потом класс 2).

"""

class Student:
    def __init__(self, name: str, gpa: float):
        self._name = name
        self._gpa = gpa

    @property
    def gpa(self):
        return self._gpa

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"{self._name} (GPA: {self._gpa})"


class StudentGroup:
    def __init__(self):
        self._items = []

    def add(self, student):
        if isinstance(student, Student) == False:
            raise TypeError("Можно добавлять только экземпляры класса Student")
        self._items.append(student)

    def get_all(self):
        return list(self._items)

    def get_top_students(self, min_gpa: int):
        horoshie_studenty = []
        for student in self._items:
            if student.gpa >= min_gpa:
                horoshie_studenty.append(student)
        return horoshie_studenty
    


"""
group = StudentGroup()
group.add(Student("Иван", 4))
group.add(Student("Мария", 3))
group.add(Student("Алексей", 5))

top_students = group.get_top_students(4)
for s in top_students:
    print(s)
"""