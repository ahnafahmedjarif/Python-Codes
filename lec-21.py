# Finally keyword in Python

def func1():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    
    except:
        print("Some error occurred")
        return 0
    
    finally:
         print("I am always executed")
    # print("I am always executed")

x = func1()
print(x)