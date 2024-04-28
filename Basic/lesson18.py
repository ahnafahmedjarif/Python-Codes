"""             Global Variables Vs Local Variables             """

"""  Global Variables

* Global variables are declared outside of any function or class.
* They can be accessed and modified from any part of the program, including inside functions.
* To create a global variable within a function, you need to use the `global` keyword.

    Local Variables

* Local variables are declared within a function or a block.
* They are only accessible within the scope where they are defined, such as inside a function.
* Local variables cannot be accessed from outside the function they are defined in.
* If a local variable has the same name as a global variable, the local variable will take     precedence within the scope where it's defined. 

"""

x = 10 # global variable

def my_function():
    y = 5 # local variable
    print(y)

my_function()
print(x)
# print(y)  this will cause an error because y is a local variable and it is not accessible outside of the function

"""     `global` Keyword

the `global` keyword is used to declare a variable inside a function as a global variable. This means that the variable will be accessible and modifiable from anywhere in the program, including outside the function where it was originally defined.

"""

global_var = 10

def func():
    global global_var
    global_var = 20
    print("Inside func(), global_var is:", global_var)

func()
print("Outside func(), global_var is:", global_var)
