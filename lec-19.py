# for loop with else

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry! no i")

# while loop with else:

x = 0
while x < 6:
    print(x)
    x += 1
    if x == 4:
        break

else:
    print("Sorry! no x")