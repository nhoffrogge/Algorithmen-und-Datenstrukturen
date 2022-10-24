# Variable Function Arguments

def greet(name, msg="Good morning!", alter="25"):
    """
    This function greets to
    the person with the
    provided message.
    
    If the message is not provided,
    it defaults to "Good morning!"
    """
    
    print("Hello", name + ', ' + msg  + ', '+ alter)
    
greet("Kate")
greet("Bruce", "How do you do?")

# Arbitrary arguments

def greets2(*names):
    """
    This function greets all
    the person in the same tuple.
    """
    
    for name in names:
        print("Hello", name)
        
greets2("Monika", "Luke", "Steve", "John")