#coding=utf-8

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >=90:
            return ('%s: A' % self.__name)
        elif self.__score >=60:
            return ('%s: B' % self.__name)
        else:
            return ('%s: C' % self.__name)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('Bart Simpson',59)
bart.print_score()
print bart.get_grade()
bart.score = 78
bart.print_score()
print bart.get_score()
