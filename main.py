# main.py

from task_manager import TaskManager

def main():
    server = 'DESKTOP-VIKK52P'
    database = 'TO_DO_List'
    

    task_manager = TaskManager(server, database)

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. List Pending Tasks")
        print("4. Search Task")
        print("5. Update Task Status")
        print("6. Mark Task as Completed")
        print("7. Edit Task Name")
        print("8. Delete Task")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
            print("Task added.")
        elif choice == '2':
            tasks = task_manager.list_tasks()
            for task in tasks:
                print(task)
        elif choice == '3':
            tasks = task_manager.list_pending_tasks()
            for task in tasks:
                print(task)
        elif choice == '4':
            search_term = input("Enter search term: ")
            tasks = task_manager.search_task(search_term)
            for task in tasks:
                print(task)
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (Pending/Completed): ")
            task_manager.update_task_status(task_id, new_status)
            print("Task status updated.")
        elif choice == '6':
            task_id = int(input("Enter task ID to mark as completed: "))
            task_manager.mark_task_completed(task_id)
            print("Task marked as completed.")
        elif choice == '7':
            task_id = int(input("Enter task ID to edit: "))
            new_name = input("Enter new task name: ")
            task_manager.edit_task_name(task_id, new_name)
            print("Task name updated.")
        elif choice == '8':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
            print("Task deleted.")
        elif choice == '9':
            task_manager.close()
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
