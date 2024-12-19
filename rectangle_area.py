# Rectangle Area Calculator

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Main program
def main():
    print("Rectangle Area Calculator")

    # Input from user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area
    area = calculate_area(length, width)

    # Output the result
    print(f"The area of the rectangle is: {area} square units")

if __name__ == "__main__":
    main()
