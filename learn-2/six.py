#coding=utf-8

class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' %self.name

    __repr__ = __str__

# print (Student('Michael'))


class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self): #python3中用__next__
        self.a,self.b = self.b , self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

# for n in Fib():
#     print(n)

class Fibt(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            a,b = 1,1
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a,b = b,a+b
            return L[start:stop:step]
f = Fibt()
print f[0]
print f[0:5]
print f[:10]
print f[:10:2]
