
def validate_input(a, b):
    if isinstance(int,a) and isinstance(int,b):
        return True
    else: 
        print("No valid input")

@validate_input(a,b)
def AddNumbers(a, b):
    return a + b
print(AddNumbers(3,5))
