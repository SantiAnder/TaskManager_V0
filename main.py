from task_manager import TaskManager

def print_menu():
    print("\n---Task Manager Advanced with AI---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Marked task as completed")
    print("4. Delete task")
    print("5. Exit")

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
                    manager.list_tasks()
                case 3: 
                    task_id = int(input("Wich task have you completed? "))
                    manager.complete_task(task_id)
                case 4: 
                    task_id = input("Wich task do you wish to delete? ")
                    manager.delete_task(task_id)
                case 5: 
                    print("Thank you for using this Task Manager... ")
                    break;
                case _: 
                    print ("Invalid Option.")
        except ValueError:
            print("Invalid Option")  


if __name__ == "__main__":
    main()