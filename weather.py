import csv
from datetime import datetime
from mimetypes import init
from typing import ItemsView

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    data = iso_string[:-15] # Remove timezone at end
    date_object = datetime.strptime(data, "%Y-%m-%d")
    formatted = date_object.strftime("%A %d %B %Y")
    return formatted

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    float_farenheit = float(temp_in_farenheit)
    celcius = 5/9 * (float_farenheit - 32)
    format_celcius = "{:.1f}".format(celcius)
    float_celcius = float(format_celcius)
    return float_celcius

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    list = []

    for data in weather_data:
        float_data = float(data)
        list.append(float_data)

    length = len(list)

    total = sum(list) / length
    mean = float(total)

    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    list = []
    new_list = []

    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list.append(row)

    list.pop(0)

    for row in list:
        new_list.append(int(row[1]))
        new_list.append(int(row[2]))

    print(new_list)
    return list

print(load_data_from_csv("tests/data/example_one.csv"))

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if weather_data == []:
        return()

    list = []

    for num in weather_data:
        num = float(num)
        list.append(num)

    minimum = min(list)

    for i in reversed(range(len(list))):
        if list[i] == minimum:
            return minimum, i

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
