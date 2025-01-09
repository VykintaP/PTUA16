# Objective: Write a Python program that calculates what day of the week your next birthday falls on.
# Steps:
# Import the datetime library.
# Ask the user to input their birthdate in the format YYYY-MM-DD.
# Parse the input into a datetime object.
# Get the current year and create a datetime object for the next birthday using the month and day from the user's input.
# If the birthday for the current year has already passed, calculate it for the next year.
# Determine the day of the week for the next birthday using .strftime("%A").
# Display the result to the user.


import datetime


def get_next_birthday_day(birthdate_input):
    try:
        # Parse the input into a datetime object
        birthdate = datetime.datetime.strptime(birthdate_input, "%Y-%m-%d")

        # Get the current year
        current_year = datetime.datetime.now().year

        # Create a datetime object for the next birthday
        next_birthday = datetime.datetime(year=current_year, month=birthdate.month, day=birthdate.day)

        # Check if the birthday for the current year has already passed
        if next_birthday < datetime.datetime.now():
            next_birthday = datetime.datetime(year=current_year + 1, month=birthdate.month, day=birthdate.day)

        # Determine the day of the week for the next birthday
        day_of_week = next_birthday.strftime("%A")

        # Return the result
        return f"Your next birthday will fall on a {day_of_week}."
    except ValueError:
        return "Invalid date format. Please enter the date in the format YYYY-MM-DD."


# Example usage for testing
if __name__ == "__main__":
    # Replace input with a predefined value for testing purposes
    test_birthdate = "1990-07-15"  # Example birthdate
    print(get_next_birthday_day(test_birthdate))
