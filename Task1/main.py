from worker import Worker
from workerdb import WorkerDB

workers = WorkerDB()

menu = """
    1. Add Worker
    2. Delete Worker
    3. Edit Worker
    4. Read CSV
    5. Display Workers
    6. Sort Workers
    7. Search Worker
    0. Exit the program
"""

while True:
    print(menu)

    choice = input("Select option: ")

    if choice == '1':
        worker = Worker.input_worker()
        workers.add_worker(worker)
    elif choice == '2':
        try:
            id_to_del = int(input("Enter id to delete: "))
            workers.del_worker(id_to_del)
        except ValueError as e:
            print(e)
    elif choice == '3':
        try:
            id_to_edit = int(input("Enter id to edit: "))
            field = input("Enter field to edit: ")
            value = input("Enter value to edit: ")
            workers.edit_worker(id_to_edit, field, value)
        except ValueError as e:
            print(e)
    elif choice == '4':
        filename = input("Enter a filename: ")
        workers.read_from_csv(filename)
    elif choice == '5':
        workers.display_workers()
    elif choice == '6':
        field = input("Enter field to sort: ")
        workers.sort_workers(field)
    elif choice == '7':
        field = input("Enter field to search: ")
        found = workers.search_workers(field)
        try:
            for worker in found:
                print(worker)
        except Exception as e:
            print(e)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Enter again.")
