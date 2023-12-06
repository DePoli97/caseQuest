import json

CONFIG_FILE_PATH = "../config.json"


def get_last_id():
    with open(CONFIG_FILE_PATH, "r") as file:
        data = json.load(file)
    return data["last_id"]


def increment_last_id():
    with open(CONFIG_FILE_PATH, "r") as file:
        data = json.load(file)
    data["last_id"] = str(int(data["last_id"]) + 1)
    with open(CONFIG_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def initialize_config_file():
    initial_data = {"last_id": 0}
    with open(CONFIG_FILE_PATH, "w") as file:
        json.dump(initial_data, file, indent=4)


try:
    with open(CONFIG_FILE_PATH, "r"):
        pass
except FileNotFoundError:
    initialize_config_file()
