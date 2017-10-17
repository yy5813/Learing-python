#coding=utf-8
#练习1
#请利用print()输出1024 * 768 = xxx：
#print '1024 * 768 =',1024*768

#练习2
#请打印出以下变量的值：
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# n = 123
# print n
# f = 456.789
# print f
# s1 = '\'Hello, world\''
# print s1
# s2 = '\'Hello, \\\'Adam\\\'\''
# print s2
# s3 = 'r\'Hello, \"Bart\"\''
# print s3
# s4 = 'r\'\'\'Hello,\nLisa!\'\'\''
# print s4
#python 练习3
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# s1 = 72
# s2 = 85
# r =(s2-s1)*100/s1
# print('%.1f%%' % r)
#练习4
# 请用索引取出下面list的指定元素：
# L = [
#     ['Apple','Google','Microsoft'],
#     ['Java','Python','Ruby','PHP'],
#     ['Adam','Bart','Lisa']
# ]
# #打印Apple
# print L[0][0]
# #打印Python
# print L[1][1]
# #打印Lisa
# print L[2][2]

#练习5
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
#
# 用if-elif判断并打印结果：

# height = 1.75
# weight = 80.5
# bmi = weight / (height * height)
# if bmi <= 18.5:
#     print '过轻'
# elif bmi >18.5 and bmi <= 25:
#     print '正常'
# elif bmi > 25 and bmi <= 28:
#     print '过重'
# elif bmi >28 and bmi <= 32:
#     print '肥胖'
# elif bmi > 32 :
#     print '严重肥胖'

#练习6
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart','Lisa','Adam']
# for l in L:
#     print 'hello,',l

#把(1, 2, 3)和(1, [2, 3])放入dict或set中
# a = ('a','b','c')
# b = ('a',['b','c'])
# dict1 = {a:"hello"}
# dict2 = {b:"hello"}
# print dict1[a]

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print hex(n1)
print hex(n2)
