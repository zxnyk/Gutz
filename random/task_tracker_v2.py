class Task:

    def __init__(self, title):
        self.title = title
        self.done = False
    
    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "🕓"
        return f"{status} {self.title}"
    
class TaskManager:
    
    def __init__(self):
        self.tasks = []
    
    def add_tasks(self, title):
        if any(task.title.lower() == title.lower() for task in self.tasks):
            print("Task already exist")
            return
        task = Task(title)
        self.tasks.append(task)
        print(f"Added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        done  = sum(task.done for task in self.tasks)
        to_do = len(self.tasks) - done

        print(f"TOTAL TASK: {len(self.tasks)}")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}: {task}")
        print(f"✅ Done: {done} | 🕓 To Do: {to_do}")

    def remove_task(self, index):
        if not self.existing_task(index):
            return 
        task = self.tasks[index - 1].title
        self.tasks.pop(index - 1 )
        print(f"Task removed. {task}")

    def complete_task(self, index):
        if not self.existing_task(index):
            return 
        task = self.tasks[index - 1].title
        self.tasks[index - 1].mark_done()
        print(f"Task completed. {task}")

    def existing_task(self, index):
        if index < 1 or index > len(self.tasks):
            print(f"Task does not exist. Try again.")
            return False
        return True


if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        print("\n========== 🧩 TASK TRACKER ==========")
        print("1️⃣  Add Task")
        print("2️⃣  List Tasks")
        print("3️⃣  Complete Task")
        print("4️⃣  Remove Task")
        print("5️⃣  Exit")
        print("====================================")

        choice = input("👉 Choose: ").strip()

        if choice == "1":
            title = input("📝 Enter task name: ").strip()
            manager.add_tasks(title)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            index = int(input("🔢 Enter task number: "))
            manager.complete_task(index)
        elif choice == "4":
            index = int(input("🔢 Enter task number: "))
            manager.remove_task(index)
        elif choice == "5":
            print("👋 Exiting Task Tracker. Goodbye!")
            break
        else:
            print("⚠️  Invalid choice, please try again.")