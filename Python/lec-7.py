# While loop
# While loop is mainly used for complex condition

# With numbers

i = 0
while i < 5:
    print(i)
    i+=1
print("Done with the loop")

# Reverse Numbers
count =  5
while count > 0:
    print(count)
    count -= 1

print("Done with the loop")

# Do while loop

num2 = 0
while True:
    print(num2)
    if num2 % 100 == 0:
        break


# else with While

x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print("I am outside of While loop")

# condition with while

num = int(input("Enter the number: "))
while num <= 38:
    num = int(input("Enter the number: "))
    print(num)
print("Done with the loop")