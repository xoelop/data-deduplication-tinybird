import re
import math


def str_human_to_number(num: str):
    num_events_total = int(re.findall(r"\d+", num)[0])
    if "k" in num.lower():
        num_events_total *= 1e3
    elif "m" in num.lower():
        num_events_total *= 1e6
    elif "b" in num.lower():
        num_events_total *= 1e9
    num_events_total = int(num_events_total)
    return num_events_total


def number_to_human_str(number):
    # from https://stackoverflow.com/a/45478574/5031446
    units = ["", "K", "M", "G", "T", "P"]
    k = 1000.0
    magnitude = int(math.floor(math.log(number, k)))
    return "%.0f%s" % (number / k ** magnitude, units[magnitude])
