# Default Arguments and Return Values

def g(p1, p2, p3 = 10, p4 = 10):
    print(f'p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}')

int1 = 10
int2 = 20
int3 = 30
int4 = 40
# Key word arguments
g(int1, int2, p3 = int3, p4 = int4)

# Positional Arguments
# *args: variable number of pos. arguments

def my_function(a, b, *args):
    print(*args, type(args))
    print(f'a: {a}, b: {b}, args: {args}')

my_function(1, 2, 3, 4)

# Keyword arguments
# Reihenfolge: Normal Args; *Args, Default Args, **Kwargs
# *Args: Tuple
# *Kwargs: Dict

def my_function(a, *args, x=2, y=3, z=4, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'a: {a}, x: {x}, y: {y}, z: {z}\nargs: {args}\nkwargs: {kwargs}')

my_function(1, 2, 4, x=13.37, b=False, c=30, d=40.5)