class Task:
    def __init__(self, title, description=''):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            status = 'Completed'
        else:
            status = 'Incomplete'
        return f"{self.title} - {self.description} [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks.pop(index-1)

    def update_task(self, index, title=None, description=None):
        if 1 <= index <= len(self.tasks):
            if title:
                self.tasks[index-1].title = title
            if description:
                self.tasks[index-1].description = description

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index-1].mark_completed()

    def __str__(self):
        return "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        print(todo_list)
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Update task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            description = input("Task description: ")
            todo_list.add_task(Task(title, description))
        elif choice == '2':
            index = int(input("Task number to remove: "))
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Task number to update: "))
            title = input("New title (leave empty to keep current): ")
            description = input("New description (leave empty to keep current): ")
            todo_list.update_task(index, title, description)
        elif choice == '4':
            index = int(input("Task number to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again. Enter option between (1 - 5)")


if __name__ == "__main__":
    main()
