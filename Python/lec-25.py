#Local vs Golbal variable in python

x = 10 # Global variable 

def my_function():
    global x    # global keyword
    x = 4
    y = 5 # Local Variable 
    print(f"The local variable is {y}")

my_function()    
print(f"The global variable is {x}")
# print(y) this will cause error because y is a local variable
            #and this is not accessible outside of the function