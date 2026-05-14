def add_task(tasks):
    task_1 = input("Enter task = ")
    tasks.append(task_1)

def view_task(tasks):
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for index ,task in enumerate(tasks,
        start=1):
            print(f"{index}. {task}")

def delete_task(tasks):
    deleting_task = input("Enter task to delete = ")
    try:
        tasks.remove(deleting_task)
    except ValueError:
        print("task not found")


def main():
    tasks = []
    while True:
        user_input = input(f"""1. Add task
2. View task
3. Delete task
4. Exit
=> """)



        if user_input == "1":
            add_task(tasks)
        
        elif user_input == "2":
            view_task(tasks)

        elif user_input == "3":
            delete_task(tasks)

        elif  user_input == "4":
            break

        else:
            print("Invalid option") 

if __name__ == "__main__":
    main()