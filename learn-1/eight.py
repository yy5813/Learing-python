#coding=utf-8
#空字符串删除
# def not_empty(s):
#     return  s and s.strip()
#
# L = list(filter(not_empty,['A','','B',None,'c','  ']))
# print L

# print sorted([23,45,-23,-12,12],key=abs)
# print sorted(['bob','about','Zoo','Credit'],key=str.lower, reverse=True)

#练习 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(n):
    return n[0]
print sorted(L,key = by_name)
#再按成绩从高到低排序：
def by_scort(s):
    return s[1]
print sorted(L,key = by_scort,reverse = True)
