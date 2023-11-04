import csv


class Worker:
    def __init__(self, name, surname, depart, salary):
        self.__id
        self.name = name
        self.surname = surname
        self.depart = depart
        self.salary = salary


class WorkerDB:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def del_worker(self, worker):
        self.workers.remove(worker)

    def read_from_csv(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            id = 0
            for row in reader:
                if int(row['id']) > id:
                    id = int(row['id'])
                name, surname, depart, salary = row['name'], row['surname'], row['depart'], row['salary']
                self.workers.append(Worker(name, surname, depart, salary))

    def write_to_csv(self, filename):
        with open(filename, mode='w', newline='',) as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in self.workers:
                writer.writerow(row)
