
"""
class Something:

    car = 'ford'
    house = 22

    @classmethod
    def drive(cls, car):
        cls.car = car
        return cls

    @staticmethod
    def driven(cls, car):
        cls.car = car
        return cls

    @staticmethod
    def drone():
        cls.car = car       # If you did not pass in the class then you also cannot update class variables
        car = car

    @staticmethod
    def foo():
        print('Hello')

classmeth = Something.drive('Ferrari')
staticmeth = Something.driven(Something(), 'Toyota')
print(staticmeth.car)
print(Something.foo())
"""




"""
class Person:

    def __init__(self, name, eyes, length):
        self.name = name
        self.eyes = eyes
        self.length = length

    def dunno(self):
        return 'Inside the function dunno'


person = Person('John', 'blue', 'short')
print(person.length)
"""




"""
class Animal:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sound():
        print("sound...")

    def eat(self):
        print(f"{self.name} eats")


class Dog(Animal):
    @staticmethod
    def sound(self):
        print("Dog barks")
"""





"""
class Class:

    today = 'Tuesday'

    def func(self):
        return 'in class called Class'


class Man(Class): # See how the class 'Man' inherits from the class 'Class'

    tomorrow = 'Wednesday'
    fun = super().func()


class_object = Class()
print(Class.func(class_object))
print(Class.today)  # See how a class attribute is accessed without creating a class object

print('******************')
man_object = Man()
print(man_object.tomorrow)
print(man_object.today)
print(man_object.func())    # Notice that I don't have to pass a 'self/class object' to func() here
"""




"""
class One:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

    def foo(self):
        return 'Hello class One'


class Two(One):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
one_object = One('John', 'Jameson')
two_object = Two('Rick', 'James')
"""



"""
class Something:

    car = 'Toyota'

    def foo(self):
        self.car = 'Ferrari'
        return self.car

    @staticmethod
    def without():
        car = 'Ferrari'
        return car

    @classmethod
    def func(cls):
        cls.car = 'Ford'
        return cls.car


class_object = Something()
print(class_object.foo())
print(Something.func())
"""




"""
class Mom:

    broom = True

    def cleaning(self, tool):
        print(f'Mom is doing some cleaning with a {tool}.')


class Dad:

    spanner = True

    def fixing(self, tool):
        print(f'Dad is doing some fixing with a {tool}.')


class Child(Mom, Dad):

    toy = True

    def playing(self, toy):
        print(f'Child is playing with a {toy}.')

    @property
    def searching(self):
        return f'Child is searching:  {self.toy}.'


child = Child()
child.playing('truck')
#child.fixing(Dad(), 'spanner')
print(child.searching)
"""


class Mom:

    broom = True
    moms_name = 'Zelda'

    def cleaning(self, tool):
        print(f'Mom is doing some cleaning with a {tool}.')

    @classmethod
    def change_moms_name(cls, name):
        cls.moms_name = name

    @staticmethod
    def moms_name_change(obj, name):
        obj.moms_name = name

    def name_change_mom(self, name):
        self.moms_name = name


class Dad:

    spanner = True
    beer = 2

    def fixing(self, tool):
        print(f'Dad is doing some fixing with a {tool}.')


class Child(Mom, Dad):

    toy = 'Dragon'
    name = None

    def __init__(self, name):
        self.name = name

    def playing(self, toy):
        print(f'Child is playing with a {toy}.')

    @property
    def searching(self):
        return f'Child is searching:  {self.toy}.'


print('***********NO CHANGES***********')
Ben = Child('Ben')
Susan = Child('Susan')
print(Mom.moms_name)
print(Ben.moms_name)
print(Susan.moms_name)
print('**********@CLASSMETHOD**********')
Mom.change_moms_name('Marlene')
print(Mom.moms_name)
print(Susan.moms_name)
print(Ben.moms_name)
print('**********@STATICMETHOD*********')
Mom.moms_name_change(Ben, 'Sheila')
print(Mom.moms_name)
print(Susan.moms_name)
print(Ben.moms_name)
print('**********NORMAL FUNCTION BEFORE CREATING A MOM OBJECT*******')
Mom.name_change_mom(Ben, 'Daphny')
print(Mom.moms_name)
print(Susan.moms_name)
print(Ben.moms_name)
print('**********NORMAL FUNCTION AFTER CREATING A MOM OBJECT********')
mom = Mom()
print(mom.moms_name)
mom.name_change_mom('Daphny')
print(mom.moms_name)
print(Susan.moms_name)








