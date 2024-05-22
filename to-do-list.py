"""
Project Requirements
    1- User Interface (UI):
Create a command-line interface (CLI) for the To-Do List Application.
Display a welcoming message and a menu with the following options:
```
Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit

    ```

    
    2- To-Do List Features:
Implement the following features for the To-Do List:
Adding a task with a title (by default “Incomplete”).
Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
Marking a task as complete.
Deleting a task.
Quitting the application.

    3- User Interaction:
Allow users to interact with the application by selecting menu options using input().
Implement input validation to handle unexpected user input gracefully.

    4- Error Handling:
Implement error handling using try, except, else, and finally blocks to handle potential issues.

    5- Code Organization:
Organize your code into functions to promote modularity and readability.
Use meaningful function names with appropriate comments and docstrings for clarity.

    6- Testing and Debugging:
Thoroughly test your application to identify and fix any bugs.
Consider edge cases, such as empty task lists or incorrect user input.

    7- Documentation:
Include a README file that explains how to run the application and provides a brief overview of its features.

    8- Optional Features (Bonus):
If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

    9- GitHub Repository:
Create a GitHub repository for your project.
Commit your code to the repository regularly.
Include a link to your GitHub repository in your project documentation.



    Submission
Submit your project, including all source code files and the README, to your instructor or designated platform.

    Project Tips
Start by designing a simple user interface and plan the program's structure.
Test your code frequently as you build each feature to ensure everything works as expected.
Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!
"""

def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Complete")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return


    view_tasks(tasks)
    index = int(input("Enter task index to mark as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return


    view_tasks(tasks)
    index = int(input("Enter task index to delete: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task index.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()


    while True:
        display_menu()


        choice = input("Enter your choice: ").lower()


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
