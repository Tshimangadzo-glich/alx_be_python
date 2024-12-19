# Simple Interest Calculator

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Main program
def main():
    print("Simple Interest Calculator")

    # Input from user
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in %): "))
    time = float(input("Enter the time (in years): "))

    # Calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)

    # Output the result
    print(f"The simple interest is: {interest}")

if __name__ == "__main__":
    main()
