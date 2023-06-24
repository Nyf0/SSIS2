import sqlite3
import os
import msvcrt as m

# Create a connection to the database
conn = sqlite3.connect('SSIS_2.db')
print("Connected successfully!")
cursor = conn.cursor()

# Create the Students table
cursor.execute('PRAGMA foreign_keys = 1')

# For pausing the screen
def  prompt():
    print("\n\nPress Enter to continue...")
    m.getch()

# Function to create a new student
def create_student():
    os.system('cls')
    print("Enter student details:")
    name = input("\nName: ")
    gender = input("Gender: ")
    yearlevel = int(input("Year Level: "))
    course_code = input("Course Code: ")

    cursor.execute('''
        INSERT INTO Students (name, gender, yearlevel, course_code)
        VALUES (?, ?, ?, ?)
    ''', (name, gender, yearlevel, course_code))
    conn.commit()
    print("Student created successfully!")
    prompt()

# Function to read student information
def read_student():
    os.system('cls')
    ch = input("Would you like to search by name(1) or ID(2)? ")

    if ch == '1':
        student_n = input("\nEnter student name: ")
        cursor.execute('SELECT * FROM Students WHERE name = ?', (student_n,))
        student = cursor.fetchone()
        if student:
            print("\nStudent ID:", student[0])
            print("Name:", student[1])
            print("Gender:", student[2])
            print("Year Level:", student[3])
            print("Course Code:", student[4])
        else:
            print("Student not found.")
        prompt()

    elif ch == '2':
        student_id = int(input("\nEnter student ID: "))
        cursor.execute('SELECT * FROM Students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()
        if student:
            print("\nStudent ID:", student[0])
            print("Name:", student[1])
            print("Gender:", student[2])
            print("Year Level:", student[3])
            print("Course Code:", student[4])
        else:
            print("Student not found.")
        prompt()
    
    else:
        print("\nInvalid choice!")
        prompt()

# Function to update student information
def update_student():
    os.system('cls')
    student_id = int(input("Enter student ID: "))
    cursor.execute('SELECT * FROM Students WHERE student_id = ?', (student_id,))
    student = cursor.fetchone()
    if student:
        print("\nCurrent Student Details:")
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Gender:", student[2])
        print("Year Level:", student[3])
        print("Course Code:", student[4])

        print("\nEnter new student details:")
        name = input("Name: ")
        gender = input("Gender: ")
        yearlevel = int(input("Year Level: "))
        course_code = input("Course Code: ")

        cursor.execute('''
            UPDATE Students
            SET name = ?, gender = ?, yearlevel = ?, course_code = ?
            WHERE student_id = ?
        ''', (name, gender, yearlevel, course_code, student_id))
        conn.commit()
        print("\nStudent information updated successfully!")
    else:
        print("\nStudent not found.")
    prompt()

# Function to delete a student
def delete_student():
    os.system('cls')
    student_id = int(input("Enter student ID: "))
    cursor.execute('SELECT * FROM Students WHERE student_id = ?', (student_id,))
    student = cursor.fetchone()
    if student:
        confirmation = input("\nAre you sure you want to delete this student? (Y/N): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM Students WHERE student_id = ?', (student_id,))
            conn.commit()
            print("\nStudent deleted successfully!")
        else:
            print("\nDeletion canceled.")
    else:
        print("\nStudent not found.")
    prompt()

# Function to create a new course
def create_course():
    os.system('cls')
    print("Enter course details:")
    course_code = input("\nCourse Code: ")
    name = input("Course Name: ")

    cursor.execute('''
        INSERT INTO Courses (course_code, name)
        VALUES (?, ?)
    ''', (course_code, name))
    conn.commit()
    print("\nCourse created successfully!")
    prompt()

# Function to read course information
def read_course():
    os.system('cls')
    course_code = input("Enter course code: ")
    cursor.execute('SELECT * FROM Courses WHERE course_code = ?', (course_code,))
    course = cursor.fetchone()
    if course:
        print("\nCourse Code:", course[0])
        print("Course Name:", course[1])
    else:
        print("\nCourse not found.")
    prompt()

# Function to update course information
def update_course():
    os.system('cls')
    course_code = input("Enter course code: ")
    cursor.execute('SELECT * FROM Courses WHERE course_code = ?', (course_code,))
    course = cursor.fetchone()
    if course:
        print("\nCurrent Course Details:")
        print("Course Code:", course[0])
        print("Course Name:", course[1])

        print("\nEnter new course details:")
        name = input("Course Name: ")

        cursor.execute('''
            UPDATE Courses
            SET name = ?
            WHERE course_code = ?
        ''', (name, course_code))
        conn.commit()
        print("\nCourse information updated successfully!")
    else:
        print("\nCourse not found.")
    prompt()

# Function to delete a course
def delete_course():
    os.system('cls')
    course_code = input("Enter course code: ")
    cursor.execute('SELECT * FROM Courses WHERE course_code = ?', (course_code,))
    course = cursor.fetchone()
    if course:
        confirmation = input("\nAre you sure you want to delete this course? (Y/N): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM Courses WHERE course_code = ?', (course_code,))
            conn.commit()
            print("\nCourse deleted successfully!")
        else:
            print("\nDeletion canceled.")
    else:
        print("\nCourse not found.")
    prompt()

# Function to list all students
def list_students():
    os.system('cls')
    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()
    if students:
        for student in students:
            print("Student ID:", student[0])
            print("Name:", student[1])
            print("Gender:", student[2])
            print("Year Level:", student[3])
            print("Course Code:", student[4])
            print("----------------------")
    else:
        print("No students found.")
    prompt()

# Function to list all courses
def list_courses():
    os.system('cls')
    cursor.execute('SELECT * FROM Courses')
    courses = cursor.fetchall()
    if courses:
        for course in courses:
            print("Course Code:", course[0])
            print("Course Name:", course[1])
            print("----------------------")
    else:
        print("No courses found.")
    prompt()

# Main program loop
while True:
    os.system('cls')
    print("\n--- Simple Student Information System (SSIS) v2 ---")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Create Course")
    print("6. Read Course")
    print("7. Update Course")
    print("8. Delete Course")
    print("9. List Students")
    print("10. List Courses")
    print("0. Exit")
    
    choice = input("Enter your choice (0-10): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == "5":
        create_course()
    elif choice == "6":
        read_course()
    elif choice == "7":
        update_course()
    elif choice == "8":
        delete_course()
    elif choice == "9":
        list_students()
    elif choice == "10":
        list_courses()
    elif choice == "0":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please try again.")
