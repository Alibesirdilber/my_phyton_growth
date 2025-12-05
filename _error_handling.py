a = 5
b = 7
c = a/b
x = 3
d = x
name : "Ali"
character : name[6]

#thereare3lettersinthename
#thatswhyweshouldhavewritten3

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
