# This one is like your scripts with argv
def print_two(*arg) :
    arg1, arg2 = arg
    print(f"arg1 : {arg1}", f"arg2 : {arg2}")

#ok, that *arg is actually pointless, we can just do this
def print_two_again(arg1,arg2) :
    print(f"arg1 : {arg1}", f"arg2 : {arg2}")

# this one take one argument
def print_one(arg1) :
    print(f"arg1 : {arg1}")

# This function take no argument
def print_none() :
    print("I got nothin'.")

print_two("Hi","Bye")
print_two_again("This","That")
print_one("One")
print_none()
