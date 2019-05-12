class Parent(object):

    def implict(self):
        print("Parent implicit()")

class Child(Parent):

    def implict2(self):
        print("Son implicit2()")

dad = Parent()
son = Child()

dad.implict()
son.implict()
son.implict2()
