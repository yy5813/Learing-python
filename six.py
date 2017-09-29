#coding=utf-8
#生成器
# g = (x * x for x in range(10))
# for n in g:
#     print(n)
#斐波那契数列

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n + 1
#
# for n in fib(10):
#     print(n)

#杨辉三角

def triangles():
    L = [1]

    while True:
        yield L
        L.append(0)
        L = [L[x]+L[x-1] for x in range(len(L))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
