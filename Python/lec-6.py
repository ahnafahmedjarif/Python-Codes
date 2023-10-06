# For loop 
# In string

name  = "Arham"

for i in name:
    print(i , end=", ")
    if i == "r":
        print("This is something special.")

# In list

colors = ["Red" , "Green" , "Purple" , "Orange" , "Black" , "White"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# In Number

for i in range(1 , 20):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1,20,4):
    print(i)