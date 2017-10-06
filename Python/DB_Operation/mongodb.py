# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/26 22:42'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'mongodb.py'


from datetime import datetime
from pymongo import MongoClient

#在pumongo里面使用了连接池把

class TestMongo(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
        post = {
            'title': '新的标题',
            'content': '博客内容...',
            'created_at': datetime.now()
        }
        return self.db.blog.posts.insert_one(post)

if __name__ == '__main__':
    # client1 = MongoClient()
    # client2 = MongoClient('localhost', 27017)
    # client3 = MongoClient('mongodb://localhost:27017/')
    pass
