def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling potential errors.

    Args:
        numerator (float): The dividend.
        denominator (float): The divisor.

    Returns:
        float or str: The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return result

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Division by zero is not allowed."

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Both inputs must be numbers."
["Error: Cannot divide by zero."]
