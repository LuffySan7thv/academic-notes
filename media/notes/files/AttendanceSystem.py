import csv

class AttendanceSystem:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        self.students = []
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["absences"] = int(row["absences"])
                    self.students.append(row)
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "name", "absences"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students)

    def add_student(self, student_id, name):
        student_id = student_id.strip()
        name = name.strip()
        if not student_id or not name:
            print("[Error] ID and name cannot be empty.")
            return False
        if not student_id.isdigit():
            print("[Error] ID must contain only digits.")
            return False
        if any(s["id"] == student_id for s in self.students):
            print("[Error] Student ID already exists.")
            return False
        self.students.append({"id": student_id, "name": name, "absences": 0})
        self.save_to_file()
        print(f"[OK] Student '{name}' (ID: {student_id}) added.")
        return True

    def mark_attendance(self):
        if not self.students:
            print("[Empty] No students to mark attendance.")
            return
        print("\n--- Mark Attendance for Today's Session ---")
        for student in self.students:
            print(f"\nStudent: {student['name']} (ID: {student['id']}) - Current absences: {student['absences']}")
            while True:
                status = input("Present (p) or Absent (a)? ").strip().lower()
                if status == "p":
                    break
                elif status == "a":
                    student["absences"] += 1
                    print(f"[Alert] {student['name']} now has {student['absences']} absence(s).")
                    break
                else:
                    print("[Error] Invalid input. Enter 'p' or 'a'.")
        self.save_to_file()
        print("\n OK Attendance recorded and saved.")

    def show_absence_alerts(self, threshold=3):
        alert_list = [s for s in self.students if s["absences"] >= threshold]
        if not alert_list:
            print(f"[Info] No student has reached {threshold} absences.")
        else:
            print(f"\n Absence Alert (Threshold = {threshold})")
            for s in alert_list:
                print(f"[Alert] {s['name']} (ID: {s['id']}) has {s['absences']} absences.")

    def list_students(self):
        if not self.students:
            print("[Empty] No students in the system.")
        else:
            print("\n--- Student List ----")
            for s in self.students:
                print(f"ID: {s['id']} | Name: {s['name']} | Absences: {s['absences']}")

    def reset_absences(self, student_id):
        for s in self.students:
            if s["id"] == student_id:
                s["absences"] = 0
                self.save_to_file()
                print(f"[OK] Absences reset for {s['name']}.")
                return True
        print("[Error] Student ID not found.")
        return False

    def edit_student(self, old_id):
        old_id = old_id.strip()
        for s in self.students:
            if s["id"] == old_id:
                print(f"Editing student: {s['name']} (ID: {s['id']})")
                new_id = input("New ID (press Enter to keep unchanged): ").strip()
                new_name = input("New name (press Enter to keep unchanged):").strip()

                if new_id:
                    if not new_id.isdigit():
                        print("[Error] New ID must contain only digits.")
                        return False
                    if any(st["id"] == new_id for st in self.students):
                        print("[Error] New ID already exists.")
                        return False
                    s["id"] = new_id

                if new_name:
                    if not new_name:
                        print("Error... Name cannot be empty.")
                        return False
                    s["name"] = new_name

                self.save_to_file()
                print("[OK] Student information updated.")
                return True
        print("[Error] Student ID not found.")
        return False

def main():
    system = AttendanceSystem()

    while True:
        print("\n==== Student Attendance & Alert System =======")
        print("1. Add new student")
        print("2. Mark attendance for a session")
        print("3. Show absence alerts (>=3)")
        print("4. List all students")
        print("5. Reset absences for a student")
        print("6. Edit student information")
        print("7. Exit")
        choice = input("Choose (1-7): ").strip()

        if choice == "1":
            sid = input("Student ID:").strip()
            name = input("Full name:").strip()
            if sid and name:
                system.add_student(sid, name)
            else:
                print("[Error] ID and name cannot be empty.")

        elif choice == "2":
            system.mark_attendance()
            system.show_absence_alerts()

        elif choice == "3":
            system.show_absence_alerts()

        elif choice == "4":
            system.list_students()

        elif choice == "5":
            sid = input("Enter student ID to reset absences:").strip()
            system.reset_absences(sid)

        elif choice == "6":
            sid = input("Enter student ID to edit: ").strip()
            system.edit_student(sid)

        elif choice == "7":
            print("[Exit]")
            break

        else:
            print("Error Invalid choice")

if __name__ == "__main__":
    main()