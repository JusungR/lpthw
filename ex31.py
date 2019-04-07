print("""You've enter a dark room with two doors.
Do you go through dor #1 and #2?""")

door = input("> ")

if door == "1" :
    print("There's giant bear here eating cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream the bear.")

    bear = input("> ")

    if bear == "1" :
        print("The bear eats your face off. Good job!")
    elif bear == "2" :
        print("The bear eats your legs off. Good job! ")
    else :
        print(f"Doing {bear} is probably better. Bear run away.")

elif door == "2" :
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2" :
        print("Your body survies powered by a mind of jello. Good job!")
    else :
        print("insanity rots your eyes into a pool of murk. Good job!")
else :
    print("You stumble around and fall on a kinfe and die. Good job!")
