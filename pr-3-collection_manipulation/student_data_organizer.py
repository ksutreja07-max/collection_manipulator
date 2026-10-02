student_data = []

print("Welcome to Student data organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display all Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\nChoose an choice: "))

    if choice == 1:
        print("\nEnter Student Information")

        student_id = int(input("student ID: "))
        student_name = input("student Name: ")
        student_age = int(input("student Age: "))
        student_grade = input("student Grade: ")
        student_dob = input("date of Birth: ")
        subjects = input("enter subjects separated by comma: ")

        subject_list = {item.strip() for item in subjects.split(",") if item.strip()}

        record = {
            "id": (student_id,),
            "name": student_name,
            "age": student_age,
            "grade": student_grade,
            "dob": (student_dob,),
            "subject": subject_list
        }

        student_data.append(record)

        print(f"\nRecord of {student_name} added successfully!")

    elif choice == 2:

        if len(student_data) == 0:
            print("no student records available.")
        else:
            print("\n===== STUDENT RECORDS =====")

            for record in student_data:
                print(
                    f"ID: {record['id']} | "
                    f"name: {record['name']} | "
                    f"age: {record['age']} | "
                    f"grade: {record['grade']} | "
                    f"subjects: {record['subject']}"
                )

    elif choice == 3:

        student_id = int(input("Enter ID of student to modify: "))
        found = False

        for record in student_data:

            if (student_id,) == record["id"]:

                record["age"] = input("Enter updated age: ")
                record["subject"] = input("enter updated subjects: ")

                print(f"student ID {record['id']} details updated!")
                found = True
                break

        if found == False:
            print("No student found with this ID.")

    elif choice == 4:

        student_id = int(input("enter id of student to remove: "))
        found = False

        for index in range(len(student_data)):

            if student_data[index]["id"] == (student_id,):

                del student_data[index]

                print("Student record removed successfully!")
                found = True
                break

        if found == False:
            print("Student record not found.")

    elif choice == 5:

        print("\n===== Subject Offered =====")

        for record in student_data:
            print(record["subject"])

    elif choice == 6:

        print("thank you for using Student Record Management!")
        break

    else:
        print("Please enter a valid option.")


