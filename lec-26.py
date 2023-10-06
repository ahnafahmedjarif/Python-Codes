# File io in python

# Reading file
r = open('myfile.txt' , 'r')
# print(f)
txt = r.read()
print(txt)
r.close()

# Writing file
w = open('myfile.txt' , 'w')
wrt = w.write("Hey everyone!!")
# print(wrt)
w.close()

# Append file
a = open('myfile.txt' , 'a')
# apnd = a.write("Welcome to the python code")
# print(apnd)
a.close()


# The 'with' statement

with open('myfile.txt' , 'a') as a:
    a.write("Hey I am inside 'with'")
