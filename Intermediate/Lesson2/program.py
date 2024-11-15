import lesson2
# import trial 

# Here we are importing the lesson2.py file and trying to use the functions of lesson2.py
# So that's why, the lesson2.py is working as a Module.

print("Hello, I am inside program.py!")


n = lesson2.find_fib(15)

print(f"15th fibonacci number is {n}")


# Now if we want to unprint the statement which are mainly showing while running the lesson2.py,
# we need to use a global variable called "__name__"

# To use it, we will create a file named trial.py

# print(trial.__name__)