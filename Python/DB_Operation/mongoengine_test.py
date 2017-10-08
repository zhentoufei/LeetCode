# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/8 14:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'mongoengine.py'

from mongoengine import connect, Document, StringField, IntField, \
    FloatField, EmbeddedDocument, ListField, EmbeddedDocumentField

# 要把class Student(Document):修改成class Student(DynamicDocument):
from mongoengine import DynamicDocument  # 可以动态添加属性

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)


class Grade(EmbeddedDocument):
    ''' 成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)


# class Student(Document):
#     name = StringField(max_length=32, required=True)
#     age = IntField(required=True)
#     sex = StringField(choices=SEX_CHOICES, required=True)
#     grade = FloatField()
#     address = StringField()
#     grades = ListField(EmbeddedDocumentField(Grade))
#
#     meta = {
#         'collection': 'students'
#     }

class Student(DynamicDocument):
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students',
        'ordering': ['-age'],  # 排序方式,倒叙排列
    }


class TestMongoEngine(object):
    def add_one(self):
        yuwen = Grade(
            name='语文',
            score=90,
        )

        shuxue = Grade(
            name='数学',
            score=100,
        )

        stu_obj = Student(
            name='张三',
            age=15,
            sex='male',
            grades=[yuwen, shuxue],
        )
        stu_obj.remark = 'remark'  # 就可以在这里动态添加属性了
        stu_obj.save()
        return stu_obj

    def getOne(self):
        '''查询一条数据'''
        return Student.objects.first()

    def getMore(self):
        '''获取多条数据'''
        return Student.objects.all()

    def getFromId(self, id):
        '''根据id获取数据'''
        return Student.objects.filter(pk=id).first()

    def update(self):
        '''修改数据'''
        # 修改所有男生年龄，增加10岁
        return Student.objects.filter(sex='male').update(inc__age=10)

    def delete(self):
        # 删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        # 删除多条数据
        return Student.objects.filter(sex='male').delete()


if __name__ == '__main__':
    obj = TestMongoEngine()

    rest = obj.add_one()
    print rest.pk
