class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def __repr__(self):
        return f"Student(name={self.name!r}, student_id={self.student_id!r}, gpa={self.gpa!r})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.name == other.name and 
                self.student_id == other.student_id and 
                self.gpa == other.gpa)

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    student_id: str
    gpa: float

s1 = Student("Alisher", "2024001", 3.8)
s2 = Student("Alisher", "2024001", 3.8)

print(s1)          # Student(name='Alisher', student_id='2024001', gpa=3.8)
print(s1 == s2)    # True
