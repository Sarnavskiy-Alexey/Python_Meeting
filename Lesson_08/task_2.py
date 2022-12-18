"""
File with task 2
"""

from random import randint

names = ["Алексей", "Борис", "Владимир", "Григорий", "Александр", "Дмитрий", "Михаил", "Сэм", "Дин", "Роберт", "Алекс", "Марти", "Мэлман", "Глория"]
last_names = ["Антонов", "Яковлев", "Суворов", "Кутузов", "Сухой", "Скайуокер", "Соло", "Уинду", "Петров", "Сидоров", "Иванов"]
groups = ["Python", "C++"]


class Student:
    def __init__(self, name: str, group: str, progress: list[int]):
        self.name = name
        self.group = group
        self.progress = progress

    def __str__(self) -> str:
        return self.name + ' | ' + self.group + ' | ' + str(self.progress)

    def average_marks(self) -> float:
        return sum(self.progress) / len(self.progress)


class Faculty:
    def __init__(self, quantity=1):
        self.quantity = quantity
        self.students = []
        for _ in range(self.quantity):
            student_name = ' '.join([names[randint(0, len(names) - 1)],
                                     last_names[randint(0, len(last_names) - 1)]])
            student_group = groups[randint(0, len(groups) - 1)]
            student_progress = [randint(2, 5) for _ in range(randint(5, 10))]
            self.students += [Student(student_name, student_group, student_progress)]

    def sort_by_names(self, reverse=False):
        self.students.sort(reverse=reverse, key=lambda x : x.name)

    def sort_by_groups(self, reverse=False):
        self.students.sort(reverse=reverse, key=lambda x : x.group)

    def sort_by_progresses(self, reverse=False):
        self.students.sort(reverse=reverse, key=lambda x : sum(x.progress) / len(x.progress))

    def print_all_students(self):
        for student in self.students:
            print(student)
        print()

    def print_bad_people(self) -> None:
        for student in self.students:
            if 2 in student.progress or student.average_marks() <= 3.5:
                print(student)
        print()

    def add_student(self, student: Student) -> None:
        self.students += [student]


if __name__ == '__main__':
    faculty = Faculty(5)
    faculty.print_all_students()
    faculty.print_bad_people()
    # new_student = Student('Антуан де-Сент Экзюпери', 'Проза', [5, 4, 4, 5, 4, 5])
    # faculty.add_student(new_student)
    # faculty.print_all_students()
    # faculty.print_bad_people()
    # faculty.sort_by_names()
    # faculty.print_all_students()
    # faculty.sort_by_names(True)
    # faculty.print_all_students()
    # faculty.sort_by_groups()
    # faculty.print_all_students()
    # faculty.sort_by_groups(True)
    # faculty.print_all_students()
    # faculty.sort_by_progresses()
    # faculty.print_all_students()
    # faculty.sort_by_progresses(True)
    # faculty.print_all_students()
