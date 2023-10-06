# List datatype in function

marks = [88 , 75 , 90 , "Jarif" , True ] 
print(marks)
print(marks[0])
print(marks[-3]) # Negative Index
print(marks[len(marks) - 3]) # converting to the positive index 


colors = ["Red" , "Green " , "Blue" , "Yellow" , "Purple"]
#         [0]       [1]        [2]       [3]        [4]

print(colors[1:]) # set up a range for print the element
print(colors[1:len(colors) - 1])
print(colors[1:4:2]) # jump index 

if "pink" in colors: #Finding element in list
    print("Yes!") 

else:
    print("No")

# Same thing applies for strings as well
# if "Gre " in "Green":
#     print("Yes")

# List comprehension

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)

