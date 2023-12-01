import unittest
from worker import Worker
from workerdb import WorkerDB


class TestCase(unittest.TestCase):
    def setUp(self):
        self.db = WorkerDB()
        self.worker1 = Worker("Vito", "Scaletta", "Mafia", 50000)
        self.worker2 = Worker("Joe", "Barbaro", "Mafia", 60000)
        self.db.add_worker(self.worker1)
        self.db.add_worker(self.worker2)

    def test_add_worker(self):
        self.assertEqual(len(self.db.workers), 2)
        new_worker = Worker("Charlie", "Brown", "IT", 70000)
        self.db.add_worker(new_worker)
        self.assertEqual(len(self.db.workers), 3)

    def test_del_worker(self):
        self.assertEqual(len(self.db.workers), 2)
        self.db.del_worker(self.worker1.get_id())
        self.assertEqual(len(self.db.workers), 1)

    def test_edit_worker(self):
        self.db.edit_worker(self.worker1.get_id(), "salary", 55000)
        self.assertEqual(self.worker1.salary, 55000)

    def test_read_file(self):
        filename = "workers.csv"
        self.db.read_from_csv(filename)
        self.assertEqual(len(self.db.workers), 4)

    def test_sort_workers(self):
        self.worker3 = Worker("Eve", "Adams", "HR", 45000)
        self.db.add_worker(self.worker3)
        self.db.sort_workers("salary")
        sorted_db = [worker.salary for worker in self.db.workers]
        self.assertEqual(sorted_db, [45000, 50000, 60000])

    def test_search_workers(self):
        found = self.db.search_workers("Vito")
        self.assertEqual(self.worker1, found[0])


if __name__ == "__main__":
    unittest.main()
