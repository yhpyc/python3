#!/user/bin/env python3
# coding:utf-8
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def prints(self):
        print('name:%s,score:%s' % (self.name,self.score))


