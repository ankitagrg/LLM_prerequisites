def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Please enter valid numbers!")
        return None
    else:
        print(f"Division successful! Result = {result}")
        return result
    finally:
        print("Operation complete.")

# --- Example Usage ---
divide_numbers(10, 2)   
divide_numbers(5, 0)   
divide_numbers("a", 3)  
