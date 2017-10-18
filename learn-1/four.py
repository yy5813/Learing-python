#coding=utf-8
#递归函数
# def fact(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return n * fact(n-1)
#
# for i in range(1,100):
#     print 'n=',i,'n!=',fact(i)
#尾递归
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
#
# for i in range(1,100):
#     print 'n=',i,'n!=',fact(i)

#练习  汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,'A','B','C')
