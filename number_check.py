# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

print(number, "is an", result, "number.")