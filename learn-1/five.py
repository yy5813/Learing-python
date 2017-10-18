#coding=utf-8
#切片
# L = list(range(100))
# print L[3:10:2]
#判断一个对象是否可以迭代
# from collections import Iterable
# print isinstance('abc',Iterable) #str是否可迭代
# print isinstance([1,2,3],Iterable) #list是否可迭代
# print isinstance(123,Iterable) #整数是否可迭代
# Python内置的enumerate函数可以把一个list变成索引-元素对
# for i,value in enumerate(['A','B','C']):
#     print(i,value)
#列表生成式
# L = list(range(1,11))
# M = [x*x for x in range(1,11)]
# N = [x*x for x in range(1,11) if x%2 ==0]
# O = [m+n for m in 'ABC' for n in 'DEF']
# d = {'x':'A','y':'B','z':'C'}
# P = [k + '=' + v for k,v in d.items()]
# Q = ['Hello','World','IBM','Apple']
# R = [s.lower() for s in Q]
# print R

#练习
L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print L2
