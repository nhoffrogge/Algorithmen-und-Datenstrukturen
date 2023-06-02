# Position only

def pos_only_arg(a, /):
    print(a)

my_val = 5
pos_only_arg(1)
pos_only_arg(my_val)

# Parametername = Argument ist nicht erlaubt
# pos_only_arg(a = 1)

# Keyword only

def kwd_only_arg(*, a):
    print(a)

kwd_only_arg(a=3)
# Parametername = Argument muss gegeben werden

kwd_only_arg(a=3)

# Mischung

def combined_example(a, /, b, *, c):
    print(a, b, c)

# a kann nur ohne keyword uebergeben werden
# b mit und ohne keyword
# c muss mit keyword uebergeben werden

combined_example(1, b=2, c=3)
combined_example(1, 2, c=3)