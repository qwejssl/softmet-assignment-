"""Unit tests for TaskManager."""

from assignment1.test import TaskManager


def test_add_and_list():
    manager = TaskManager()
    manager.add_task("Read book", 3)
    lines = manager.list_tasks()
    assert any("Read book" in line for line in lines)


def test_complete_task():
    manager = TaskManager()
    manager.add_task("Run 5k", 2)
    manager.complete_task(1)
    assert manager.tasks[0].completed is True


def test_invalid_priority():
    manager = TaskManager()
    try:
        manager.add_task("Oops", 10)  # priority out of range
    except ValueError as exc:
        assert "Priority must be between" in str(exc)
    else:
        raise AssertionError("Expected ValueError was not raised")
