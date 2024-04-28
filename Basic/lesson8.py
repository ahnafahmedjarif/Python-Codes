""" lets make a letter grade programme """

marks = int(input("Enter your marks: "))

if marks >= 80:
    grade = "A+"

elif marks >= 70:
    grade = "A"

elif marks >= 60:
    grade = "A-"

elif marks >= 50:
    grade = "B"

else:
    grade = "F"

print("Your grade is", grade)
    


""" Check weather a number is positive or negative """

numbers = int(input("Enter any number: "))

if numbers > 0:
    print("The number is positive")

else:
    print("The number is negative")



""" Check weather a number is even or odd """

num = int(input("Enter any number: "))

if num % 2 == 0:
    print("The number is an even number") # condition for even number

else:
    print("The number is an odd number")


