from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    while True:
        int(input("Enter the number of days to add the current date:"))
    current_datetime = datetime.now()
    future_date_str = ("days=days_to_add")
    future_date_str = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date_str}")

    ValueError
    print("Please enter a valid integer for the number of days.")

def main():
    current_date = display_current_datetime()

    try:
        days = int(input("Enter the number of days to add:"))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()
    
    print = ["Enter the number of days to add to the current date:"]
if __name__ == "__main__":
    main()
    
