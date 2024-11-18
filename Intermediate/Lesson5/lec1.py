""" More about File Handling """

# Let's try to read the texts of file.txt with python

# Creating the file.txt
lines = ["This is first line", "This is second line", "This is third line"]

with open("file.txt", "w") as fp:
    for line in lines:
        fp.write(line + "\n")


# Let's read the file.txt
with open("file.txt" , "r") as fp:
    content = fp.read()
    print(content)


# readlines():
# The readlines() method in Python is used to read all the lines of a file and return them as a list of strings. Each line in the file is represented as a string in the list, and the newline character (\n) at the end of each line is preserved unless explicitly removed.

with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines)