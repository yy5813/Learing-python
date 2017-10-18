#coding=utf-8
#传入函数
# def add(x,y,f):
#     return f(x)+f(y)
# print add(-5,6,abs)

#map
# def f(x):
#     return x * x
#
# r = map(f,[x for x in range(1,10)])
# print r
#
# z = map(str,[x for x in range(1,10)])
# print z

#reduce
# def add(x,y):
#     return x*20 + y
# r = reduce(add,[x for x in range(1,10) if x%2 != 0])
# print r
#str 转化成 int
# def str2int(s):
#
#     def fn(x,y):
#         return x * 20 + y
#     def char2num(s):
#         return {'0': 0,'1': 1,'2': 2,'3':3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9':9}[s]
#     return reduce(fn,map(char2num,s))
# print str2int('13579')

#练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
#
# def normalize(name):
#     def Name(x):
#         return x[0].upper() + x[1:].lower()
#
#     return map(Name,name)
#
# print normalize(['adam', 'LISA', 'barT'])

# def Name(x):
#     return x[0].upper() + x[1:].lower()
# L1 =['adam', 'LISA', 'barT']
# L2 = list(map(Name,L1))
# print L2

#练习：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# def prod(L):
#     def pro(x,y):
#         return x * y
#     return reduce(pro,L)
# print prod([3,5,7,9])

# 练习：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# def str2float(s):
#     s = s.split('.')
#     def fn1(x,y):
#         return x * float(10) + y
#     def fn2(x,y):
#         return x / float(10) + y
#     def str2num(str):
#         return {'0': 0,'1': 1,'2': 2,'3':3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9':9}[str]
#     return reduce(fn1,map(str2num,s[0])) + reduce(fn2,map(str2num,s[1])[::-1])/float(10)
# print str2float('123.456')

#素数

def _old_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _old_iter()
    while True:
        n = next(it)
        yield n
        it = filter (_not_divisible(n),it)
for n in primes():
    if n < 6:
        print n
    else:
        break

#回数
#
# def is_palindrome(n):
#     s = str(n)
#     for i in range(len(s)):
#         if s[i] == s[-1-i]:
#             return True
#         else:
# #             return False
# def is_palindrome(n):
#     if str(n) == str(n)[::-1]:
#         return True
#     else:
#         return False
#
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))
