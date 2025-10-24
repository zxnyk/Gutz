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
        task = Task(title)
        self.tasks.append(task)
        print(f"Added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        done  = 0
        to_do = 0 
        print(f"TOTAL TASK: {len(self.tasks)}")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}: {task}")
            if task.done:
                done += 1
            else:
                to_do += 1
        print(f"✅ Done: {done} | 🕓 To Do: {to_do}")

    def remove_task(self, index):
        self.tasks.pop(index - 1 )

    def complete_task(self, index):
        self.tasks[index - 1].mark_done()

if __name__ == "__main__":
    manager = TaskManager()
    
