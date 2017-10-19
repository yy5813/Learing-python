#coding=utf-8

# class Student(object):
#     name = 'Student'
#
# s = Student()
# print s.name
# print Student.name

# class Student(object):
#     pass
#
#
# # s = Student()
# # s.name = 'Michael'
# # s.age = 25
# # print s.name,s.age
#
# def set_age(self,age):
#     self.age = age
#
# Student.set_age = set_age
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print s.age
# s2 = Student()
# s2.set_age(23)
# print s2.age

class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass


s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 98
print s.name,s.age
# print s.score
t = GraduateStudent()
t.score = 98
print t.score
