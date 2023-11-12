# Recursion in python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))

# fibonacci series



def fibo(num):
    for i in range(num):
        a = 0
        b = 1
        s = 0
        print(s)
        s = a + b
        b = a
        a = s
        
fibo(9)

