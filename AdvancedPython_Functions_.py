# Default Arguments and Return Values

def g(p1, p2, p3 = 10, p4 = 10):
    print(f'p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}')

int1 = 10
int2 = 20
int3 = 30
int4 = 40
# Key word arguments
g(int1, int2, p3 = int3, p4 = int4)

# Ohne return gibt die Funktion nur None zurück

def append_list(my_list, value):
    my_list.append(value)

l = [1, 2]

l = append_list(l, 3)

print(l)


# Function Attributes

def grow_list(val, my_list=None):
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

my_func = grow_list

print(my_func, type(my_func))

def print_function_output(fn, **kwargs):
    print(fn(**kwargs))

print_function_output(my_func, val=10)

print(grow_list.__defaults__)
print(grow_list.__name__)
print(dir(grow_list.__code__))
print(grow_list.__code__.co_argcount)
print(grow_list.__code__.co_varnames)

# Auf keinen Fall mutable types als default Werte benutzen.

# BAD Idea

def grow_list2(val, my_list = []):
    my_list.append(val)
    return my_list

my_list2 = grow_list2(42)
print(my_list2)
my_list3 = grow_list2(43)
print(my_list3)

# GOOD idea

def grow_list3(val, my_list=None):
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

my_list3 = grow_list3(42)
print(my_list3)

my_list3 = grow_list3(43)
print(my_list3)