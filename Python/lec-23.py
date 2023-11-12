# Exercise - 4

# import section
import string
import random


message = input("Enter your message:  ")
# print("\n")
coding_string="" # empty string
list = message.split()
# print(list)


# Coding
for i in range (len(list)):
  if (len(list[i]) >=3):
    first_character=list[i][0]
    new_str=list[i].lstrip(first_character)
    new_str=new_str+list[i][0]
   
    # print(new_str)
    random_characters1 = ''.join(random.choices(string.ascii_lowercase, k = 3)) 
    random_characters2 = ''.join(random.choices(string.ascii_lowercase, k = 3)) 
    
    # print(random_characters)
    final_string=random_characters1+new_str+random_characters2
    coding_string=coding_string+" "+final_string
    
    # print(final_string)
  elif (len(list[i])==2):
    new_list_2=list[i][1] + list[i][0]
    # new_list_2=reversed(list[i])
    # print(new_list_2)
    
    coding_string=coding_string+new_list_2
  else:
    coding_string=list[i]+" "
print("Your coding message is below\n")
print(coding_string)
print("\n")

print("""Do you want to decode your message?
if Yes press 1""")
choice = int(input())
# Decoding
if(choice==1):
  Coding_list=coding_string.split()
  # print(Coding_list)
  for j in range (len(Coding_list)):
    if(len(Coding_list[j]) >=3):
      
      remove_random_character=Coding_list[j][3:-3]
      # print(remove_random_character)
      # remove_last_character=remove_random_character[j][:-1]
      last_character=remove_random_character[-1]
      # print(last_character)
      remove_last_character=remove_random_character[:-1]
      # print(remove_last_character)
      final_version=remove_random_character[-1] + remove_last_character[:]
      # print(final_version)
      decoding_string=decoding_string+" "+" "+final_version
    elif(len(Coding_list[j])==2):
        reverse_string=Coding_list[j][1]+Coding_list[j][0]
        # print(reverse_string)
        decoding_string=decoding_string+" "+" "+reverse_string
    else:
      decoding_string= Coding_list[j]

  print("Decoding string is: ")
  print(decoding_string)
else:
  print("Wrong Choice")

  
