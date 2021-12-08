"""
class Mom:

    broom = True
    moms_name = 'Zelda'

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
    def get_toy(self):
        return self.toy

    @get_toy.setter
    def get_toy(self, toy):
        self.toy = toy


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



print()
print()
print('********GETTERS AND SETTERS****************')
print(Ben.toy)
print(Ben.get_toy)
Ben.set = 'Alien'
print(Ben.get_toy)
print(Child.get_toy.setter)
"""



"""

class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        
    def hello(self):
        print('Hello')


class BellClock(Time):

    def __init__(self, hour, minute, name):
        super().__init__(hour, minute)
        self.name = name
        
    super().hello()


class StopWatch(Time, BellClock):

    #def __init__(self, hour, minute, seconds):
        #Time.__init__(Time, hour, minute)
        #self.seconds = seconds

print('***********BELLCLOCK OBJECT************')
clock = BellClock(12, 30, 'Big Ben')
print(f'{clock.name}, {clock.hour}:{clock.minute}')
#print('***********STOPWATCH OBJECT************')
#watch = StopWatch(18, 25, 30)
#print(f'{watch.hour}:{watch.minute}:{watch.seconds}')


"""

class Dog:

    def sound(self, name):
        print(f'Dog sound is {name}')


class Cat(Dog):

    def sound(self, name):
        Dog.sound(self, name)


cat = Dog()
cat.sound('Stormy')


