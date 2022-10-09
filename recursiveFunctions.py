def factorial(x):
    """This is a recursive function
    to find the factorial of an int
    """
    
    if x == 1:
        return 1
    else:
        return (x * factirial(x-1))
num = 3

print("The factorial of", num, "is", factorial(num))

# num=3: 3 * 2 * 1