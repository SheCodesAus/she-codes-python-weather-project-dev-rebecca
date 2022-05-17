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
pass
#     datetime.strptime(iso_string, "%d")

# 2021-07-05T07:00:00+08:00

# import datetime
# test = datetime.datetime.strptime('2021-07-05T07:00:00+08:00', "%Y-%m-%dT%H:%M:%S%z")

# print(test)

# new = datetime.datetime.strptime(test, "%Y-%m-%dT%H:%M:%S%z")

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
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    index = 0
    minimum = weather_data[0]

    for num in weather_data:
        if num <= minimum:
            index += 1
            minimum = num

    return minimum, index
    
# data = [49, 57, 56, 55, 53]
# print(find_min(data))

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
