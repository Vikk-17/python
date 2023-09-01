# ERROR

class ParentClass:
    def printHello(self):
        print("Helloo world!")

class ChildClass:
    def someNewMethod(self):
        print("ParentClass objects don't have this method.")

class GrandchildClass:
    def anotherNewMethod(self):
        print("Only GrandchildClass objects have this method.")

print('Create a ParentClass object and call its method.')
parent = ParentClass()
parent.printHello()

print('Create a ChildClass object and calls its method.')
child = ChildClass()
child.printHello()
child.someNewMethod()

print('Create a GrandchildClass object and calls its method.')
grandChild = GrandchildClass()
grandChild.printHello()
grandChild.someNewMethod()
grandChild.anotherNewMethod()

print('An error:')
parent.someNewMethod()