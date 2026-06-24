import csv

class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def load_from_file(self):
        self.tasks = []
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.tasks = list(reader)
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "status"])
            writer.writeheader()
            writer.writerows(self.tasks)

    def add_task(self, title):
        self.tasks.append({"title": title, "status": "Pending"})
        self.save_to_file()
        print(f"[OK] Task '{title}' added.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks) and self.tasks[index]["status"] == "Pending":
            self.tasks[index]["status"] = "Done"
            self.save_to_file()
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_to_file()
            return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("[Empty] No tasks yet.")
        else:
            for i, t in enumerate(self.tasks, 1):
                status_text = "Done" if t["status"] == "Done" else "Pending"
                print(f"{i}. {t['title']} [{status_text}]")

def main():
    todo = ToDoList()
    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add task")
        print("2. Mark as completed")
        print("3. Delete task")
        print("4. List all tasks")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                todo.add_task(title)
            else:
                print("[Error] Title cannot be empty.")
        elif choice == "2":
            todo.list_tasks()
            if todo.tasks:
                try:
                    idx = int(input("Number of task to complete: ")) - 1
                    if todo.mark_completed(idx):
                        print("[OK] Task marked as done.")
                    else:
                        print("[Error] Invalid number or already completed.")
                except ValueError:
                    print("[Error] Please enter a number.")
        elif choice == "3":
            todo.list_tasks()
            if todo.tasks:
                try:
                    idx = int(input("Number of task to delete: ")) - 1
                    if todo.delete_task(idx):
                        print("[OK] Task deleted.")
                    else:
                        print("[Error] Invalid number.")
                except ValueError:
                    print("[Error] Please enter a number.")
        elif choice == "4":
            todo.list_tasks()
        elif choice == "5":
            print("[Exit] Goodbye!")
            break
        else:
            print("[Error] Invalid choice. Try again.")

if __name__ == "__main__":
    main()