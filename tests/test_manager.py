import unittest
from manager import TaskManager
from task import Task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.manager.reset_all_tasks()

    def test_add_task_assigns_id(self):
        task = Task("Test Title", "Test Description", 1, None)
        self.manager.add_task(task)
        self.assertEqual(task.id, 1)

    def test_add_second_task_gets_id_2(self):
        task1 = Task("First", "desc", 1, None)
        task2 = Task("Second", "desc", 1, None)
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        self.assertEqual(task2.id, 2)

    def test_remove_task_returns_true_when_found(self):
        task = Task("Test", "desc", 1, None)
        self.manager.add_task(task)
        result = self.manager.remove_task(task.id)
        self.assertTrue(result)

    def test_remove_task_returns_false_when_not_found(self):
        result = self.manager.remove_task(999)
        self.assertFalse(result)

    def test_mark_task_done(self):
        task = Task("Test", "desc", 1, None)
        self.manager.add_task(task)
        self.manager.mark_task_done(task.id)
        self.assertTrue(task.done)

    def test_mark_task_pending(self):
        task = Task("Test", "desc", 1, None)
        self.manager.add_task(task)
        self.manager.mark_task_done(task.id)
        self.manager.mark_task_pending(task.id)
        self.assertFalse(task.done)

    def test_sort_by_deadline_does_not_crash_with_none(self):
        task1 = Task("A", "desc", 1, None)
        task2 = Task("B", "desc", 1, None)
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        self.manager.sort_by_deadline()


if __name__ == "__main__":
    unittest.main()
