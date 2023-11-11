import csv

c_id = 0


class Worker:
    def __init__(self, name, surname, depart, salary):
        global c_id
        self.__id = c_id
        c_id = c_id + 1
        self.set_id(c_id)
        self.name = name
        self.surname = surname
        self.depart = depart
        self.salary = float(salary)

    def set_id(self, new):
        self.__id = new

    def get_id(self):
        return self.__id

    def __str__(self):
        output = ""
        output += f"ID: {self.get_id()}\n"
        output += f"Name: {self.name}\n"
        output += f"Surname: {self.surname}\n"
        output += f"Depart: {self.depart}\n"
        output += f"Salary: {self.salary}\n"
        return output

    @classmethod
    def input_worker(cls):
        name = input("Enter worker name: ")
        surname = input("Enter worker surname: ")
        department = input("Enter worker department: ")
        salary = float(input("Enter salary: "))
        return cls(name, surname, department, salary)


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
                salary = float(row['salary'])
                worker = Worker(name, surname, depart, salary)
                self.add_worker(worker)

    def display_workers(self):
        if not self.workers:
            print("List is empty.")
        else:
            for worker in self.workers:
                print(worker)

    def sort_workers(self, field):
        if not self.workers:
            print("List is empty.")
        else:
            try:
                self.workers.sort(key=lambda item: getattr(item, field))
                print(f"Sorted successfully by {field}")
            except AttributeError as e:
                print(e)

    def search_workers(self, field):
        found = []
        for worker in self.workers:
            if field in str(worker):
                found.append(worker)
        if not found:
            print(f"Worker with field {field} not found.")
        else:
            print("Searched workers:")
            for worker in found:
                print(f"Worker with field '{field}':\n {worker}")
