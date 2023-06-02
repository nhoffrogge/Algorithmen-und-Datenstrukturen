import random
random.seed(42)

def print_memory_adress(var):
    print(hex(id(var)))


my_value = 10
print_memory_adress(my_value)

my_int1 = 35
my_int2 = 35
my_int3 = 35

print_memory_adress(my_int1)
print_memory_adress(my_int2)
print_memory_adress(my_int3)

'''Beim start der python shell werden integer werte initialisiert
    wird der gleiche int werte mehrfach vergeben, wird mehrfach auf die speicheradresse gezeigt'''

my_int4 = 300
my_int5 = 300
print_memory_adress(my_int4)
print_memory_adress(my_int5)


my_bool1 = True
my_bool2 = True

print_memory_adress(my_bool1)
print_memory_adress(my_bool2)

'''klappt fuer bools, int, None'''


my_list1 = [1, 2, 3]
my_list2 = my_list1

print_memory_adress(my_list1)
print_memory_adress(my_list2)

'''variable my_list1 und my_list2 werden im speicher angelegt, beide zeigen aber auf die gleiche liste'''


my_list1 = []

def append_random_value(l):
    l.append(random.randint(-100, 100))

append_random_value(my_list1)

print(my_list1)

def square_list(l):
    print_memory_adress(l)
    l = [val**2 for val in l]   # hier wird neues Objekt l erzeugt, mylist2 bleibt auf dem bisherigen Speicherplatz, mit return wird my_list2 überschrieben
    print_memory_adress(l)
    return l

my_list2 = [1, 2, 3]

print_memory_adress(my_list2)
my_list2 = square_list(my_list2)
print_memory_adress(my_list2)