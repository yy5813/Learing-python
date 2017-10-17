#coding=utf-8
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
print list(map(lambda x: x * x , [x for x in range(1,10)]))

print list(x*x for x in range(1,10))
