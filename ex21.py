def add(a,b) :
    print(f"Adding {a} + {b}")
    return a+b

def substract(a,b) :
    print(f"Subsracting {a} + {b}")
    return a-b

def multiply(a,b) :
    print(f"Multipying {a} * {b}")
    return a*b

def divide(a,b) :
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(20,8)
height = substract(200,33)
weight = multiply(9,7)
iq = divide(100,1)

print(f"Age : {age} \n Height : {height} \n Weight : {weight} \n IQ : {iq}\n")

#Puzzle for extra credit, type in anyway.

print("Here is Puzzle")

what = add(age,substract(height,multiply(weight,iq)))

print(f"That's becomes: ", what , "can you do by hands?")
