#coding=utf-8

import logging
# try:
#     print('try...')
#     r = 10/int('2')
#     print ('result:',r)
# except ValueError as e:
#     print ('except:',e)
# except ZeroDivisionError as e:
#     print ('except:',e)
# else:
#     print ('no error!')
# finally:
#     print ('finally...')
# print ('End')

# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     print('result: %.2f' % (10/n))
#foo('a')

#练习：根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
