# Enumerate Function

# Normal function
# marks = [12 , 56 , 32 , 98 , 45 , 1 , 4 ]
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Jarif awesome !")
#     index += 1


#Enumerate function
marks = [12 , 56 , 32 , 98 , 45 , 1 , 4 ]

for index , mark in enumerate(marks):
    print(index , mark)
    if index == 3:
        print("Jarif awesome !")
    