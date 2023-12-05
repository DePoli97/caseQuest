import csv


def append_result(result):
    dict_result = result.dict()
    with open('results.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_result.keys())

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(dict_result)

    return "Data appended successfully"
