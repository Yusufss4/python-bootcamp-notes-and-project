import pandas as pd
import numpy as np
from datetime import date


class Lesson:
    course_id_counter = 101

    def __init__(self, name, course_id=False, max_students=10):
        self.name = name
        self.course_id = course_id
        if not course_id:
            self.course_id = Lesson.increase_course_id()
        else:
            self.course_id = course_id  # Check if the student id is on the use.
        self.max_students = max_students
        self.students = []  # Empty lists for the students.

    @classmethod
    def increase_course_id(cls):
        cls.course_id_counter = cls.course_id_counter + 1
        return cls.course_id_counter

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
            (self.students[i]).describe(True)

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

        @classmethod  # Class methods are specific to classes.
        def change_calculation_grades_manually(cls):
            pass

        @classmethod  # Class methods are specific to classes.
        def return_current_grades(cls):
            pass

    def calculate_grade(self,
                        calculation_type="catalog"):  # return a dataframe that consist of IDs and Passed/Non-Passed
        if calculation_type == "catalog":
            pass
        elif calculation_type == "manual":
            for student in self.students:
                index = 0
                course_found = 0
                for course_info in student.lessons_registered:
                    if course_info[0] == self.course_id:
                        students_point = student.lessons_registered[index][1]
                        course_found = 1
                        if students_point is None:
                            grade = "GZ"
                            # If the calculate is called and students mark is None it means that person
                            # doesn't enter the exam.
                        elif students_point > Lesson.CalculationGrades.AA:
                            grade = "AA"
                        elif students_point > Lesson.CalculationGrades.BA:
                            grade = "BA"
                        elif students_point > Lesson.CalculationGrades.BB:
                            grade = "BB"
                        elif students_point > Lesson.CalculationGrades.CB:
                            grade = "CB"
                        elif students_point > Lesson.CalculationGrades.CC:
                            grade = "CC"
                        elif students_point > Lesson.CalculationGrades.DC:
                            grade = "DC"
                        elif students_point > Lesson.CalculationGrades.DD:
                            grade = "DD"
                        elif students_point > Lesson.CalculationGrades.FD:
                            grade = "FD"
                        elif students_point > Lesson.CalculationGrades.FF:
                            grade = "FF"
                        elif students_point >= 0:
                            grade = "FF"
                        elif students_point == Lesson.CalculationGrades.GR:
                            grade = "GR"
                        else:
                            grade = None

                        student.lessons_registered[index][2] = grade
                        index += 1

                if course_found == 0:
                    print(f"The lesson is not assigned to the student with ID of {student.student_id}")

    def export_excel_file(self):
        # columns = ['Student ID', 'Student Name', 'Student Grade', 'Passed or Not']
        data = pd.DataFrame()
        for student in self.students:
            index = 0
            for course_info in student.lessons_registered:
                if course_info[0] == self.course_id:
                    if student.lessons_registered[index][2] != "FF" or student.lessons_registered[index][2] != "GZ":
                        is_passed = "Passed"
                    else:
                        is_passed = "Failed"

                    student_row = [[student.student_id,
                                    student.name + " " +
                                    student.surname,
                                    student.lessons_registered[index][1],
                                    student.lessons_registered[index][2],
                                    is_passed]]
                    data_students = pd.DataFrame(student_row, columns=['Student ID', 'Student Name', 'Student Grade',
                                                                       'Student Point', 'Status'])
                    data = pd.concat([data, data_students])
                index += 1
        data.reset_index(inplace=True, drop=True)
        print(data)

        todays_date = date.today().strftime("%d-%m-%Y")
        excel_file_name = f"{self.name}{str(self.course_id)}-{str(len(self.students))}-{todays_date}.xlsx"
        print(excel_file_name)
        try:
            data.to_excel(excel_file_name)
        except:
            print("Could not import to the excel file.")


class Student:
    student_id_counter = 0

    def __init__(self, name, surname, student_id=False):
        self.name = name
        self.surname = surname
        if not student_id:
            self.student_id = Student.increase_student_id()
        else:
            self.student_id = student_id  # Check if the student id is on the use.
        self.lessons_registered = []
        self.number_of_lessons_registered = 0

    @classmethod
    def increase_student_id(cls):
        cls.student_id_counter = cls.student_id_counter + 1
        return cls.student_id_counter

    def describe(self, with_lessons=False):
        self.number_of_lessons_registered = len(self.lessons_registered)
        print(
            f"{self.name} {self.surname} - Student ID: {self.student_id} Reg Lessons: {self.number_of_lessons_registered}")
        if with_lessons:
            for i in range(self.number_of_lessons_registered):
                print(
                    f"Lesson ID: {self.lessons_registered[i][0]} Point: {self.lessons_registered[i][1]} Grade: {self.lessons_registered[i][2]}")

    def register_lesson_to_student(self, course_id):
        self.lessons_registered.append([course_id, None, None])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
