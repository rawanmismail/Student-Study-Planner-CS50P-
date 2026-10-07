# STUDENT STUDY PLANNER


The **Student Study Planner** is a command-line interface (CLI) application written in Python, designed to help students of all grades to organize, manage, and track their academic workload. Keeping track of coursework, assignment deadlines, exams, and daily reminders across multiple subjects can quickly become overwhelming. This application provides a centralized, lightweight, and offline solution for students to organize active assignments, record completed tasks, set scheduled reminders, and analyze productivity metrics.

### Features & Overview
The application operates on an interactive main menu loop that accepts user choices to trigger specific sub-functions.

1. **Task Management**: Students can create tasks by entering essential attributes such as Task Name, Subject/Course, Due Date, Priority (Low, Medium, High), and Additional Notes. Active tasks default to an "In Progress" status and can be updated to "Completed" or deleted from the system.
2. **Reminders**: A dedicated sub-system allows users to set general study reminders paired with specific dates and times.
3. **Search & Analytics**: Users can search active tasks by keyword (matching against task titles or subject names) and view real-time statistics, including total task count, active task count, completed count, and an overall percentage completion rate.

---

### Key Design Choices

During development, several key architectural and structural decisions were made:

- **In-Memory Lists vs. Direct Database/File Reads**: Global list structures (`tasks`, `completed`, and `reminders`) are kept in memory during runtime rather than constantly reading/writing to the disk on every input. This speeds up execution and gives the user control over when to save or load state via dedicated menu options.
- **JSON for Storage**: CSV files were considered initially, but nested dictionaries with varying attributes (like notes or custom priorities) were neater to represent using standard JSON formatting.

---

### How to Run

1. Open your terminal in the project directory:
   ```bash
   python project.py

### Demonstartion Video Link
https://www.youtube.com/watch?v=xcMM3Kdaq8Y

