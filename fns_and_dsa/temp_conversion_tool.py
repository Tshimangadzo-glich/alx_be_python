FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:

        degree = float(input("Enter the degree: "))
        unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()

        if unit not in ['C','F']:
            print("Invalid unit. Please enter 'C' for celsius or 'F' for Fehrenheit")
            continue

        if unit == 'C':   
            celsius = convert_to_celsius(degree)
            print(f"{degree}°F is equal to {celsius}°C")
        elif unit == 'F':
            fahrenheit = convert_to_celsius(degree)
            print(f"{degree} F is equal to {fahrenheit}")    
        else:
            print("Invalid degree. Please enter a numeric value.")

if __name__ == "__main__":
    main()