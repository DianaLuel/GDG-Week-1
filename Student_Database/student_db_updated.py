student_database = {}

def print_updated_list():
    print("--- The updated list ---")
    for key, value in student_database.items():
        print(f"ID: {key}")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key.capitalize()}: {sub_value}")
    if not student_database:
        print("The database is empty.")

def menu():
    menu_list = """
    Welcome to ATR's Student Database!!!
    ---------------------------
    |    1. Add Student       |
    |    2. View Student      |
    |    3. List All Students | 
    |    4. Update Student    |
    |    5. Delete Student    |
    |    6. Delete All List   |
    |    7. Exit              |
    ---------------------------
    """
    print(menu_list)
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Enter a valid number.")

def add_student():
    ID = input("Enter ID of the student: ")
    if ID in student_database:
        print(f"Student with ID {ID} already exists.")
        return

    fname = input("Enter First name of the student: ")
    lname = input("Enter Last name of the student: ")
    
    try:
        age = int(input("Enter Age of the student: "))
    except ValueError:
        print("Age must be a number.")
        return

    gender = input("Enter Gender of the student (M/F): ").upper()
    if gender not in ['M', 'F']:
        print("Invalid gender. Enter 'M' or 'F'.")
        return

    grade = input("Enter Grade of the student (A/B/C/...): ").upper()
    if grade not in ['A', 'B', 'C', 'D', 'F']:
        print("Enter a valid grade.")
        return

    student_database[ID] = {
        "fname": fname,
        "lname": lname,
        "age": age,
        "gender": gender,
        "grade": grade
    }
    print("Student added successfully!")
    print_updated_list()

def view_student():
    search_id = input("Enter the ID of the student you want to view: ")
    if search_id in student_database:
        print(f"Details for Student ID {search_id}:")
        for key, value in student_database[search_id].items():
            print(f"  {key.capitalize()}: {value}")
    else:
        print(f"Student ID {search_id} not found.")

def list_student():
    print_updated_list()

def update_student():
    search_id = input("Enter the ID of the student you want to update: ")
    if search_id not in student_database:
        print(f"Student ID {search_id} not found.")
        return

    update_menu = """
    What do you want to update?
    ----------------------
    |    1. First Name   |
    |    2. Last Name    |
    |    3. Age          |
    |    4. Gender       |
    |    5. Grade        |
    |    6. Back to menu |
    ----------------------
    """
    print(update_menu)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        student_database[search_id]["fname"] = input("Enter new First Name: ")
    elif choice == 2:
        student_database[search_id]["lname"] = input("Enter new Last Name: ")
    elif choice == 3:
        try:
            student_database[search_id]["age"] = int(input("Enter new Age: "))
        except ValueError:
            print("Age must be a number.")
            return
    elif choice == 4:
        gender = input("Enter new Gender (M/F): ").upper()
        if gender in ['M', 'F']:
            student_database[search_id]["gender"] = gender
        else:
            print("Invalid gender. Enter 'M' or 'F'.")
            return
    elif choice == 5:
        grade = input("Enter new Grade: ").upper()
        if grade in ['A', 'B', 'C', 'D', 'F']:
            student_database[search_id]["grade"] = grade
        else:
            print("Enter a valid Grade.")
            return
    elif choice == 6:
        return
    else:
        print("Invalid choice.")
        return

    print("Student updated successfully!")
    print_updated_list()

def delete_student():
    search_id = input("Enter the ID of the student you want to delete: ")
    if search_id in student_database:
        del student_database[search_id]
        print(f"Student with ID {search_id} deleted successfully.")
    else:
        print(f"Student ID {search_id} not found.")
        return
    print_updated_list()

def delete_all():
    student_database.clear()
    print("All students deleted successfully.")
    print_updated_list()

def main():
    while True:
        choice = menu()
        match choice:
            case 1:
                add_student()
            case 2:
                view_student()
            case 3:
                list_student()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                delete_all()
            case 7:
                print("Bye bye :)\n")
                exit()
            case _:
                print("Enter numbers only from the above menu.")

if __name__ == "__main__":
    main()
