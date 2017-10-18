#coding=utf-8
import functools

print int('100000',base = 2)
int2 =  functools.partial(int,base = 2)
print int2('100000')

print max(2,3,4,5,6,7)
max2 = functools.partial(max,10)
print max2(2,3,4,5,6,7)
