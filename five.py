#coding=utf-8
#切片
# L = list(range(100))
# print L[3:10:2]
#判断一个对象是否可以迭代
# from collections import Iterable
# print isinstance('abc',Iterable) #str是否可迭代
# print isinstance([1,2,3],Iterable) #list是否可迭代
# print isinstance(123,Iterable) #整数是否可迭代

for i,value in enumerate(['A','B','C']):
    print(i,value)
