"""                     Break and Continue                  

Break: The `break` statement "jumps out" of loop.
continue: The `continue` statement "jumps over" one iteration in the loop.

"""

# Example of using break statement

while True:
    n = int(input("Enter any number (0 to exit): "))
    if n == 0:
        break
    print("Square of", n, "is", n*n)


# Example of using continue statement

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print only odd numbers
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        continue      # Skip the rest of the loop for even numbers
    print(num)


terminate = False

while not terminate:

    num1 = int(input("Enter any number (0 to exit):"))
    num2 = int(input("Enter another number (0 to exit):"))

    while True:
        operation = input("Enter add/sub or quit to exit: ")

        if operation == "quit":
            terminate = True
            break

        if operation == "add":
            print("Result is", num1 + num2)
            break

        if operation == "sub":
            print("Result is", num1 - num2)
            break

        if operation not in ["add", "sub"]:
            print("Unknow operation")
            continue