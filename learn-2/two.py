#coding=utf-8

class Animal(object):
    def run(self):
        print ('Animal is running ...')




class Dog(Animal):
    def run(self):
        print ('Dog is running ...')

class Cat(Animal):
    def run(self):
        print ('Cat is running ...')

class Shepherd(Dog):
    def run(self):
        print ('Shepherd is running ...')

class Tortoise(object):
    def run(self):
        print ('Tortoise is running ...')

def run_twice(a):
    a.run()
    a.run()


a = Animal()
b = Dog()
c = Shepherd()
d = Tortoise()
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Shepherd())
# run_twice(Tortoise())

print isinstance(b,Dog)
print isinstance(b,Animal)
print isinstance(b,Shepherd)
print isinstance(b,Tortoise)
print isinstance(b,Animal) and isinstance(b,Shepherd)
print isinstance('b',int )
print isinstance((1, 2, 3), (list, tuple))
