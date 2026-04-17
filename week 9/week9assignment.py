from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    student_id: str
    assignments_done: int = 0
    scores: list = field(default_factory=list)

    def submit(self, score: int):
        self.assignments_done += 1
        self.scores.append(score)

    def avg_score(self) -> float:
        if self.scores:  
            return sum(self.scores) / len(self.scores)
        return 0.0

@dataclass
class Course:
    course_name: str
    professor: str
    capacity: int
    students: list[Student] = field(default_factory=list)
    enrolled: int = field(init=False, default=0)

    def enroll(self, student: Student) -> bool:
        if self.enrolled < self.capacity:
            self.students.append(student)
            self.enrolled += 1
            return True
        return False
    
    def top_student(self) -> str:
        if not self.students:
            return "No data"
        best = self.students[0]
        for s in self.students:
            if s.avg_score() > best.avg_score():
                best = s
        if best.avg_score() == 0:
            return "No data"
        return best.name

    def course_stats(self) -> str:
        header = f"{self.course_name} ({self.professor}):\n"
        body = ""
        for s in self.students:
            avg = s.avg_score()
            body = body + f"  {s.name} - {s.assignments_done} assignments, avg {avg:.1f} pts\n"
        footer = f"Enrolled: {self.enrolled}/{self.capacity}"
        return header + body + footer

s1 = Student("Liam", "S101")
s2 = Student("Nora", "S102")
s3 = Student("Omar", "S103")

s1.submit(72)
s1.submit(88)
s1.submit(91)
s2.submit(95)
s2.submit(89)
s3.submit(60)

c = Course("Data Structures", "Prof. Kim", 3)
print(c.enroll(s1))
print(c.enroll(s2))
print(c.enroll(s3))
print(c.enroll(Student("Priya", "S104")))
print(c.enrolled)
print(c.top_student())
print(c.course_stats())
