tasks = []


while True:
        user_input = input(f"""1. Add task
2. View task
3. Delete task
4. Exit
=> """)
        
        if user_input == "1":
            task_1 = input("Enter task = ")
            tasks.append(task_1)
        
        elif user_input == "2":
            if len(tasks) == 0:
                print("no tasks yet")
            else:
                for index ,task in enumerate(tasks,
                start=1):
                    print(f"{index}. {task}")


    
        elif user_input == "3":
            deleting_task = input("Enter task to delete = ")
            try:
                tasks.remove(deleting_task)
            except ValueError:
                print("task not found")
        elif  user_input == "4":
            break
        else:
            print("Invalid option") 