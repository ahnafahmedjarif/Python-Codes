""" Module and Package 

A module is simply a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Modules can define functions, classes, and variables that can be imported and used in other modules or scripts.

A package is a way of structuring Python’s module namespace by using “dotted module names”. A package is a directory that contains a special file named __init__.py along with other modules. The __init__.py file can be empty, but it usually contains the initialization code for the package.

Directory stucture:

    mypackage/
    __init__.py
    module1.py
    module2.py

"""

# To use something from module 
# Structure: package_name.module_name.function_name()

# To use class's method from module
# Structure: package_name.module_name.class_name.function_name() 

# Example:

from datetime import datetime
d = datetime.today()
print(d) 