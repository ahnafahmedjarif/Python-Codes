# Function in Pytohn

# Geometric mean and greater number

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

# greater number with function

def is_greater(a, b):
    # x = 9
    # y = 8
    if a > b: # Condition for greater number
        print(a , " number is greater")
    elif a < b:
        print(b," number is greater")
    else:
        print("Both number is equal")

a = 9
b = 8
calculateGmean(a,b)
is_greater(a,b)

c = 4
d = 3

calculateGmean(c , d)
is_greater(c , d)


# is_greater(10,9)

# pass in function

def is_lesser(a , b):
    pass
