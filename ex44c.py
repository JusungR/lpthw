class Parent(object):

    def implicit(self):
        print("Parent altered()")

    def altered(self):
        print("PARENT altered")

class Child(Parent):

    def altered(self):
        print("CHILD, BERORE PARENT altred()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altred()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

print("-------------")
son.implicit()
