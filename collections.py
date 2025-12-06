# Initialize an empty dictionary named Ali. Dictionaries store data in key-value pairs.
Ali = {}
# Assign the value "Ali" to the key "first" (first name).
Ali["first"] = "Ali"
# Assign the value "Dilber" to the key "last" (last name).
Ali["last"] = "Dilber"

# Initialize a second empty dictionary named kumsal.
kumsal = {}
# Assign the value "kumsal" to the key "first".
kumsal["first"] = "kumsal"
# Assign the value "han" to the key "last".
kumsal["last"] = "han"

# Initialize an empty list named people. Lists are used to store ordered collections of items.
people = []
# Add the 'Ali' dictionary to the 'people' list as the first element.
people.append(Ali)
# Add the 'kumsal' dictionary to the 'people' list as the second element.
people.append(kumsal)
# Create a third dictionary inline and append it directly to the list.
# This is a concise way to add data that doesn't need its own variable name.
people.append({
    "first": "bill", 
    "last": "gates"
})

# Print the entire 'people' list, which contains all three dictionaries.
print(people)