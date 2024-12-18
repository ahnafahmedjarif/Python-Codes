""" Exeption Handling in Python """

# Exception handling in Python is done using try, except, else, and finally blocks. It allows you to gracefully handle errors and exceptions that may occur during runtime without crashing the program.


# Structure:

"""

try:
     # Code that may raise an exception
     risky_code()

except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")

else:
    # Code to run if no exception was raised
    print("No exceptions occurred!")

finally:
    # Code that will always run, regardless of whether an exception occurred
    print("Execution complete.")
    
"""
# Example 1: Handling Division by Zero

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful:", result)
finally:
    print("Finished processing.")


# Example 3: Raising Exceptions

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(e)