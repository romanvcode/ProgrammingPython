import tkinter as tk
from workerdb import WorkerDB, Worker


class WorkersMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Worker Database")
        self.workers_db = WorkerDB()

        default_filename = "workers.csv"
        self.filename_label = tk.Label(root, text="Filename:")
        self.filename_entry = tk.Entry(root)
        self.filename_entry.insert(index=0, string=default_filename)
        self.filename_label.pack()
        self.filename_entry.pack()

        self.read_csv_button = tk.Button(root, text="Read from CSV", command=self.read_from_csv)
        self.read_csv_button.pack()

        self.add_worker_button = tk.Button(root, text="Add Worker", command=self.add_worker_window)
        self.add_worker_button.pack()

        self.edit_workers_button = tk.Button(root, text="Edit Worker", command=self.edit_worker_window)
        self.edit_workers_button.pack()

        self.display_workers_button = tk.Button(root, text="Display Workers", command=self.display_workers_window)
        self.display_workers_button.pack()

        self.sort_button = tk.Button(root, text="Sort Workers", command=self.sort_workers_window)
        self.sort_button.pack()

        self.search_button = tk.Button(root, text="Search Workers", command=self.search_workers_window)
        self.search_button.pack()

        self.plot_departs_button = tk.Button(root, text="Plot Departments", command=self.plot_departs)
        self.plot_departs_button.pack()

    def read_from_csv(self):
        filename = self.filename_entry.get()
        self.workers_db.read_from_csv(filename)

    def add_worker_window(self):
        add_worker_window = tk.Toplevel(self.root)
        add_worker_window.title("Add Worker")
        add_worker_window.geometry("200x200")

        name_label = tk.Label(add_worker_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(add_worker_window)
        self.name_entry.pack()

        surname_label = tk.Label(add_worker_window, text="Surname:")
        surname_label.pack()
        self.surname_entry = tk.Entry(add_worker_window)
        self.surname_entry.pack()

        depart_label = tk.Label(add_worker_window, text="Department:")
        depart_label.pack()
        self.depart_entry = tk.Entry(add_worker_window)
        self.depart_entry.pack()

        salary_label = tk.Label(add_worker_window, text="Salary:")
        salary_label.pack()
        self.salary_entry = tk.Entry(add_worker_window)
        self.salary_entry.pack()

        add_button = tk.Button(add_worker_window, text="Add", command=self.add_worker)
        add_button.pack()

    def add_worker(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        depart = self.depart_entry.get()
        salary = float(self.salary_entry.get())

        worker = Worker(name, surname, depart, salary)

        self.workers_db.add_worker(worker)
        self.workers_db.display_workers()

    def edit_worker_window(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Worker")
        edit_window.geometry("200x200")

        edit_id_label = tk.Label(edit_window, text="Enter Worker ID to Edit:")
        edit_id_label.pack()
        self.edit_id_entry = tk.Entry(edit_window)
        self.edit_id_entry.pack()

        field_label = tk.Label(edit_window, text="Field to Edit:")
        field_label.pack()

        options = ["Name", "Surname", "Department", "Salary"]
        self.edit_var = tk.StringVar(edit_window)
        self.edit_var.set(options[0])
        edit_menu = tk.OptionMenu(edit_window, self.edit_var, *options)
        edit_menu.pack()

        edit_value_label = tk.Label(edit_window, text="Enter New Value:")
        edit_value_label.pack()
        self.edit_value_entry = tk.Entry(edit_window)
        self.edit_value_entry.pack()

        edit_button = tk.Button(edit_window, text="Edit", command=self.edit_worker)
        edit_button.pack()

    def edit_worker(self):
        worker_id = int(self.edit_id_entry.get())
        field = self.edit_var.get().lower()
        new_value = self.edit_value_entry.get()

        self.workers_db.edit_worker(worker_id, field, new_value)
        self.workers_db.display_workers()

    def display_workers_window(self):
        workers_window = tk.Toplevel(self.root)
        workers_window.title("Workers List")

        workers_text = tk.Text(workers_window, height=10, width=40)
        workers_text.pack()

        for worker in self.workers_db.workers:
            worker_info = (f"ID: {worker.get_id()}\n"
                           f"Name: {worker.name}\n"
                           f"Surname: {worker.surname}\n"
                           f"Department: {worker.depart}\n"
                           f"Salary: {worker.salary}\n\n")
            workers_text.insert(tk.END, worker_info)

    def sort_workers_window(self):
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Sort Workers")
        sort_window.geometry("200x200")

        sort_label = tk.Label(sort_window, text="Sort by:")
        sort_label.pack()

        options = ["Name", "Surname", "Department", "Salary"]
        self.sort_var = tk.StringVar(sort_window)
        self.sort_var.set(options[0])
        sort_menu = tk.OptionMenu(sort_window, self.sort_var, *options)
        sort_menu.pack()

        sort_button = tk.Button(sort_window, text="Sort", command=self.sort_workers)
        sort_button.pack()

    def sort_workers(self):
        field = self.sort_var.get().lower()
        self.workers_db.sort_workers(field)
        self.workers_db.display_workers()

    def search_workers_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Workers")
        search_window.geometry("200x200")

        search_label = tk.Label(search_window, text="Search by:")
        search_label.pack()

        self.search_entry = tk.Entry(search_window)
        self.search_entry.pack()

        search_button = tk.Button(search_window, text="Search", command=self.search_workers)
        search_button.pack()

    def search_workers(self):
        search_field = self.search_entry.get()

        found_workers = self.workers_db.search_workers(search_field)

        if found_workers:
            search_result_window = tk.Toplevel(self.root)
            search_result_window.title("Search Results")

            results_text = tk.Text(search_result_window, height=10, width=40)
            results_text.pack()

            for worker in found_workers:
                worker_info = (f"ID: {worker.get_id()}\n"
                               f"Name: {worker.name}\n"
                               f"Surname: {worker.surname}\n"
                               f"Department: {worker.depart}\n"
                               f"Salary: {worker.salary}\n\n")
                results_text.insert(tk.END, worker_info)
        else:
            print("No Results.")

    def plot_departs(self):
        self.workers_db.plot_departs()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    menu = WorkersMenu(root)
    root.mainloop()
