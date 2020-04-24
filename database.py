import csv


def add_info(person_id, filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [str(person_id)]:
                return 0

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([person_id])

    return 1

def get_full_info(filename):
    full_list = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            full_list.append(row)
    return full_list
