def menu():
    print("Welcome to the School Attendance Management System!")

    print("1. Display All Students")
    print("2. Search Student")
    print("3. Mark Attendance")
    print("4. Update Attendance")
    print("5. Calculate Attendance Percentage")
    print("6. Display Attendance Status")
    print("7. Display Students Below Attendance Requirement")
    print("8. Attendance Summary")
    print("9. Exit")

    choice = int(input("Enter the number of the function you want to perform: "))

    if choice == 1:
        display_all_students()
    elif choice == 2:
        search_student()
    elif choice == 3:
        mark_attendance()
    elif choice == 4:
        update_attendance()
    elif choice == 5:
        calculate_attendance_percentage()
    elif choice == 6:
        display_attendance_status()
    elif choice == 7:
        display_students_below_requirement()
    elif choice == 8:
        attendance_summary()
    elif choice == 9:
        exit_system()
    else:
        print("Invalid choice! Please select a number from 1 to 9.")


def display_all_students():
    print("You have selected: Display All Students")


def search_student():
    print("You have selected: Search Student")


def mark_attendance():
    print("You have selected: Mark Attendance")


def update_attendance():
    print("You have selected: Update Attendance")


def calculate_attendance_percentage():
    print("You have selected: Calculate Attendance Percentage")


def display_attendance_status():
    print("You have selected: Display Attendance Status")


def display_students_below_requirement():
    print("You have selected: Display Students Below Attendance Requirement")


def attendance_summary():
    print("You have selected: Attendance Summary")


def exit_system():
    print("You have selected: Exit")


menu()