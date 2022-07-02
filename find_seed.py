from urllib.request import urlopen
import json
import re
import random
import os
import sys


threshold = 13 # only seeds of runs under this many minutes


def get_time(run):
    time_str = run["run"]["times"]["primary"]
    hours_match = re.search(r"\d+(?=H)", time_str)
    hours = int(hours_match.group(0)) if hours_match is not None else 0

    minutes_match = re.search(r"\d+(?=M)", time_str)
    minutes = int(minutes_match.group(0)) if minutes_match is not None else 0

    seconds_match = re.search(r"\d+(?=.?\d{0,3}S)", time_str)
    seconds = int(seconds_match.group(0)) if seconds_match is not None else 0

    millis_match = re.search(r"\d+(?=S)", time_str)
    millis = int(millis_match.group(0)) if millis_match is not None else 0
    return [hours, minutes, seconds, millis]


def get_seed(run):
    comment = run["run"]["comment"]
    regex = re.compile(r"(?<=seed:\s)-?\d+", re.I)
    match = re.search(regex, comment) or re.search(r"\d{4,}", comment)
    return match.group(0)


def main():
    os.chdir(sys.path[0])
    response = urlopen("""
        https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926?var-jlzkwqlz=mln68v0q&var-r8rg67rn=21d4zvp1
    """)
    data_json = json.loads(response.read())
    runs = data_json["data"]["runs"]
    runs_filtered = list(filter(lambda run: get_time(run)[1] < threshold and get_time(run)[0] == 0, runs))
    rand_run = random.choice(runs_filtered)
    seed = get_seed(rand_run)
    with open("seed.txt", "w") as f:
        f.writelines(seed)


if __name__ == "__main__":
    main()
