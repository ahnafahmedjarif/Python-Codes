# Exercise - 5

import random

options = ['Rock' , 'Paper' , 'Scissors']
point_user = 0
point_computer = 0
win = ((0 , 1) , (1 , 2) , (2 , 0))

for i in range(5):
    for index,option in enumerate(options): # enumerate function is used for print index easily
        print(f"{index}:{option}") # Printting the options with the index

    # Input and output from user
    user_choise = int(input("Enter the number of your option: ")) 
    print(f"\nYou have choosen {options[user_choise]}" )

    # Computers choise using the random module
    computer_choise = int(random.randint(0,len(options) - 1))
    print(f"computer has choosen {options[computer_choise]}")
    print()
    
    # The main logic statement

    # If the match is tie 
    if computer_choise == user_choise:
        print('Its tie')
        print()

    # If user won the match
    elif (computer_choise,user_choise) in win:
        print("You won")
        point_user += 5 # Adding 5 point , if user won
        print()

    # if computer won the match
    else:
        print("You lose !")
        point_computer += 5 # Adding 5 point , if computer won
        print()

# Final Statement

print("You point = " , point_user) # Printing users point
print("Computers point = " , point_computer) # Printing computers point

# Logic for comparison statement

if point_user == point_computer:
    print("The match is tie") 

elif point_user > point_computer:
    print("You have won the match")

else:
    print("You hava lost the game")

