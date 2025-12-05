a = 5
b = 7
c = a/b
x = 3
d = x
name : "Ali"
# The assignment operator should be the equals sign (=) instead of the colon (:).
# The correct syntax is: name = "Ali" 
character : name[6]
# IndexError: character = name[6]
# The 'name' variable holds the string "Ali".
# In Python, indexing starts at 0. The valid indices for "Ali" are 0 ('A'), 1 ('l'), and 2 ('i'). 
# Index 6 is far beyond the string's length (3 characters).
# This attempt to access an out-of-bounds index will cause an **IndexError** at runtime.

#there are 3 letters in the name
#thats why we should have written 3

except ZeroDivisionError
print ("the denominator should not be zero")
except NameError
print ("this variable has not been defined before")
except IndexError
print ("there is no such index")
except Exception
print ("an unknown error occured")

else:
print ("else block is working")
print (c)
print (character)

finally
print ("finally block is working")
# All block headers in Python (including 'except', 'else', and 'finally') 
# must end with a colon (:) to denote the start of the indented code block.
# Example: except ZeroDivisionError:
# Example: else:
# Example: finally: 
