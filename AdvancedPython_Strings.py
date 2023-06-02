import os
from pathlib import Path

def memory_adress(var):
    return hex(id(var) % 0xFFFFFFF)

def print_string_info(st):
    print(f"String adress: {memory_adress(st)}")
    for val in st:
        print(f"Val: {memory_adress(val)}")
    print("\n")

# stings sind immutable, daher lanege kann sich nicht aendern und sind hashable

my_name = 'Nilss'

print(my_name)

print_string_info(my_name)

# always use f strings

my_int = 1000
my_float = 42.112344
my_name = 'Nils Hoffrogge'

my_str = f"my_name: {my_name}, my_int: {my_int:10d}, my_float: {my_float:.32}"

print(my_str)

# " or ' inside of f- strings

my_dict = {"a": 1}

my_str2 = f"{my_dict['a']}"

print(my_str2)

# File path

porject_path = os.path.abspath(
    "C:/Users/00087043/Documents/5 - Training/software and coding/Python/exchange/"
)

file_path = os.path.join(
    porject_path,
    "Algorithmen-und-Datenstrukturen",
    "irgendwas.txt"
)
# benutzt absoluten Pfad, pardir geht ein Verzeichnis hoeher
porject_path = os.path.abspath(
    os.path.pardir,
)
print(porject_path)

p = Path(file_path)

print([d for d in dir(p) if '_' not in d])
print(type(p))
print(p)
print(p.parent)
print(p.absolute())
print(p.is_dir())
print(p.is_file())

# Files

# Context managers provide enter() and exit() methods within with scope.

with open(file_path, "r") as f:
    content = f.readlines()
    print(f.closed)

print(f.closed)
print(f, type(f))


