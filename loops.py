names = ['ali', 'dilara', 'dilan']

print("\n--- Temporary Reverse Sorting (Z-A) ---")

# The sorted() function is different from .sort(). It returns a BRAND NEW sorted list, 
# leaving the original 'names' list completely unchanged. 
# This is useful when you need a sorted view temporarily, but the original order 
# must be preserved for later use in the program.

# Setting the 'reverse=True' argument tells the function to sort the items 
# in descending order (from Z to A).
for name in sorted(names, reverse=True):
    # The loop iterates over the temporary, reverse-sorted list.
    print(f"Z-A Order: {name.title()}")

# After the loop finishes, if we were to print 'names', it would still be 
# ['ali', 'dilara', 'dilan'], proving the sort was temporary.

# Rationale: This is the preferred method for sorting when immutability 
# (keeping the original data intact) is a requirement.