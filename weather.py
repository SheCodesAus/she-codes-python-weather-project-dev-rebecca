import csv
from datetime import date, datetime
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

    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list.append(row)

    list.pop(0)

    list = [x for x in list if x != []]

    for row in list:
        row[1] = int(row[1])
        row[2] = int(row[2])

    return list

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
    
    if weather_data == []:
        return()

    list = []

    for num in weather_data:
        num = float(num)
        list.append(num)

    maximum = max(list)

    for i in reversed(range(len(list))):
        if list[i] == maximum:
            return maximum, i


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    list = []
    dates = []
    low_numbers = []
    high_numbers = []
    days = 0

    for row in weather_data:
        list.append(row)

    for num in list:
        dates.append(num[0])
        low_numbers.append(num[1])
        high_numbers.append(num[2])
        # Count days on list
        if row[1] > days: 
            days+= 1

    # Finding min and max, and their respective indexes

    min_num_and_index = find_min(low_numbers)
    max_num_and_index = find_max(high_numbers)

    min_number = min_num_and_index[0]
    min_index = min_num_and_index[1]

    max_number = max_num_and_index[0]
    max_index = max_num_and_index[1]

    # Converting min & max to celcius

    min_celcius = convert_f_to_c(min_number)
    max_celcius = convert_f_to_c(max_number)

    # Finding high & low mean, and converting to celcius

    ave_low_f = calculate_mean(low_numbers)
    ave_low_c = convert_f_to_c(ave_low_f)
    
    ave_high_f = calculate_mean(high_numbers)
    ave_high_c = convert_f_to_c(ave_high_f)

    # Finding dates based on min and max index

    min_iso_date = dates[min_index]
    min_human_date = convert_date(min_iso_date)

    max_iso_date = dates[max_index]
    max_human_date = convert_date(max_iso_date)

    return(f"{days} Day Overview\n  The lowest temperature will be {min_celcius}{DEGREE_SYBMOL}, and will occur on {min_human_date}.\n  The highest temperature will be {max_celcius}{DEGREE_SYBMOL}, and will occur on {max_human_date}.\n  The average low this week is {ave_low_c}{DEGREE_SYBMOL}.\n  The average high this week is {ave_high_c}{DEGREE_SYBMOL}.")

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    list = []
    result = ""

    for row in weather_data:
        list.append(row)

    for x in list:
        date = (convert_date(x[0]))
        min = (format_temperature(convert_f_to_c(x[1])))
        max = (format_temperature(convert_f_to_c(x[2])))
        result += f"---- {date} ----\n"
        result += f"  Minimum Temperature: {min}\n"
        result += f"  Maximum Temperature: {max}\n\n"

    return result