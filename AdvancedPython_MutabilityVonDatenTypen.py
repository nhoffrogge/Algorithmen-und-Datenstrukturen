def print_memory_adress(var):
    print(hex(id(var)))

# Immutable types: int, float, bool, str, tuple
# Mutable types: list, dict, set, etc.

my_int1 = 43
my_int2 = 22

print_memory_adress(my_int1)
print_memory_adress(my_int2)

'''var name zeigt erst auf speicherplatz fuer 43, dann auf speicherplatz fuer 22. speicherplatz fuer 43 kann
kann nicht ueberschieben werden.'''

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print_memory_adress(my_list)

my_list[0] = -1

print_memory_adress(my_list)

my_list.append(4)
print_memory_adress(my_list)

'''var name zeigt auf den speicherplatz der list, auch wenn die liste verändert wird.'''