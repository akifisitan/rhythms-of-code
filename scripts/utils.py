import json

# Define helper functions for reading and writing data
def read_data(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_data(filename: str, data: dict):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)