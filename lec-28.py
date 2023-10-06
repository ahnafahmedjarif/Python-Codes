# seek() and tell() in python

# with open ('myfile4.txt' , 'r') as f:
#     # Move to the 10 bytes in the file
#     f.seek(10)

#     # Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

# tuncate() method

with open('myfile4.txt' , 'w') as f:
    f.write("Hello world")
    f.truncate(5)
    
with open('myfile4.txt' , 'r') as f:
    print(f.read())