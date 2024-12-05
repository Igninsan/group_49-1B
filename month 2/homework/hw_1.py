class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Имя - {self.full_name}, Возраст - {self.age} лет, Женат/Замужем - {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks: dict):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def count_average_mark(self):
        average_mark = sum(self.marks.values()) / len(self.marks)
        print(f'Средняя оценка = {average_mark}')

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def count_salary(self):
        salary = Teacher.base_salary
        if self.experience > 3:
            for _ in range(self.experience - 3):
                salary += salary * 0.05

        print(f'Зарплата = {salary}')

Anna = Teacher('Анна Викторовна', 30, 'Нет', 5)
Anna.introduce_myself()
print(f'Опыт работы: {Anna.experience} лет')
Anna.count_salary()

def create_students():
    students_list = []
    first_student = Student('Денис', 19, 'Нет',
    {'Математика' : 3, 'Русский язык': 5, 'Английский язык': 3, 'История': 5})
    second_student = Student('Кирилл', 20, 'Нет',
    {'Математика' : 4, 'Русский язык': 3, 'Английский язык': 4, 'История': 3, 'Химия': 4})
    third_student = Student('Артём', 25, 'Да',
    {'Математика': 5, 'Русский язык': 4, 'Английский язык': 4, 'История': 4, 'Физика': 4, 'Психология': 3})

    students_list.extend([first_student, second_student, third_student])
    return students_list

new_students = create_students()

for student in new_students:
    print()
    student.introduce_myself()
    print(f'Предметы и оценки по ним: {student.marks}')
    student.count_average_mark()

