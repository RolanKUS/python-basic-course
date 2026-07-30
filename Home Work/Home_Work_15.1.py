class LimitError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f"Gender: {self.gender}, Age: {self.age}, "
                f"Name: {self.first_name} {self.last_name}")


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"{super().__str__()}, "
                f"Record book: {self.record_book}")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise LimitError(
                "It is not possible to add more than 10 students to the group."
            )
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')
students = [
    Student('Male', 20, 'Ivan', 'Petrenko', 'AN101'),
    Student('Female', 21, 'Anna', 'Koval', 'AN102'),
    Student('Male', 22, 'Oleh', 'Shevchenko', 'AN103'),
    Student('Female', 23, 'Maria', 'Bondar', 'AN104'),
    Student('Male', 24, 'Andrii', 'Melnyk', 'AN105'),
    Student('Female', 20, 'Olena', 'Tkachenko', 'AN106'),
    Student('Male', 21, 'Maksym', 'Boyko', 'AN107'),
    Student('Female', 22, 'Sofia', 'Kravets', 'AN108'),
    Student('Male', 23, 'Dmytro', 'Kovalchuk', 'AN109'),
    Student('Female', 24, 'Natalia', 'Moroz', 'AN110')
]

for student in students:
    gr.add_student(student)

print(gr)

print("\nNumber of students:", len(gr.group))

try:
    st11 = Student('Male', 25, 'Steve', 'Jobs', 'AN111')
    gr.add_student(st11)

except LimitError as e:
    print("\nException:")
    print(e)