# Lambda function in python

# normal function
# def double(x):
#     return x*2 

double = lambda x: x*2 # lambda function
cube = lambda x: x*x*x # lambda function
avg = lambda x,y: (x+y)/2

print(double(5))
print(cube(5))
print(avg(5, 10))