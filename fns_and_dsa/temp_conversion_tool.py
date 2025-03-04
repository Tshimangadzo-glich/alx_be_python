FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True:
        degree = float(input("Enter the degree: "))
        unit = input("Is this in (C)elsius or (F)ahrenheit? (C/F): ").strip().upper()
        ["Is this temperature in Celsius or Fahrenheit? (C/F):"]
        if unit == 'C':   
            celsius = convert_to_celsius(degree)
            print(f"{degree}°F is equal to {celsius}°C")

        elif unit == 'F':
            fahrenheit = convert_to_celsius(degree)
            print(f"{degree} F is equal to {fahrenheit}")    
        else:
            print("Invalid degree. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    ValueError
    print("Invalid temperature. Please enter a numeric value.")
print = ["Enter the temperature to convert:"]
if __name__ == "__main__":
    main()
