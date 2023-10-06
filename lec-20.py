# Exeption Handling in Python

a = input("Enter the number : ")    

print(f"Multiplication table of {a} is: ")
try: 
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("invalid input")

print("Some importent lines of code")
print("End of program")

try:
    num = int(input("Enter the integer : "))
    b = [6 , 3]
    print(b[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")