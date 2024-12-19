def convert_hours_to_seconds(hours):
    return hours * 60 * 60

# Main program
hours = float(input("Enter the number of hours: "))
seconds = convert_hours_to_seconds(hours)
print(f"{hours} hours is equal to {seconds} seconds")
