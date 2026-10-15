from unittest import TestCase, main
from students.college import College
from students.student import Student


class TestCollege(TestCase):
    def setUp(self):
        self.college = College()
        self.alice = Student(id=1, name="Alice", score=85)
        self.bob = Student(id=2, name="Bob", score=90)
        self.charlie = Student(id=3, name="Charlie", score=75)
        self.david = Student(id=4, name="David", score=91)

    def add_sample_students(self):
        self.college.add_student(self.alice)
        self.college.add_student(self.bob)
        self.college.add_student(self.charlie)
        self.college.add_student(self.david)

    def test_empty_college_returns_empty_lists(self):
        self.assertListEqual(self.college.get_students_by_id(), [])
        self.assertListEqual(self.college.get_students_by_score(), [])
        self.assertListEqual(self.college.get_students_by_scores_between(0, 100), [])

    def test_add_student(self):
        self.college.add_student(self.alice)

        self.assertListEqual(self.college.get_students_by_id(), [self.alice])
        self.assertListEqual(self.college.get_students_by_score(), [self.alice])

    def test_add_multiple_students_are_sorted_by_id(self):
        self.college.add_student(self.charlie)
        self.college.add_student(self.alice)
        self.college.add_student(self.david)
        self.college.add_student(self.bob)

        self.assertListEqual(
            self.college.get_students_by_id(),
            [self.alice, self.bob, self.charlie, self.david],
        )

    def test_get_students_by_score_returns_students_sorted_by_score(self):
        self.add_sample_students()

        self.assertListEqual(
            self.college.get_students_by_score(),
            [self.charlie, self.alice, self.bob, self.david],
        )

    def test_students_with_same_score_are_handled_correctly(self):
        eve = Student(id=5, name="Eve", score=85)
        self.college.add_student(self.alice)
        self.college.add_student(eve)

        self.assertListEqual(
            self.college.get_students_by_score(),
            [self.alice, eve]
        )

    def test_add_duplicate_student_raises_value_error(self):
        self.college.add_student(self.alice)

        with self.assertRaises(ValueError) as context:
            self.college.add_student(Student(id=1, name="Another Alice", score=100))

        self.assertEqual(str(context.exception), "Student with id 1 already exists")


    def test_remove_student(self):
        self.add_sample_students()

        self.college.remove_student(self.bob)

        self.assertListEqual(
            self.college.get_students_by_id(),
            [self.alice, self.charlie, self.david],
        )
        self.assertListEqual(
            self.college.get_students_by_score(),
            [self.charlie, self.alice, self.david],
        )

    def test_remove_missing_student_raises_value_error(self):
        missing_student = Student(id=99, name="Missing", score=50)

        with self.assertRaises(ValueError) as context:
            self.college.remove_student(missing_student)

        self.assertEqual(str(context.exception), "Student with id 99 does not exist")


    def test_get_students_by_scores_between(self):
        self.add_sample_students()

        result = self.college.get_students_by_scores_between(80, 90)

        self.assertListEqual(result, ["Alice", "Bob"])

    def test_get_students_by_scores_between_includes_bounds(self):
        self.add_sample_students()

        result = self.college.get_students_by_scores_between(75, 91)

        self.assertListEqual(result, ["Charlie", "Alice", "Bob", "David"])

    def test_get_students_by_scores_between_single_exact_score(self):
        self.add_sample_students()

        result = self.college.get_students_by_scores_between(85, 85)

        self.assertListEqual(result, ["Alice"])

    def test_get_students_by_scores_between_returns_empty_list_when_no_matches(self):
        self.add_sample_students()

        result = self.college.get_students_by_scores_between(95, 100)

        self.assertListEqual(result, [])

    def test_get_students_by_scores_between_invalid_range_returns_empty(self):
        self.add_sample_students()

        result = self.college.get_students_by_scores_between(90, 80)

        self.assertListEqual(result, [])

    def test_get_students_by_scores_between_excludes_removed_student(self):
        self.add_sample_students()
        self.college.remove_student(self.alice)

        result = self.college.get_students_by_scores_between(80, 90)

        self.assertListEqual(result, ["Bob"])


if __name__ == "__main__":
    main()