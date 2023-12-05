import csv


def append_result(result):
    with open('results.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=result.keys())

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(result)

    return "Data appended successfully"
