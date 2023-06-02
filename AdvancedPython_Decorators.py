import time
from functools import wraps

## Closure

# Eine closure function ist eine innere function, die zugriff auf auf die lokalen variablen der
# aeusseren function hat

def outer_fn(fn):   #outer_fn ist der Decorator, der eine andere function entgegen nimmt, hier fn()
    def inner_fn():
        fn_result = fn()
        return fn_result
    return inner_fn

def print_hello_world():
    print("hello world")


def outer_fn(message):
    outer_message = "Outer" + message
    current_time = time.time()
    
    def inner_fn():
        print("Inner: '" + outer_message + "'")
        print("Current time: ", current_time)
    return inner_fn()

outer_fn("hello world")

## Decorators - Nimmt andere Func entgegen

# -warps a function by another function
# -takes a function as an argument, returns a closure
# -the closure runs the previous passed function with the *args and **kwargs arguments
# Decorator nimmt andere Function entgegen, Funktionsobjekt

def outer_fn(fn): # Decorator
    def inner_fn():
        fn_result = fn()
        return fn_result
    return inner_fn

def print_hello_world():
    print("Hello world")

decorated_print_hello_world = outer_fn(print_hello_world)
decorated_print_hello_world()

def decorator(fn):
    print("Start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("Start wrapper function from: ", fn.__name__)
        fn_result = fn(*args, **kwargs)
        print("End wrapper function from: ", fn.__name__)
        return fn_result
    print("End decorator function from: ", fn.__name__)
    return wrapper

def print_arguments(a, b, c=None):
    print(f"A: {a}, A: {b}, C: {c}")


decorated_print_arguments = decorator(print_arguments)


decorated_print_arguments(a=1, b=2, c=3)

# @DecoratorFunctionName
@decorator
def print_arguments2(a, b, c=None):
    print(f"A: {a}, A: {b}, C: {c}")

print_arguments2(a=1, b=2, c=4)

def decorator(fn):
    def wrapper(*args, **kwargs):
        result = volumen(*args, **kwargs)
        return result
    return wrapper

def volumen(radius, pi, hoehe):
    print(radius*radius*pi*hoehe)

decorated_volumen = decorator(volumen)
decorated_volumen(radius=1, pi=3.145, hoehe=1)



