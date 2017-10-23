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
# f = Fibt()
# print f[0]
# print f[0:5]
# print f[:10]
# print f[:10:2]

class Student1(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self,attr):
        if attr == 'score':
            return 99

        if attr == 'age':
            return lambda:25

        raise AttributeError('\'Student1\' object has no attribute \'%s\'' %attr)

# s = Student1()
# print s.name
# print s.score
# print s.age()
# print s.hige

class Chain(object):

    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# print Chain().status.user.timeline.list

class Student2(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student2('Michael')
s()
