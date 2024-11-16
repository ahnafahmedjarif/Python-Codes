"""     Creating New Module     """

# At first we are making a program to generate fibonacci series below

def find_fib(n):
    if n <= 2:
        return 1
    
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next 

    return fib_next

def list_fib(n):
    fib_list = [1, 1]
    if n <= 2:
        return fib_list[:n]
    
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        fib_list.append(fib_next)

    return fib_list

# Now we can implement the knowledge of __name__....

if __name__ == "__main__":

    for x in range(1, 11):
        print(find_fib(x))

    print(list_fib(1))
    print(list_fib(2))
    print(list_fib(10))


# Now we will create a program.py and will try to use the fibonacci functions from program.py