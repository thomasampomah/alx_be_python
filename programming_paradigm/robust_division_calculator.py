def safe_divide(numerator, denominator):
    try:
        results = numerator / denominator
        return ("The result of the division is {results:.1f}")
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.")
    except ValueError:
        return ("Error: Please enter numeric values only.")
    