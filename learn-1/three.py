#coding=utf-8
#默认参数
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
# 关键字参数
# def person(name,age,**kw):
#     return ('name:',name,'age:',age,'other:',kw)
#
# print person('Michael',30)
# print person('Bob',35, city='Beijing',job='Engineer')
#可变参数
# nums = [1,2,3]
# def cals(*numbers):
#     sum = 0
#     for n in numbers:
#         sum =sum + n*n
#     return sum
# print cals(*nums)

#参数组合
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

args = (1,2,3,4)
kw = {'x':99}
func(*args,**kw)
