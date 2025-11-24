from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\n---Task Manager Advanced with AI---")
    print("1. Add task")
    print("2. Add complex task with AI")
    print("3. List tasks")
    print("4. Marked task as completed")
    print("5. Delete task")
    print("6. Exit")

def main():
    manager = TaskManager()

    while True:
        
        print_menu()

        try: 

            choice = int(input("Choose an option: "))

            match choice:
                case 1: 
                    description = input("What task do you have to do? ")
                    manager.add_task(description)
                    pass
                case 2: 
                    description = input("What task do you have to do? ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print (subtask)
                            break   
                case 3: 
                    manager.list_tasks()
                case 4: 
                    task_id = int(input("Wich task have you completed? "))
                    manager.complete_task(task_id)
                case 5: 
                    task_id = input("Wich task do you wish to delete? ")
                    manager.delete_task(task_id)
                case 6: 
                    print("Thank you for using this Task Manager... ")
                    break;
                case _: 
                    print ("Invalid Option.")
        except ValueError:
            print("Invalid Option")  


if __name__ == "__main__":
    main()