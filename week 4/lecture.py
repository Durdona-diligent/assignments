class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} (age {self.age})'
    def introduce(self):
        print(f'Hi, I am {self.name}')
class Subject:
    def __init__(self, name, teacher_name):
        self.name = name
        self.teacher_name = teacher_name
    def __str__(self):
        return f'{self.name} (by {self.teacher_name})'
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.subjects = []
    def introduce(self):
        super().introduce()
        print(f'My student ID is {self.student_id}')
    def add_subject(self, subject):
        if not isinstance(subject, Subject):
            return NotImplemented
        self.subjects.append(subject)
    def show_subjects(self):
        print(f'Subjects of {self.name}')
        for subject in self.subjects:
            print(f'-{subject.name} (by {subject.teacher_name})')
class GradStudent(Student):
    def __init__( )