class Lesson:
    def __init__(self, name, course_id, max_students):
        self.name = name
        self.course_id = course_id
        self.max_students = max_students
        self.students = []  # Empty lists for the students.

    def add_student_to_lesson(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            student.register_lesson_to_student(self.course_id)
            return True
        return False

    def add_grade_to_student(self, student, point):
        if student in self.students:
            index = 0
            course_found = 0
            for course_info in student.lessons_registered:
                if course_info[0] == self.course_id:
                    student.lessons_registered[index][1] = point
                    course_found = 1
            index += 1
            if course_found == 0:
                print(f"The lesson is not assigned to the student with ID of {student.student_id}")
        else:
            print(f"Could not find the student with ID of {student.student_id}")

    def describe(self):
        print(f"\nCourse name: {self.name}")
        print(f"Course ID: {self.course_id}")
        print(f"Max Students: {self.max_students}")
        print(f"Students are assigned:")
        for i in range(len(self.students)):
            (self.students[i]).describe()


    def calculate_grade(self, calculation_type="catalog"):  # return a dataframe that consist of IDs and Passed/Non-Passed
        pass


class CalculationGrades:
    AA = 90
    BA = 80
    BB = 70
    CB = 65
    CC = 60
    DC = 55
    DD = 50
    FD = 40
    FF = 35
    GR = "GR"

    @classmethod  # Class methods are spesific to classes.
    def change_calculation_grades(cls):
        pass

    @classmethod  # Class methods are spesific to classes.
    def return_current_grades(cls):
        pass


class Student:
    def __init__(self, name, surname, student_id):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.lessons_registered = []
        self.number_of_lessons_registered = 0

    def describe(self,with_lessons=False):
        self.number_of_lessons_registered = len(self.lessons_registered)
        print(f"{self.name} {self.surname} - Student ID: {self.student_id} Reg Lessons: {self.number_of_lessons_registered}")
        if with_lessons == True:
            for i in range(self.number_of_lessons_registered):
                print(f"Lesson ID: {self.lessons_registered[i][0]} Point: {self.lessons_registered[i][1]}")

    def register_lesson_to_student(self, course_id):
        self.lessons_registered.append([course_id, None])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = Student("Yusuf", "Savas", 1)
    s2 = Student("Mehmet", "Yılmaz", 2)
    s3 = Student("Ayşe", "Demir", 3)
    s4 = Student("John", "Rave", 4)

    course1 = Lesson("Math", 1, 30)
    course1.add_student_to_lesson(s1)
    course1.add_student_to_lesson(s2)
    course1.add_student_to_lesson(s3)

    course2 = Lesson("Art", 2, 5)
    course2.add_student_to_lesson(s3)
    course2.add_student_to_lesson(s4)

    course1.add_grade_to_student(s1, 10)
    course1.add_grade_to_student(s2, 10)

    CalculationGrades.return_current_grades()
    course1.calculate_grade()

    course1.describe()
    course2.describe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
