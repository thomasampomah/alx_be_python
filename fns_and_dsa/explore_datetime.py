from datetime import datetime, timedelta

current_date = datetime.datetime.now()

formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")


def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")


def calculate_future_date():
    number_of_days =  int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta (number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"future date will be {formatted_future_date} after adding {number_of_days} of days to the current date.")







