"""     Creating files & doing operations       """

# Creating a file in Python is straightforward using the built-in open() function. Here's how we can do it:

"""
syntax:
file = open("filename.txt", "mode")
file.close()

"""

# Common Modes
# 'w' (Write): Creates a new file if it doesn't exist, or truncates (clears) the file if it exists.
# 'a' (Append): Creates a new file if it doesn't exist; appends to the file if it exists.
# 't' (Text Mode): Default mode for reading/writing text.
# 'b' (Binary Mode): Used for binary files (like images or executables).

# Example 1: Create and Write to a File

# Create or overwrite a file
with open("example1.txt", "w") as file:
    file.write("Hello, world!")

# Append to an existing file
with open("example2.txt", "a") as file:
    file.write("\nAppending new text!")

# Writing binary data
with open("example3.bin", "wb") as file:
    file.write(b"Binary data here!")
