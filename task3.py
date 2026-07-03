def display_menu():
    print("==========================================")
    print("CLASSROOM ATTENDANCE ANALYTICS SYSTEM")
    print("==========================================")
    print("1. Record Attendance")
    print("2. View Attendance Summary")
    print("3. Exit")
def main():
    
    while True:
        display_menu()
        choice = input("choose option")
        if choice == "1":
         print("Record Attendance ")
         name,subject,total_students = get_class_information()
         record_attendance(total_students)
        elif choice == "2":
         print("View Attendance Summary ")
        elif choice == "3":
         print("exist")
         break
def get_class_information():
 name = input("enter Class Name: ")
 subject =  input("enter subject Name: ")
 total_students = int(input("enter Total Students "))
 return name,subject,total_students

#def record_attendance(total_students):

    #for student in range(1, total_students + 1):
        #status = input(f"Student {student}: ")
        #part 3 but for part4 
def record_attendance(total_students):

        present = 0
        absent = 0

        for student in range(1, total_students + 1):

         while True:
            status = input(f"Student {student} (P/A): ").upper()

            if status == "P":
                present += 1
                break

            elif status == "A":
                absent += 1
                break

            else:
                print("Invalid Attendance Status.")
                print("Please Enter Again.")
                continue
         return present, absent
main()

