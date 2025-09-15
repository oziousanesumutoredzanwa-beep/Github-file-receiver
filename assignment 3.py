def classify_number():
    while True:
        user_input = input("Please enter an integer: ")
        try:
            number = int(user_input)
            if number > 0:
                return "Positive"
            elif number < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("That's not a valid integer. Please try again.")


result = classify_number()
print(result)

#Question 2

def calculate_average(*args):
    """
    Calculate the average of a variable number of numerical arguments.

    Parameters:
    *args (float): A variable number of numerical values.

    Returns:
    float: The average of the provided numbers. Returns None if no numbers are provided.
    """
    if not args:
        return None

    total = sum(args)
    count = len(args)
    average1 = total / count
    return average1

avg = calculate_average(10, 20, 30)
print(f"The average is: {avg}")

#Question 3

def get_valid_number():
    while True:
        user_input = input("Please enter a number: ")
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

valid_number = get_valid_number()
print(f"You entered a valid number: {valid_number}")

#Question 4

names = ["Lisa", "Bury", "James", "Phil", "Peter"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

#Quesion 5

celsius_temps = [0, 19, 21, 100, -15]

fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)

#Question 6

def divide_numbers(numerator, denominator):
    """
    Divide two numbers and handle exceptions for division by zero and invalid types.

    Parameters:
    numerator (float or int): The number to be divided.
    denominator (float or int): The number by which to divide.

    Returns:
    float: The result of the division if successful.
    """
    try:
        result1 = numerator / denominator
        return result1
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")

num = 10
den = 0

result = divide_numbers(num, den)
if result is not None:
    print(f"The result of {num} / {den} is: {result}")

#Question 7

class NegativeNumberError(Exception):
    """Custom exception raised for negative numbers."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"NegativeNumberError: {value} is a negative number.")

def check_positive(number):
    """
    Check if the number is positive.

    Parameters:
    number (int or float): The number to check.

    Raises:
    NegativeNumberError: If the number is negative.
    """
    if number < 0:
        raise NegativeNumberError(number)

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)

#Question 8

import random

def generate_random_integers(count, lower_bound, upper_bound):
    """
    Generate a list of random integers.

    Parameters:
    count (int): Number of random integers to generate.
    lower_bound (int): Minimum integer value.
    upper_bound (int): Maximum integer value.

    Returns:
    list: A list of random integers.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The average of the numbers.
    """
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

random_numbers = generate_random_integers(10, 1, 100)
average = calculate_average(random_numbers)

print("Generated random integers:", random_numbers)
print("Average of generated numbers:", average)

#Question 9

import re


def extract_emails(text):
    """
    Extracts all email addresses from a given text.

    Args:
        text (str): The input string.

    Returns:
        list: A list of all found email addresses.
    """

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, text)


def validate_date(date_string):
    """
    Validates a date in 'YYYY-MM-DD' format.

    Args:
        date_string (str): The date string to validate.

    Returns:
        bool: True if the date is valid, False otherwise.
    """

    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(date_regex, date_string) is not None


def replace_word(text, old_word, new_word):
    """
    Replaces all occurrences of a word with another word.

    Args:
        text (str): The input string.
        old_word (str): The word to be replaced.
        new_word (str): The new word.

    Returns:
        str: The string with the word replaced.
    """

    word_regex = r'\b' + re.escape(old_word) + r'\b'
    return re.sub(word_regex, new_word, text, flags=re.IGNORECASE)

def split_by_non_alphanumeric(text):
    """
    Splits a string by all non-alphanumeric characters.

    Args:
        text (str): The input string.

    Returns:
        list: A list of substrings split by non-alphanumeric characters.
    """

    return re.split(r'\W+', text)

if __name__ == "__main__":
    # Part I: Extract Emails
    text_with_emails = "Please contact me at john.doe@example.com or support@company.org for assistance."
    emails_found = extract_emails(text_with_emails)
    print("Extracted emails:", emails_found)
    print("-" * 20)

    # Part II: Validate Date
    date1 = "2025-09-15"
    date2 = "15-09-2025"
    print(f"Is '{date1}' a valid date format? {validate_date(date1)}")
    print(f"Is '{date2}' a valid date format? {validate_date(date2)}")
    print("-" * 20)

    # Part III: Replace Word
    original_text = "The quick brown fox jumps over the lazy dog."
    replaced_text = replace_word(original_text, "fox", "cat")
    print("Original string:", original_text)
    print("Replaced string:", replaced_text)
    print("-" * 20)

    # Part IV: Split by non-alphanumeric
    sentence = "Hello, world! This is a test. 123-abc."
    split_result = split_by_non_alphanumeric(sentence)
    print("Original string:", sentence)
    print("Split result:", split_result)
    print("-" * 20)

#Question 10

import socket

def start_server(host='127.0.0.1', port=65432):
    """Start the server to listen for incoming connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        while True:
            try:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    message = "Hello from server!"
                    conn.sendall(message.encode())
            except Exception as f:
                print(f"Error: {f}")

if __name__ == "__main__":
    start_server()

#Question 11

import requests

# API endpoint (example: JSONPlaceholder test API)
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)  # Send GET request

    # Check if request was successful (status code 200 means OK)
    if response.status_code == 200:
        data = response.json()  # Convert response to Python dictionary
        print("Response Data:", data)
    else:
        print("Request failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error during request:", e)



