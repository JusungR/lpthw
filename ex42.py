#Animal is-a object (yes, osrt of confusing) look at the extra credtit
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self,name):
        ##Class Dog has-a __init__ that makes self and name parameters.
        self.name = name

##Cat is-a Animal.
class Cat(Animal):

    def __init__(self,name):
        ##Class Cat has-a __init__ that makes self and name parameters.
        slef.name = name

##Person is-a Object.
class Person(object):

    def __init__(self,name):
        ##Class Person has-a __init__ that makes self and name parameters.
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a Person.
class Employee(Person):

    def __init__(self,name, salary):
        ##class Employee has-a __init__ that takes self, name and salary parameters.
        ##hmm what is this strange magic?
        super(Employee,self).__init__(name)
        ##From Employee get the salary attribute and set it to salary
        self.salary = salary

##Fish is-a object.
class Fish(object):
    pass

#Salmon is a Fish.
class Salmon(Fish):
    pass

##Halibut is a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## mary is a Person
mary = Person("Mary")

##From mary get pet attribute and set it to satan
mary.pet = satan

##Set crouse to an instance of salmon
crouse = Salmon()

##Set harry to an instance of Halibut()
harry = Halibut()
