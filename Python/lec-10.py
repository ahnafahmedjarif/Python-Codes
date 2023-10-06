# Function Argument in Python


# Defalt Arguments
def average(a = 9, b = 1):
    print("The average is " , (a+b)/2)
# average(4, 6)
average()
average(b = 9 , a = 21) # keyword argument

def name(fname , mname = "Ahmed" , lname = "jarif"):
    print("Hello" , fname , mname , lname)
name(fname = "Ahnaf") # Keyword argument 

# Required Argument
# In case we dont pass the arguments with key = value syntax  , then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should math with actual function definition

# Varialbe length arguments

def average2(*numbers):
    sum = 0
    for i in numbers:   
        sum = sum + i
    print("The average is " , sum/len(numbers))

average2(5,6)

# Return in function

def sum(x , y):
    result = x + y
    return result

addition = sum(2 , 5)
print("The result is" , addition)