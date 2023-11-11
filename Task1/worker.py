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
