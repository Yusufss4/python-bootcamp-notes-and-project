import register_system as rg


def print_menu():
    print("1. Add Course")
    print("2. Add Student to Course")
    print("3. Add Grade to Students")
    print("4. Calculate Grades for a Course")
    print("5. Populate Example Data (Debug)")


def add_course_menu(course_list):
    course_name = input('Enter the name for the course: ')
    course_max_students = int(input('Enter the max students for the course:'))
    course = rg.Lesson(course_name, max_students=course_max_students)
    course_list.add_course_to_list(course)


def add_student_to_course_menu(course_list, student_list):
    course_name = input("Enter the name of the course: ")
    course_found = course_list.search_course_by_name(course_name)


    option_for_existing_student = input("Do you want to add existing student? Y/N")
    if option_for_existing_student == 'Y' or option_for_existing_student == 'y':
        student_name = input("Enter the name of the student: ")
        student_surname = input("Enter the surname of the student: ")
        student = student_list.search_student_by_name(student_name,student_surname)
    else:
        print("Creating new student.")
        student_name = input("Enter the name of the student: ")
        student_surname = input("Enter the surname of the student: ")
        student = rg.Student(student_name, student_surname)
        student_list.add_student_to_list(student)

    course_found.add_student_to_lesson(student)
    print(f"Student: {student.student_id } is assigned to the course: {course_name}.")

    course_found.describe()
    student.describe()


def add_grades_to_students_menu():

    course_name = input("Enter the name of the course: ")
    course_found = course_list.search_course_by_name(course_name)

    while True:
        student_name = input("Enter the name of the student: ")
        student_surname = input("Enter the surname of the student: ")
        student = student_list.search_student_by_name(student_name, student_surname)

        student_grade = input("Enter the grade of the student: ")
        course_found.add_grade_to_student(student,student_grade)
        option_for_more_students = input("Dou want to continue: Y/N ")

        if option_for_more_students == "N":
            break
            return
        else:
            continue


def calculate_grades_for_course():
    course_name = input("Enter the name of the course: ")
    course_found = course_list.search_course_by_name(course_name)

    course_found.calculate_grade(calculation_type="manual")
    course_found.export_excel_file()
    course_found.describe()


def populate_example_data():

    s1 = rg.Student("Yusuf", "Savas")
    s2 = rg.Student("Mehmet", "Yılmaz")
    s3 = rg.Student("Ayşe", "Demir")
    s4 = rg.Student("John", "Rave", 101) # Custom ID for a student.

    course1 = rg.Lesson("Math", max_students=30) # Creating a lesson.
    course1.add_student_to_lesson(s1)
    course1.add_student_to_lesson(s2)
    course1.add_student_to_lesson(s3)


    course1.add_grade_to_student(s1, 60)
    course1.add_grade_to_student(s2, 20)
    course1.add_grade_to_student(s3, 50)

    course1.CalculationGrades.return_current_grades()
    course1.calculate_grade("manual")

    course2 = rg.Lesson("Art", max_students=5)
    course2.add_student_to_lesson(s3)
    course2.add_student_to_lesson(s4)

    course2.add_grade_to_student(s3, 10)
    course2.add_grade_to_student(s4, 50)
    course2.calculate_grade("manual")

    course1.describe()
    course2.describe()

    course1.export_excel_file()
    course2.export_excel_file()
    pass


if __name__ == '__main__':

    course_list = rg.CourseList("UniversityList")
    student_list = rg.StudentList("UniversityList")

    input_menu = 0
    while input_menu != "exit":
        print_menu()
        input_menu = input('Menu Option:')
        if input_menu == "1":
            add_course_menu(course_list)
        elif input_menu == "2":
            add_student_to_course_menu(course_list, student_list)
        elif input_menu == "3":
            add_grades_to_students_menu()
        elif input_menu == "4":
            calculate_grades_for_course()
        elif input_menu == "5":
            populate_example_data()


"""
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
        """
