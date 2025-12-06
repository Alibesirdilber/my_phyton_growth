country = input ("what country do you live in?")

if country.lower() == "turkey":
    # Corrected variable name from 'provinve' to 'province'
    province = input ("what state/province do you live in?") 
    
    # Correct indentation for the inner if/elif/else block
    if province in ("Ankara", "İzmir", "İstanbul"):
        tax = 0.05
    elif province.lower() == "hatay": # Used .lower() for a more robust check
        tax = 0.13
    else: 
        tax = 0.1
else:
    # This else is for the main 'if country.lower() == "turkey":'
    tax = 0.0

print(tax)