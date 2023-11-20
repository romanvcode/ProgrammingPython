import csv
from worker import Worker


def decorator_sort(func):
    def wrapper(self, field):
        func(self, field)
        print(f"Sorted successfully by {field}")
    return wrapper


def decorator_search(func):
    def wrapper(self, field):
        print(f"Searched results for field {field}:")
        func(self, field)
    return wrapper


class WorkerDB:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def del_worker(self, id_to_del):
        for worker in self.workers:
            if worker.get_id() == id_to_del:
                self.workers.remove(worker)
                return
            else:
                print(f"Worker with ID {id_to_del} not found.")

    def edit_worker(self, id_to_edit, field, value_to_edit):
        for worker in self.workers:
            if worker.get_id() == id_to_edit:
                if hasattr(worker, field):
                    setattr(worker, field, value_to_edit)
                    print(f"Tax Free with ID {id_to_edit} - Field '{field}' edited.")
                    return
                else:
                    print(f"Invalid field: {field}.")
                return
            else:
                print(f"Worker with ID: {id_to_edit} not found.")

    def read_from_csv(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                name = row['name']
                surname = row['surname']
                depart = row['depart']
                salary = row['salary']
                salary = float(salary)
                worker = Worker(name, surname, depart, salary)
                self.add_worker(worker)

    def display_workers(self):
        if not self.workers:
            print("List is empty.")
        else:
            for worker in self.workers:
                print(worker)

    @decorator_sort
    def sort_workers(self, field):
        try:
            self.workers.sort(key=lambda item: getattr(item, field))
        except AttributeError as e:
            print(e)

    @decorator_search
    def search_workers(self, field):
        found = []
        for worker in self.workers:
            if field in str(worker):
                found.append(worker)
        if not found:
            print(f"Worker with field {field} not found.")
        else:
            for worker in found:
                print(worker)
