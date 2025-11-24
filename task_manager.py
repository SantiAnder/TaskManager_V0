import json

class Task: 
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:

    FILENAME = "task.json"
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_task()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1 
        print(f"Added {description} to the tasks list.")
        self.save_task()

    def list_tasks(self):
        if not self._tasks:
            print("There are no current tasks")
        else: 
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
                if task.id == id:
                    task.completed = True
                    self.save_task()
                    print(f"{task.description} marked as completed.")
                    return 
        print("There is no task with that ID") 

    def delete_task(self, id):
        for task in self._tasks:
                if task.id == id:
                    self._tasks.remove(task)
                    self.save_task()
                    print(f"Task number #{task.id} eliminated.")
                    return 
        print("There is no task with that ID")

    def load_task(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1 
                else: 
                    self._next_id = 1
        except  FileNotFoundError:     
            self._tasks = []
    
    def save_task(self):
         with open(self.FILENAME, "w") as file:
             json.dump([{"id":task.id, "description": task.description, "completed": task.completed}for task in self._tasks], file, indent=4)