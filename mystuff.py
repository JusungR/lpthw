def apple() :
    print("I am apple!")

orange = "I am orange."

class MyStuff(object) :

    def __init__(self) :
        self.orange = "And now one thousand years are gone."

    def apple(self) :
        print("I'm classic apple.")

    def pear(self) :
        print("I'm classic pear.")

thing = MyStuff()
thing.apple()
thing.pear()
print(thing.orange)
