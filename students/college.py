from sortedcontainers import SortedSet, SortedKeyList

class College:
    def __init__(self):
        self._students = SortedSet()
        self._students_by_score = SortedKeyList(key=lambda s: s.score)

    def add_student(self, student):
        if student in self._students:
            raise ValueError(f"Student with id {student.id} already exists")
        self._students.add(student)
        self._students_by_score.add(student)

    def remove_student(self, student):
        if student not in self._students:
            raise ValueError(f"Student with id {student.id} does not exist")
        self._students.remove(student)
        self._students_by_score.remove(student)
        
    def get_students_by_id(self):
        return list(self._students)

    def get_students_by_score(self):
        return list(self._students_by_score)

    def get_students_by_scores_between(self, min_score, max_score):
        return [student.name for student in self._students_by_score.irange_key(min_score, max_score)]
