""" Let's make a program with input(), int() and arithmetic operators """

number1 = int(input("Enter any integer: "))
number2 = int(input("Enter another integer: "))

sum = number1 + number2
sub = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_division = number1 // number2
modulus = number1 % number2
exponential = number1 ** number2

print(number1 , "+", number2 , "=", sum)
print(number1 , "-", number2 , "=", sub)
print(number1 , "*", number2 , "=", multiplication)
print(number1 , "/", number2 , "=", division)
print(number1 , "//", number2 , "=", floor_division)
print(number1 , "%", number2 , "=", modulus)
print(number1 , "**", number2 , "=", exponential)