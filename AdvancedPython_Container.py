# Tuple packing and upacking

def function():
    return (10, 20, True, None)

tpl = function()

print(tpl)

my_int, my_float, my_bool, my_None = tpl

my_int2, _, my_bool2, _ = tpl

my_int3, my_float3, *packed_tpl = tpl

print(packed_tpl)

# Dict

# keys: nur immutable type: book, int, float, str, tuple, None, key wird von einer hash function gelesen

# Dict merge

my_dict1 = {'a': 1, 'b':2}
my_dict2 = {'c': 3, 'd':4}
my_dict3 = {'e': 5, 'f':6}

# my_result_dict3 = my_dict1 | my_dict2 für python 3.9
my_result_dict1 = {**my_dict1, **my_dict2}

print(my_result_dict1)

# Sets

# Typese for set values: bool, int, float, str, tuple, None (immutable types)


try:
    my_set1 = {1, 2, 3, [1]}
except TypeError as e:
    print(e)

# Set comp

my_set_comp = {i for i in range(10)}
print(my_set_comp)