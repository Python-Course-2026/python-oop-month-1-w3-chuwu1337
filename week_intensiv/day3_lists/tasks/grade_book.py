class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self): self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        if not self.students:
            return None
        best_student
        best_avg = 0
        for name, grade in self.students.items():
            avg = sum(grade.values()) / len(grade)
            if avg > best_avg:
                best_avg = avg
                best_student = name
            return best_student