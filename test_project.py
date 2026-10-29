import json
import pytest
from unittest.mock import patch

# Import functions and global lists from project.py
import project
from project import (
    tasks,
    completed,
    reminders,
    add_task,
    completed_tasks,
    add_reminder,
    save_planner,
    load_planner,
)


@pytest.fixture(autouse=True)
def clear_lists():
    """Reset global state before each test."""
    tasks.clear()
    completed.clear()
    reminders.clear()


def test_add_task():
    user_inputs = ["Math Homework", "Calculus", "2026-10-15", "High", "Chapter 4"]

    with patch("builtins.input", side_effect=user_inputs):
        add_task()

    assert len(tasks) == 1
    assert tasks[0]["Task Name"] == "Math Homework"
    assert tasks[0]["Subject"] == "Calculus"
    assert tasks[0]["Priority"] == "High"
    assert tasks[0]["Status"] == "In Progress"


def test_completed_tasks():
    # Pre-fill active task
    tasks.append({
        "Task Name": "Essay",
        "Subject": "History",
        "Due Date": "2026-10-20",
        "Priority": "Medium",
        "Notes": "1000 words",
        "Status": "In Progress",
    })

    # User inputs task number '1' to complete
    with patch("builtins.input", return_value="1"):
        completed_tasks()

    assert len(tasks) == 0
    assert len(completed) == 1
    assert completed[0]["Task Name"] == "Essay"
    assert completed[0]["Status"] == "Completed"


def test_add_reminder():
    user_inputs = ["Study Group", "2026-10-10", "15:00"]

    with patch("builtins.input", side_effect=user_inputs):
        add_reminder()

    assert len(reminders) == 1
    assert reminders[0]["Reminder"] == "Study Group"
    assert reminders[0]["Date"] == "2026-10-10"
    assert reminders[0]["Time"] == "15:00"


def test_save_and_load_planner(tmp_path, monkeypatch):
    # Setup temporary file path for testing
    file_path = tmp_path / "planner.json"

    # Patch open inside project module to use tmp_path
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: open(file_path, *args, **kwargs))

    # Add sample data
    tasks.append({"Task Name": "Physics Quiz", "Subject": "Physics", "Due Date": "Tomorrow", "Priority": "High", "Notes": "", "Status": "In Progress"})
    reminders.append({"Reminder": "Submit draft", "Date": "Today", "Time": "12:00"})

    # Test Save
    save_planner()
    assert file_path.exists()

    # Clear memory
    tasks.clear()
    reminders.clear()

    # Test Load
    load_planner()
    assert len(tasks) == 1
    assert tasks[0]["Task Name"] == "Physics Quiz"
    assert len(reminders) == 1
    assert reminders[0]["Reminder"] == "Submit draft"
