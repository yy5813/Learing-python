#coding=utf-8
# def power(x,n=2):
#     s = 1
#     for i in range(n) :
#         s = s * x
#         i = n - 1
#     return s
# s = 0
# j = 6
# for i in range(101):
#     s = s + power(i,j)
#     i = i + 1
# print (s)

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print add_end([1,2,3])
# print add_end()
# print add_end()

# def person(name,age,**kw):
#     return ('name:',name,'age:',age,'other:',kw)
#
# print person('Michael',30)
# print person('Bob',35, city='Beijing',job='Engineer')
nums = [1,2,3]
def cals(*numbers):
    sum = 0
    for n in numbers:
        sum =sum + n*n
    return sum
print cals(*nums)
