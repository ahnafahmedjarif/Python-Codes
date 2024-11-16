"""Object and Class"""

"""
Class:
    * A class is a blueprint for creating objects.
    * It defines the properties (attributes) and behaviors (methods) that the objects created from  the class will have.

"""

"""
Object:
 *An object is an instance of a class. It has the attributes and methods defined in the class.
"""

# At first, we will create a turtle program for example

import turtle

# turtle.circle(50)

# turtle.done()

# Now will do the same program but using the Turtle Class
tur1 = turtle.Turtle()

tur1.circle(100)

# print(type(tur1)) Output: <class 'turtle.Turtle'>

# Let's create more object:

tur2 = turtle.Turtle()
tur3 = turtle.Turtle()

tur1.shape("circle")
tur2.shape("square")

tur1.left(30)
tur1.forward(100)

tur2.backward(50)

turtle.done()