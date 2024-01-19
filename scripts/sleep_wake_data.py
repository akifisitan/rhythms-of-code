import os
from pprint import pprint
from utils import write_data 

# Script to collect data from .md files
def collect_sleep_wake_times():
    sleep_wake_data = {}
    for file_name in os.listdir("personal_data"):
        with open(f"personal_data/{file_name}") as f:
            text = f.read()
        lines = text.split("\n")
        times = {"wake": None, "sleep": None}
        for line in lines:
            if times["sleep"] is not None and times["wake"] is not None:
                break
            if "Wake" in line:
                time = line.split()[1].replace(".", ":") + ":00"
                times["wake"] = time
            elif "Sleep" in line:
                time = line.split()[1].replace(".", ":") + ":00"
                times["sleep"] = time
        sleep_wake_data[file_name.split(".")[0]] = times
    return sleep_wake_data

sleep_wake_data = collect_sleep_wake_times()
pprint(sleep_wake_data["2023-09-28"])

# Store the data in a json file for processing later
write_data("data_sleep_wake.json", sleep_wake_data)
