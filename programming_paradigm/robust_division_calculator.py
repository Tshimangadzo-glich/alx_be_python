def safe_divide(numerator, denominator):
    
    try:
        # Attempt to convert inputs to floats
        num1 = float(numerator)
        num2 = float(denominator)
        if num1 != 0:
                result = num1 / num2 

        # Perform division
        result = numerator / denominator
        return result
        return f"The result of the division is {result}"
    
        else:
        raise ZeroDivisionError

    except ValueError:
        # Handle non-numeric inputs
        return ("Error: Both inputs must be numbers.")
["Error: Cannot divide by zero."]
["Error: Please enter numeric values only."]
