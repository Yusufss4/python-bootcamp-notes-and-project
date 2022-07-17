import register_system as rg


def print_menu():
    pass

if __name__ == '__main__':
    s1 = rg.Student("Yusuf", "Savas")
    s2 = rg.Student("Mehmet", "Yılmaz")
    s3 = rg.Student("Ayşe", "Demir")
    s4 = rg.Student("John", "Rave", 101)

    course1 = rg.Lesson("Math", max_students=30)
    course1.add_student_to_lesson(s1)
    course1.add_student_to_lesson(s2)
    course1.add_student_to_lesson(s3)

    course2 = rg.Lesson("Art", max_students=5)
    course2.add_student_to_lesson(s3)
    course2.add_student_to_lesson(s4)

    course1.add_grade_to_student(s1, 60)
    course1.add_grade_to_student(s2, 20)

    course1.CalculationGrades.return_current_grades()
    course1.calculate_grade("manual")

    course1.describe()
    # course2.describe()

    course1.export_excel_file()