#coding=utf-8
import functools
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1,3,4,6,8,9,4)
# print f()

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print f1(),f2(),f3()
#
# def count2():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(2,7):
#         fs.append(f(i))
#     return fs
# g1,g2,g3,g4,g5 = count2()
# print g1(),g2(),g3(),g4(),g5()
# print list(map(lambda x: x * x , [x for x in range(1,10)]))
#
# print list(x*x for x in range(1,10))




# def now():
#     print ('2017-10-18')
#
# f = now
# f()
# print now.__name__
# print f.__name__


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print ('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print ('2017-10-18')
# now()


# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print ('%s %s():' %(text, func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# # @log()
# @log('execute')
# def now():
#     print ('2017-10-18')
# # print now.__name__
# print now()

#练习 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print ('begin call %s():' % func.__name__)
#         func(*args,**kw)
#         print ('end call %s():' %func.__name__)
#     return wrapper
#
# @log
# def now():
#     print ('2017-10-18')
# now()

#练习 能否写出一个@log的decorator，使它既支持@log有支持@log('execute')
def log(text):
    if callable(text) == False:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print ('%s %s():' %(text, func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper2(*args,**kw):
            print ('call %s():' % text.__name__)
            text(*args,**kw)
        return wrapper2
@log
def now():
    print ('2017-10-18')
@log('execute')
def now2():
    print ('2017-10')
# print now.__name__
print now()
print now2()
