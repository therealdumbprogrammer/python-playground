# Define a function named make_sandwich that:

# Takes one mandatory parameter bread_type.
# Takes two keyword arguments: filling (default value "ham") and extra (default value None).
# Takes any number of additional toppings using *toppings.
# Returns a description of the sandwich, including the bread type, filling, and any extra toppings.
# Call the function with different combinations of arguments:

# Only mandatory parameter.
# Mandatory and keyword arguments.
# Mandatory, keyword, and multiple toppings.

def make_sandwich(bread_type, *toppings, filling = "ham", extra = None):
    description = f"Sandwich with {bread_type}, {filling} filling"
    
    if extra != None:
        description += f", and {extra} extra"


    if toppings:
        all_toppings = ", ".join(toppings)
        description += f", and toppings: {all_toppings}"

    return description

print(make_sandwich("Whole bread"))  
print(make_sandwich("rye", filling="turkey", extra="cheese"))
print(make_sandwich("sourdough", "lettuce", "tomato", "mustard"))