print("Let's practice Everything.")
print("You\'d need to know \'bout escape with \\ that do \n newlines and \t tbs.")

poem = """
\t The lovely World
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanantion
\n\t\twhere there is none.
"""
print("------------")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print(f"This Value is five : {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    cartes = jars / 100
    return jelly_beans, jars, cartes

start_point = 10000
beans, jars, cartes = secret_formula(start_point)

#remember that this is the another way to format a string
print("With a starting point of : {}".format(start_point))
# it is just like f"" string
print(f"We'd have {beans} beans, {jars} jars, {cartes} cartes.")

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is a easy way to apply a list to format starting
print("We'd have {} beans, {} jars, {} cartes".format(*formula))
