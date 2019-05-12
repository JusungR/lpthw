class Parent(object):

    def override(self):
        print("P override()")

    def implicit(self):
        print("P implicit()")

    def altered(self):
        print("P alered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE override()")
        super(Child,self).altered()
        print("CHILD AFTER override()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("\n")
dad.override()
son.override()
print("\n")
dad.altered()
son.altered()
