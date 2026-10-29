import json

tasks = []
completed = []
reminders = []


# OPTION 1 — ADD TASK
def add_task():
    print("")
    print("----- ADD NEW TASK -----")
    print("Please fill in the following details.")
    print("")
    

    task_name = input("Task Name: ")
    subject = input("Subject / Course: ")
    due_date = input("Due Date: ")
    priority = input("Priority (Low / Medium / High): ")
    notes = input("Additional Notes: ")

    task = {
        "Task Name": task_name,
        "Subject": subject,
        "Due Date": due_date,
        "Priority": priority,
        "Notes": notes,
        "Status": "In Progress"
    }

    tasks.append(task)

    print("")
    print("Task has been added successfully!")


# OPTION 2 — VIEW ACTIVE TASKS
def view_tasks():
    print("")
    print("----- YOUR ACTIVE TASKS -----")

    if len(tasks) == 0:
        print("You have no active tasks!")
        return

    for number, task in enumerate(tasks, 1):
        print("")
        print("----------------------")
        print(f"Task {number}")
        print("----------------------")
        print(f"Task Name: {task['Task Name']}")
        print(f"Subject: {task['Subject']}")
        print(f"Due Date: {task['Due Date']}")
        print(f"Priority: {task['Priority']}")
        print(f"Status: {task['Status']}")
        print(f"Notes: {task['Notes']}")


# OPTION 3 — REMOVE TASK
def remove_task():
    print("")
    print("----- REMOVE TASK -----")

    if len(tasks) == 0:
        print("You have no tasks to remove!")
        return

    view_tasks()

    try:
        number = int(input("Enter the task number you want to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)

            print("")
            print(
                f"'{removed_task['Task Name']}' "
                "has been removed successfully!"
            )
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


# OPTION 4 — COMPLETE TASK
def completed_tasks():
    print("")
    print("----- COMPLETE A TASK -----")

    if len(tasks) == 0:
        print("You have no active tasks.")
        return

    view_tasks()

    try:
        number = int(input("Enter the task number you completed: "))

        if 1 <= number <= len(tasks):
            completed_task = tasks.pop(number - 1)
            completed_task["Status"] = "Completed"
            completed.append(completed_task)

            print("")
            print(
                f"'{completed_task['Task Name']}' "
                "has been marked as completed!"
            )
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


# VIEW COMPLETED TASKS
def view_completed():
    print("")
    print("----- COMPLETED TASKS -----")

    if len(completed) == 0:
        print("You have no completed tasks!")
        return

    for number, task in enumerate(completed, 1):
        print("")
        print("----------------------")
        print(f"Completed Task {number}")
        print("----------------------")
        print(f"Task Name: {task['Task Name']}")
        print(f"Subject: {task['Subject']}")
        print(f"Due Date: {task['Due Date']}")
        print(f"Priority: {task['Priority']}")
        print(f"Status: {task['Status']}")


# OPTION 5 — ADD REMINDER
def add_reminder():
    print("")
    print("----- ADD REMINDER -----")
    print("")

    reminder_text = input("Reminder: ")
    reminder_date = input("Date: ")
    reminder_time = input("Time: ")

    reminder = {
        "Reminder": reminder_text,
        "Date": reminder_date,
        "Time": reminder_time
    }

    reminders.append(reminder)

    print("")
    print("Reminder has been added successfully!")


# VIEW REMINDERS
def view_reminders():
    print("")
    print("----- YOUR REMINDERS -----")

    if len(reminders) == 0:
        print("You have no reminders!")
        return

    for number, reminder in enumerate(reminders, 1):
        print("")
        print("----------------------")
        print(f"Reminder {number}")
        print("----------------------")
        print(f"Reminder: {reminder['Reminder']}")
        print(f"Date: {reminder['Date']}")
        print(f"Time: {reminder['Time']}")


# OPTION 6 — SAVE PLANNER
def save_planner():
    print("")
    print("----- SAVE PLANNER -----")

    planner = {
        "Tasks": tasks,
        "Completed": completed,
        "Reminders": reminders
    }

    with open("planner.json", "w") as file:
        json.dump(planner, file, indent=4)

    print("Planner has been saved successfully!")


# OPTION 7 — LOAD PLANNER
def load_planner():
    print("")
    print("----- LOAD PLANNER -----")

    try:
        with open("planner.json", "r") as file:
            planner = json.load(file)

        tasks.clear()
        completed.clear()
        reminders.clear()

        tasks.extend(planner.get("Tasks", []))
        completed.extend(planner.get("Completed", []))
        reminders.extend(planner.get("Reminders", []))

        print("Planner has been loaded successfully!")

    except FileNotFoundError:
        print("No saved planner was found.")


# OPTION 8 — SEARCH TASKS
def search_tasks():
    print("")
    print("----- SEARCH TASKS -----")

    if len(tasks) == 0:
        print("You have no active tasks!")
        return

    search = input("Enter a task name or subject: ").lower()

    found = False

    for task in tasks:
        if (
            search in task["Task Name"].lower()
            or search in task["Subject"].lower()
        ):
            print("")
            print(f"Task Name: {task['Task Name']}")
            print(f"Subject: {task['Subject']}")
            print(f"Due Date: {task['Due Date']}")
            print(f"Priority: {task['Priority']}")

            found = True

    if not found:
        print("No matching tasks found.")


# OPTION 9 — TASK STATISTICS
def task_statistics():
    print("")
    print("----- TASK STATISTICS -----")

    total_tasks = len(tasks) + len(completed)
    active_tasks = len(tasks)
    completed_count = len(completed)

    print(f"Total Tasks: {total_tasks}")
    print(f"Active Tasks: {active_tasks}")
    print(f"Completed Tasks: {completed_count}")

    if total_tasks > 0:
        completion_rate = (completed_count / total_tasks) * 100
        print(f"Completion Rate: {completion_rate:.1f}%")


# OPTION 10 — EXIT
def exit_program():
    print("")
    print("-----------------------------")
    print("Thank you for using")
    print("Student Study Planner!")
    print("Goodbye!")
    print("-----------------------------")


# MAIN MENU
def main():
    print("-----------------------------")
    print("    STUDENT STUDY PLANNER    ")
    print("-----------------------------")

    while True:
        print("")
        print("----------- MENU ------------")
        print("1. Add Task")
        print("2. View Active Tasks")
        print("3. Remove Task")
        print("4. Complete Task")
        print("5. Add Reminder")
        print("6. Save Planner")
        print("7. Load Planner")
        print("8. Search Tasks")
        print("9. Task Statistics")
        print("10. View Completed Tasks")
        print("11. View Reminders")
        print("12. Exit")
        print("-----------------------------")

        option = input("Please select an option: ")

        if option == "1":
            add_task()

        elif option == "2":
            view_tasks()

        elif option == "3":
            remove_task()

        elif option == "4":
            completed_tasks()

        elif option == "5":
            add_reminder()

        elif option == "6":
            save_planner()

        elif option == "7":
            load_planner()

        elif option == "8":
            search_tasks()

        elif option == "9":
            task_statistics()

        elif option == "10":
            view_completed()

        elif option == "11":
            view_reminders()

        elif option == "12":
            exit_program()
            break

        else:
            print("")
            print("Invalid option.")
            print("Please choose a number from 1 to 12.")


if __name__ == "__main__":
    main()
